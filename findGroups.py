from scipy.stats import kde
import matplotlib.pyplot as plt 
import numpy as np  
from sklearn.cluster import MeanShift, estimate_bandwidth

def get_grps1(possible_grps):
	x = np.array(possible_grps)
	density = kde.gaussian_kde(x) # x: list of price
	xgrid = np.linspace(x.min(), x.max(), x.size)   
	plt.plot(xgrid, density(xgrid))
	# plt.show()

def get_grps(possible_grps):
		
	# x = possible_grps# [1,1,5,6,1,5,10,22,23,23,50,51,51,52,100,112,130,500,512,600,12000,12230]

	# X = np.array(list(zip(x,np.zeros(len(x)))), dtype=np.int)
	# print(X)
	# bandwidth = estimate_bandwidth(X, quantile=0.1)
	# ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
	# ms.fit(X)
	# labels = ms.labels_
	# cluster_centers = ms.cluster_centers_

	# labels_unique = np.unique(labels)
	# n_clusters_ = len(labels_unique)

	# for k in range(n_clusters_):
	# 	my_members = labels == k
	# 	print ("cluster {0}: {1}".format(k, X[my_members, 0]))
	print(possible_grps)
	
	possible_grps = sorted(possible_grps)
	print(possible_grps)
	init = possible_grps[0]
	clusters = [[init]]
	for next in range(1,len(possible_grps)):
		if possible_grps[next] - init > 100:
			# New cluster
			clusters.append([possible_grps[next]])
		else:
			clusters[-1].append(possible_grps[next])
		init = possible_grps[next]
	print(clusters)
	print("*******")
	print('Number of Groups: ',len(clusters))
	print("*******")
	return len(clusters)

if __name__ == '__main__':
	get_grps([])