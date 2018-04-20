import os
from saveResults import save_fig,COLORS, plot1
# Import the kmeans clustering model.
from sklearn.cluster import KMeans,MiniBatchKMeans
from readData import load_data
# Import the PCA model.
import matplotlib.pyplot as plt
import numpy as np
from dim_reduction import reduce_dim, plotable

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
import time

def cluster(X,fig,ax):
    labels = ''
    num_clusters = int(input("Enter Number of cluster:"))
    knn_graph = kneighbors_graph(X,30, include_self=False)
    # connectivity = [True, False]
    connectivity = (None, knn_graph)[0]
    # linkage = ['average', 'complete', 'ward']
    linkage = 'complete'
    # for index, linkage in enumerate(('average', 'complete', 'ward')):
    model = AgglomerativeClustering(linkage=linkage, connectivity=connectivity,n_clusters=num_clusters)
    model.fit(X)
    labels = model.labels_
    plot_columns = plotable(X)
    # centers = plotable(model.cluster_centers_)
    plot1(num_clusters,labels,plot_columns,None,ax)
    return labels, num_clusters
#
# def cluster(X,fig,ax):
#     labels = ''
# 	knn_graph = kneighbors_graph(X, 30, include_self=False)
# 	for connectivity in (None, knn_graph):
# 	    for n_clusters in (30, 3):
# 	        plt.figure(figsize=(10, 4))
# 	        for index, linkage in enumerate(('average', 'complete', 'ward')):
# 	            plt.subplot(1, 3, index + 1)
# 	            model = AgglomerativeClustering(linkage=linkage,
# 	                                            connectivity=connectivity,
# 	                                            n_clusters=n_clusters)
# 	            t0 = time.time()
# 	            model.fit(X)
# 	            elapsed_time = time.time() - t0
# 	            plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
# 	            plt.title('linkage=%s (time %.2fs)' % (linkage, elapsed_time),
# 	                      fontdict=dict(verticalalignment='top'))
# 	            plt.axis('equal')
# 	            plt.axis('off')
#
# 	            plt.subplots_adjust(bottom=0, top=.89, wspace=0,
# 	                                left=0, right=1)
# 	            plt.suptitle('n_cluster=%i, connectivity=%r' %
# 	                         (n_clusters, connectivity is not None), size=17)
#
#
# 	plt.show()
