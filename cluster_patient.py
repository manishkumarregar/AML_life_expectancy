
import matplotlib.pyplot as plt
import textwrap as tw
import numpy as np

from readData import load_data
from saveResults import save_fig
from dim_reduction import reduce_dim
import kMeans, fuzzyCMeans, affinityPropagation, hirarAgglomerative
from survival_plot import survival_func,hazard_func
from findGroups import get_grps


# Get only the numeric columns from games.
X, days_to_death, death_observed = load_data()
choice = int(input('Want to reduce dimension(0/1):'))
if choice == 1:
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

# hazard_func(clusters,days_to_death,death_observed,ax[1])
fig2, ax2 = plt.subplots()
possible_grps = survival_func(clusters,days_to_death,death_observed,ax2)
survival_grp = get_grps(possible_grps)
actual_grp = len(survival_grp)
useful = ''
if actual_grp > 2:
    useful = 'Good/'
# plt.hist(possible_grps, 200, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)#, rwidth=0.25)

# x = possible_grps# [1,1,5,6,1,5,10,22,23,23,50,51,51,52,100,112,130,500,512,600,12000,12230]

# Y = np.array(list(zip(x,np.zeros(len(x)))), dtype=np.int)
# clu, num = affinityPropagation.cluster(Y,fig,ax[2])
# print(clu, num)


msg = 'Clustering Algo: ' + algo.__name__ + ', \n'
msg += 'Number of Clusters: ' + str(num_clusters) + ', \n'
msg += 'Number of Features: ' + str(X.shape[1]) + ' \n'
msg += 'Number of Groups: ' + str(survival_grp)

# for i in range(num_clusters):
    # msg += 'Cluster ' + str(i) + 'contains ' + str(len(clusters[i])) + 'patients\n'
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
fig_txt = tw.fill(tw.dedent(msg.rstrip() ), width=80)

# The YAxis value is -0.07 to push the text down slightly
plt.figtext(0.5, -0.07, fig_txt, horizontalalignment='center',
            multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
                      ec="0.5", pad=0.5, alpha=1), fontweight='bold')

if actual_grp > 2:
    save_fig(useful + algo.__name__ + '.py',fig2)
# plt.show()
save_fig(algo.__name__ + '.py',fig2)
