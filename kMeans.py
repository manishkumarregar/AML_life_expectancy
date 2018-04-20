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
	choice = int(input("kMeans/MiniBatchKMeans(0/1):"))
	kmeans_model = ''
	if choice == '0':
		# Initialize the model with 2 parameters -- number of clusters and random state.
		kmeans_model = KMeans(n_clusters=num_clusters, random_state=1, n_init=10)
	else:
		# Initialize the model with 2 parameters -- number of clusters and random state.
		kmeans_model = MiniBatchKMeans(n_clusters=num_clusters, init='k-means++', n_init=1,
						init_size=1000, batch_size=1000)

	# Fit the model using the good columns.
	kmeans_model.fit(X)
	# Get the cluster assignments.
	labels = kmeans_model.labels_
	print(labels)

	clusters = {i: np.where(labels == i)[0] for i in range(kmeans_model.n_clusters)}
	# print(clusters)

	plot_columns = plotable(X)
	centers = plotable(kmeans_model.cluster_centers_)

	# Make a scatter plot of each game, shaded according to cluster assignment.
	# for i in range(num_clusters):
		# ax.scatter(x=plot_columns[clusters[i],0], y=plot_columns[clusters[i],1], c=COLORS[i])

	plot1(num_clusters,labels,plot_columns,centers,ax,scatter=False)

	return labels, num_clusters
