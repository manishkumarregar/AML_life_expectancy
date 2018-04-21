
import matplotlib.pyplot as plt
import textwrap as tw
import numpy as np
from time import ctime

from readData import load_data
from saveResults import save_fig
from dim_reduction import reduce_dim
import kMeans, fuzzyCMeans, affinityPropagation, hirarAgglomerative, miniBatchkMeans
from survival_plot import survival_func
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
    4 : hirarAgglomerative,
    5 : miniBatchkMeans
}

choice = input("Choose the clustering algo:")
algo = clustering_algo[int(choice)]
fig,ax = plt.subplots()

# Clustering patients
labels, num_clusters = algo.cluster(X,fig,ax)

if num_clusters > 40:
    print("Number of clusters are very high.")
    exit()

# Separating indices of patients based on their cluster index
clusters = {}
for i in range(num_clusters):
    clusters[i] = []
for i in range(len(labels)):
    clusters[labels[i]].append(i)

fig2, ax2 = plt.subplots()

# Find possible survival groups (all clusters are different survival group)
possible_grps = survival_func(clusters,days_to_death,death_observed,ax2)

# Refine possible survival groups by combining clusters with similar
# days to survive with 0.5 probability
survival_grp = get_grps(possible_grps)

actual_grp = len(survival_grp)
useful = ''
if actual_grp > 2:
    useful = 'Good/'

# Information about current experiment
msg = 'Clustering Algo: ' + algo.__name__ + ', \n'
msg += 'Number of Clusters: ' + str(num_clusters) + ', \n'
msg += 'Number of Features: ' + str(X.shape[1]) + ' \n'
msg += 'Number of Groups: ' + str(survival_grp)

bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
fig_txt = tw.fill(tw.dedent(msg.rstrip() ), width=80)

plt.figtext(0.5, -0.07, fig_txt, horizontalalignment='center',
            multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
            ec="0.5", pad=0.5, alpha=1), fontweight='bold')

t = ctime()
save_fig(algo.__name__ + 'clusters.py',fig,t)

if actual_grp > 2:
    save_fig(useful + algo.__name__ + '.py',fig2,t)
