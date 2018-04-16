import numpy as np
from sklearn.decomposition import NMF
from readData import load_data
import matplotlib.pyplot as plt

def reduce_dim(X,num_features):
	
	model = NMF(n_components=num_features, init='random', random_state=0)
	reduced_X = model.fit_transform(X)
	# # print(reduced_X)
	# dim1 = reduced_X[:,0]
	# dim2 = reduced_X[:,1]
	# print(dim2)
	# plt.plot(dim2)
	# # plt.scatter(dim1,dim2)
	# plt.show()
	return reduced_X