import matplotlib.pyplot as plt
from readData import load_data
from saveResults import save_fig
from dim_reduction import reduce_dim
import kMeans, fuzzyCMeans, affinityPropagation

# Get only the numeric columns from games.
X, days_to_death = load_data()
choice = input('Want to reduce dimension(yes/no):')
if choice == 'yes':
    X = reduce_dim(X)

clustering_algo = {
    1 : kMeans,
    2 : 'MiniBatchKMeans',
    3 : fuzzyCMeans,
    4 : affinityPropagation
}

choice = input("Choose the clustering algo:")
algo = clustering_algo[int(choice)]
fig,ax = plt.subplots(2)
# clustering_algo[int(choice)].clustering_algo[int(choice)](X)
labels = algo.cluster(X,fig,ax[0])
# print(labels)
# print(len(labels))

clusters = {}
for i in range(len(labels)):
    if labels[i] not in clusters.keys():
        clusters[labels[i]] = []
    clusters[labels[i]].append(i)
num_clusters = len(clusters.keys())
# print(clusters)
msg = 'Clustering Algo: ' + algo.__name__ + '\n'
msg += 'Number of clusters: ' + str(num_clusters) + '\n'
msg += 'Number of Features: ' + str(X.shape[1])
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax[0].text(0, 0,msg, ha="center", va="center", size=10,
        bbox=bbox_props)
for i in range(num_clusters):
    ax[1].plot(days_to_death[clusters[i]])
# plt.show()
save_fig(algo.__name__ + '.py',fig)
