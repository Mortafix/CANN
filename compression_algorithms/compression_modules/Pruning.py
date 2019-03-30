import numpy as np
from scipy.sparse import csc_matrix,issparse

class Pruning:
    
    def __init__(self,weights):
        self.n_hidden_layers = len(weights)-1
        self.features = weights[0].shape[0] if weights[0].shape[0] > weights[0].shape[1] else weights[0].shape[1]
        self.outputs = weights[self.n_hidden_layers].shape[0] if weights[self.n_hidden_layers].shape[0] < weights[self.n_hidden_layers].shape[1] else weights[self.n_hidden_layers].shape[1]
        self.neurons = [x.shape[1] if x.shape[0] > x.shape[1] else x.shape[0] for x in weights[:-1]]
        self.weights = weights
        self.pruned_weights = None
    
    def compression(self,percentage,method='out'):
        self.perc = percentage
        self.met = method
        self.pruned_weights = [csc_matrix(self._Pruning__pruning_process(x)) for x in self.weights]
        return self.pruned_weights
    
    def get_masks(self):
        if self.pruned_weights:
            return [x.A != 0 for x in self.pruned_weights]
        else:
            raise Exception('Can\'t get Masks before pruning')

    def serialize_mats(self,file):
        if self.pruned_weights:
            return np.save(file,self.pruned_weights)
        else:
            raise Exception('Can\'t save before pruning')
    
    def __pruning_process(self,mat):
        threshold = (100-self.perc)
        if self.met == 'inout':
            threshold /= 4
            perc_up,perc_down,perc_mid_up,perc_mid_down = 100 - threshold, threshold, 50 + threshold, 50 - threshold
            percentile_up = np.percentile(mat,perc_up)
            percentile_down = np.percentile(mat,perc_down)
            percentile_mid_up = np.percentile(mat,perc_mid_up)
            percentile_mid_down = np.percentile(mat,perc_mid_down)
        else:
            threshold /= 2
            if self.met == 'in': perc_up, perc_down = 50 + threshold, 50 - threshold
            elif self.met == 'out': perc_up, perc_down = 100 - threshold, threshold
            percentile_up = np.percentile(mat,perc_up)
            percentile_down = np.percentile(mat,perc_down)
        w_pruned = np.copy(mat)
        for i,row in enumerate(mat):
            for j,_ in enumerate(row):
                if self.met == 'in':
                    if mat[i,j] > percentile_down and mat[i,j] < percentile_up:
                        w_pruned[i,j] = 0
                elif self.met == 'out':
                    if mat[i,j] < percentile_down or mat[i,j] > percentile_up:
                        w_pruned[i,j] = 0
                elif self.met == 'inout':
                    if mat[i,j] < percentile_down or mat[i,j] > percentile_up or (mat[i,j] > percentile_mid_down and mat[i,j] < percentile_mid_up):
                        w_pruned[i,j] = 0
        return w_pruned

    # in place
    def __sparse_sub_dense(sparse,dense,mask):
        sparse.data -= dense.T[mask.T]

    def __delete_last_row(csc):
        i = csc.indptr[-1]
        indptr = csc.indptr[:-1]
        data = csc.data[:i]
        indices = csc.indices[:i]
        return csc_matrix((data,indices,indptr))