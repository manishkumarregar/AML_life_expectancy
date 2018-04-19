import os
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import AffinityPropagation
import matplotlib.pyplot as plt
from itertools import cycle
from readData import load_data
from dim_reduction import reduce_dim
from saveResults import save_fig,COLORS
# Make Dummy Data
# centers = [[1, 1], [-1, -1], [1, -1]]
# X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5, random_state=0)

def cluster(X,fig,ax):

    # X , days_to_death = load_data()
    # X = reduce_dim(X)
    # Setup Affinity Propagation
    af = AffinityPropagation(preference=-50).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    # print(labels)
    # print(len(labels))
    print(cluster_centers_indices)
    no_clusters = len(cluster_centers_indices)

    print('Estimated number of clusters: %d' % no_clusters)
    # Plot exemplars

    # plt.close('all')
    # plt.figure(1)
    # plt.clf()

    # colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    colors = COLORS
    for k, col in zip(range(no_clusters), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        ax.plot(X[class_members, 0], X[class_members, 1], '.', color=col)
        ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
        for x in X[class_members]:
            ax.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    return labels
