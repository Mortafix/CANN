import Pruning as pr
import Clustering as cl
import numpy as np

# initial matrix
inpt,n1,n2,n3,oupt = 784,500,300,100,10
hl1 = np.random.rand(n1, inpt + 1) / n1
hl2 = np.random.rand(n2, n1 + 1) / n2
hl3 = np.random.rand(n3, n2 + 1) / n3
ol = np.random.rand(oupt, n3 + 1) / oupt
w = [hl1,hl2,hl3,ol]

print('### EXAMPLES ###\n')

#------------------------------------------------

# pruning

pr_test = pr.Pruning(w)							# creation pruning
csc_mats = pr_test.compression(10,'out')		# pruned weights - csc_matrix (compression)
pr_test.get_masks()								# non-zero weights masks
pr_test.serialize_mats('pruned_mats')			# serialize

print('# Pruned weights - CSC Matrix #')
print(csc_mats)
print()

#------------------------------------------------

# clustering

cl_test = cl.Clustering(w)						# creation clustering
centroids = cl_test.compression(10)				# centroids - kmeans (compression)
idx_mats = cl_test.build_index_matrix()			# indices matrix
cl_test.serialize_mats('clustered_mats')		# serialize

print('# Clustered weights - KMeans #')
print(centroids[0])
print(idx_mats[0])
print()

#------------------------------------------------

# pruning and clustering combined

pr_test = pr.Pruning(w)							# creation pruning
pruned_w = pr_test.compression(50)				# compression
cl_test = cl.Clustering(pruned_w)				# creation clustering
cl_test.compression(16)							# compression
csc_idx_matrix = cl_test.build_index_matrix()	# final matrix

print('# Pruned and Clustered weights #')
print(csc_idx_matrix)
print(csc_idx_matrix[0].A)