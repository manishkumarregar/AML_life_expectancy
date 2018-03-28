# Import the kmeans clustering model.
from sklearn.cluster import KMeans
from readData import load_data
# Import the PCA model.
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np



# Initialize the model with 2 parameters -- number of clusters and random state.
kmeans_model = KMeans(n_clusters=8, random_state=1, n_init=10)
# Get only the numeric columns from games.
good_columns, days_to_death = load_data()
# Fit the model using the good columns.
kmeans_model.fit(good_columns)
# Get the cluster assignments.
labels = kmeans_model.labels_
# print(labels)

clusters = {i: np.where(labels == i)[0] for i in range(kmeans_model.n_clusters)}

print(clusters)
# Create a PCA model.
pca_2 = PCA(2)
# Fit the PCA model on the numeric columns from earlier.
plot_columns = pca_2.fit_transform(good_columns)
# Make a scatter plot of each game, shaded according to cluster assignment.
# plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
# print(days_to_death.shape)
plt.scatter(x=[i for i in range(len(clusters[0]))], y=days_to_death[clusters[0]])
# Show the plot.
plt.show()