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
    connectivity = (None, knn_graph)[0]
    linkage = 'complete'
    model = AgglomerativeClustering(linkage=linkage, connectivity=connectivity,n_clusters=num_clusters)
    model.fit(X)
    labels = model.labels_
    plot_columns = plotable(X)
    centers = None
    plot1(num_clusters,labels,plot_columns,centers,ax)
    return labels, num_clusters
