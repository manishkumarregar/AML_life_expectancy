import os
from saveResults import save_fig,COLORS, plot1
# Import the kmeans clustering model.
from sklearn.cluster import KMeans,MiniBatchKMeans
from readData import load_data
# Import the PCA model.
import matplotlib.pyplot as plt
import numpy as np
from dim_reduction import reduce_dim, plotable

def cluster(X,fig,ax):

	num_clusters = int(input("Enter Number of cluster:"))

	minibatch_model = MiniBatchKMeans(n_clusters=num_clusters, init='k-means++', n_init=1,
					init_size=1000, batch_size=1000)
	minibatch_model.fit(X)
	labels = minibatch_model.labels_
	# clusters = {i: np.where(labels == i)[0] for i in range(minibatch_model.n_clusters)}

	plot_columns = plotable(X)
	centers = plotable(minibatch_model.cluster_centers_)

	plot1(num_clusters,labels,plot_columns,centers,ax)
	return labels, num_clusters
