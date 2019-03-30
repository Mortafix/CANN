import numpy as np
from scipy.sparse import csc_matrix,issparse
from sklearn.cluster import MiniBatchKMeans

class Clustering:
    
    def __init__(self,weights,random_seed=42):
        self.n_hidden_layers = len(weights)-1
        self.features = weights[0].shape[0] if weights[0].shape[0] > weights[0].shape[1] else weights[0].shape[1]
        self.outputs = weights[self.n_hidden_layers].shape[0] if weights[self.n_hidden_layers].shape[0] < weights[self.n_hidden_layers].shape[1] else weights[self.n_hidden_layers].shape[1]
        self.neurons = [x.shape[1] if x.shape[0] > x.shape[1] else x.shape[0] for x in weights[:-1]]
        self.weights = weights
        self.centers,self.index_matrix = None,None
        self.seed = random_seed
        self.sparse = True if any([issparse(x) for x in self.weights]) else False
    
    def compression(self,cluster):
        self.clusters = cluster
        if self.sparse:
            self.centers = [self._Clustering__build_clusters_sparse(self.clusters,x) for x in self.weights]
            return self.centers
        else:
            self.centers = [self._Clustering__build_clusters(self.clusters,x) for x in self.weights]
            return self.centers
    
    def build_index_matrix(self):
        if not self.centers:
            raise Exception('Can\'t get Index Matrix before clustering')
        else:
            if self.sparse:
                self.index_matrix = [self._Clustering__redefine_weights_sparse(w,c) for w,c in zip(self.weights,self.centers)]
                return self.index_matrix
            else:
                self.index_matrix = [self._Clustering__redefine_weights(w,c) for w,c in zip(self.weights,self.centers)]
                return self.index_matrix
            
    def get_shapes(self):
        return [w.shape for w in self.weights]
    
    def serialize_mats(self,file):
        if self.centers and self.index_matrix:
            return np.save(file,[self.centers,self.index_matrix])
        else:
            raise Exception('Can\'t save before clustering and index matrix')

    def __nearest_centroid_index(self,centers,value):
        centers = np.asarray(centers)
        idx = (np.abs(centers - value)).argmin()
        return idx

    def __build_clusters(self,cluster,weights):
        kmeans = MiniBatchKMeans(n_clusters=self.clusters,random_state=self.seed,init_size=3*self.clusters)
        kmeans.fit(np.hstack(weights).reshape(-1,1))
        return kmeans.cluster_centers_

    def __redefine_weights(self,weights,centers):
        arr_ret = np.empty_like(weights).astype(np.int16)
        for i, row in enumerate(weights):
            for j, col in enumerate(row):
                arr_ret[i,j] = self._Clustering__nearest_centroid_index(centers,weights[i,j])
        return arr_ret
    
    def __build_clusters_sparse(self,cluster,weights):
        kmeans = MiniBatchKMeans(n_clusters=self.clusters,random_state=self.seed,init_size=3*self.clusters)
        kmeans.fit(weights.data.reshape(-1,1))
        return kmeans.cluster_centers_

    def __redefine_weights_sparse(self,weights,centers):
        new_data_idx = [self._Clustering__nearest_centroid_index(centers,w) for w in weights.data]
        return csc_matrix((new_data_idx,weights.indices,weights.indptr))