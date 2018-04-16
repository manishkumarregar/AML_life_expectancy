import os
from saveResults import save_fig
# Import the kmeans clustering model.
from sklearn.cluster import KMeans,MiniBatchKMeans
from readData import load_data
# Import the PCA model.
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from dim_reduction import reduce_dim

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
	choice = input("Want to apply PCA(0/1):")
	if choice == '0':
		ax.scatter(x=X[:,0], y=X[:,1], c=labels)
		# plt.show()
	else:
		# Create a PCA model.
		pca_2 = PCA(2)
		# Fit the PCA model on the numeric columns from earlier.
		plot_columns = pca_2.fit_transform(X)
		# Make a scatter plot of each game, shaded according to cluster assignment.
		ax.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
		# print(days_to_death.shape)
		# plt.scatter(x=[i for i in range(len(clusters[0]))], y=days_to_death[clusters[0]])
		# Show the plot.
		# plt.show()
	return labels
