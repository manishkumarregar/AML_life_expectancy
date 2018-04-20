
import matplotlib.pyplot as plt
import textwrap as tw

from readData import load_data
from saveResults import save_fig
from dim_reduction import reduce_dim
import kMeans, fuzzyCMeans, affinityPropagation, hirarAgglomerative
from survival_plot import survival_func,hazard_func

# Get only the numeric columns from games.
X, days_to_death, death_observed = load_data()
choice = input('Want to reduce dimension(yes/no):')
if choice == 'yes':
    X = reduce_dim(X)

clustering_algo = {
    1 : kMeans,
    2 : fuzzyCMeans,
    3 : affinityPropagation,
    4 : hirarAgglomerative
}

choice = input("Choose the clustering algo:")
algo = clustering_algo[int(choice)]
fig,ax = plt.subplots(2)

labels, num_clusters = algo.cluster(X,fig,ax[0])

clusters = {}
for i in range(num_clusters):
    clusters[i] = []
for i in range(len(labels)):
    clusters[labels[i]].append(i)

msg = 'Clustering Algo: ' + algo.__name__ + ', \n'
msg += 'Number of clusters: ' + str(num_clusters) + ', \n'
msg += 'Number of Features: ' + str(X.shape[1])
# for i in range(num_clusters):
    # msg += 'Cluster ' + str(i) + 'contains ' + str(len(clusters[i])) + 'patients\n'
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
fig_txt = tw.fill(tw.dedent(msg.rstrip() ), width=80)

# The YAxis value is -0.07 to push the text down slightly
plt.figtext(0.5, -0.07, fig_txt, horizontalalignment='center',
            fontsize=12, multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
                      ec="0.5", pad=0.5, alpha=1), fontweight='bold')


# hazard_func(clusters,days_to_death,death_observed,ax[1])
survival_func(clusters,days_to_death,death_observed,ax[1])
save_fig(algo.__name__ + '.py',fig)
