import skfuzzy as fuzz
from readData import load_data
from saveResults import COLORS
# Import the PCA model.
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def cluster(X,fig,ax):

    # Required for fuzzy cmeans
    X = X.T
    print("Input shape:",X.shape)
    # num_cluster = 3
    num_cluster = int(input("Enter Number of cluster:"))
    # print(len(X[0]))
    # Regenerate fuzzy model with 3 cluster centers - note that center ordering
    # is random in this clustering algorithm, so the centers may change places
    cntr, u_orig, _, _, _, _, _ = fuzz.cluster.cmeans(
        X, num_cluster, 2, error=0.005, maxiter=1000)

    print("SHape of cntr:",cntr.shape)
    print("SHape of u_orig:",u_orig.shape)
    # print(len(u_orig[0]))
    # print(u_orig)
    # Show 3-cluster model
    ax.set_title('Trained model')

    pca_2 = PCA(2)
    X =X.T
    # Fit the PCA model on the numeric columns from earlier.
    plot_columns = pca_2.fit_transform(X)
    # Plot assigned clusters, for each data point in training set
    cluster_membership = np.argmax(u_orig, axis=0)
    # print(cluster_membership)
    clusters = {i: np.where(cluster_membership == i)[0] for i in range(num_cluster)}
    print(clusters)
    for j in range(num_cluster):
        ax.plot(plot_columns[clusters[j],0],
                 plot_columns[clusters[j],1], 'o',
                 label='series ' + str(j), color=COLORS[j])
    # Mark the center of each fuzzy cluster
    # plot_centers = pca_2.fit_transform(cntr)
    # print(plot_centers)
    # for pt in plot_centers:
    #     ax.plot(pt[0], pt[1], 'rs')
    ax.legend()

    return cluster_membership
