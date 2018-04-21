import os
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AffinityPropagation
import matplotlib.pyplot as plt
from itertools import cycle
from readData import load_data
from dim_reduction import reduce_dim, plotable
from saveResults import save_fig,COLORS, plot1


def cluster(X,fig,ax):

    # Setup Affinity Propagation
    af = AffinityPropagation(preference=-50).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    no_clusters = len(cluster_centers_indices)
    print('Estimated number of clusters: %d' % no_clusters)
    plot_columns = plotable(X)
    centers = plotable(X[cluster_centers_indices])
    plot1(no_clusters, labels, plot_columns, centers, ax)
    return labels, no_clusters
