import skfuzzy as fuzz
from readData import load_data
from saveResults import COLORS, plot1
from dim_reduction import plotable
# Import the PCA model.
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def cluster(X,fig,ax):

    # Required for fuzzy cmeans(X is (num_feature,num_sample))
    X = X.T
    # print("Input shape:",X.shape)
    num_cluster = int(input("Enter Number of cluster:"))

    cntr, u_orig, _, _, _, _, _ = fuzz.cluster.cmeans(
        X, num_cluster, 2, error=0.005, maxiter=1000)

    X =X.T
    plot_columns = plotable(X)
    plot_centers = plotable(cntr)

    # Labels for each sample
    cluster_membership = np.argmax(u_orig, axis=0)
    # Clusters
    # clusters = {i: np.where(cluster_membership == i)[0] for i in range(num_cluster)}
    plot1(num_cluster, cluster_membership, plot_columns, plot_centers, ax)

    return cluster_membership, num_cluster
