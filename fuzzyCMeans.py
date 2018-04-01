import skfuzzy as fuzz
from readData import load_data
# Import the PCA model.
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Get only the numeric columns from games.
X, days_to_death = load_data()
# Required for fuzzy cmeans
X = X.T
print("Input shape:",X.shape)
num_cluster = 3
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
fig2, ax2 = plt.subplots()
ax2.set_title('Trained model')

pca_2 = PCA(2)
# Fit the PCA model on the numeric columns from earlier.
plot_columns = pca_2.fit_transform(X)
# Plot assigned clusters, for each data point in training set
cluster_membership = np.argmax(u_orig, axis=0)
# print(cluster_membership)
clusters = {i: np.where(cluster_membership == i)[0] for i in range(num_cluster)}
print(clusters)
for j in range(num_cluster):
    ax2.plot(plot_columns[clusters[j],0],
             plot_columns[clusters[j],1], 'o',
             label='series ' + str(j))
# Mark the center of each fuzzy cluster
# plot_centers = pca_2.fit_transform(cntr)
# print(plot_centers)
# for pt in plot_centers:
#     ax2.plot(pt[0], pt[1], 'rs')
ax2.legend()
plt.show()
