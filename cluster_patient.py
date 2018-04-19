
import matplotlib.pyplot as plt
import textwrap as tw
from lifelines import KaplanMeierFitter

from readData import load_data
from saveResults import save_fig
from dim_reduction import reduce_dim
import kMeans, fuzzyCMeans, affinityPropagation

# Get only the numeric columns from games.
X, days_to_death, death_observed = load_data()
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
fig,ax = plt.subplots()
# clustering_algo[int(choice)].clustering_algo[int(choice)](X)
labels = algo.cluster(X,fig,ax)
# print(labels)
# print(len(labels))

clusters = {}
for i in range(len(labels)):
    if labels[i] not in clusters.keys():
        clusters[labels[i]] = []
    clusters[labels[i]].append(i)
num_clusters = len(clusters.keys())
# print(clusters)
msg = 'Clustering Algo: ' + algo.__name__ + ', \n'
msg += 'Number of clusters: ' + str(num_clusters) + ', \n'
msg += 'Number of Features: ' + str(X.shape[1])
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
fig_txt = tw.fill(tw.dedent(msg.rstrip() ), width=80)

# The YAxis value is -0.07 to push the text down slightly
plt.figtext(0.5, -0.07, fig_txt, horizontalalignment='center',
            fontsize=12, multialignment='left',
            bbox=dict(boxstyle="round", facecolor='#D8D8D8',
                      ec="0.5", pad=0.5, alpha=1), fontweight='bold')

# ax[0].text(0, 0,msg, ha="center", va="center", size=10,
#         bbox=bbox_props)
# ax[0].set_xlabel('something')
# ax[1].set_visible(False)
# for i in range(num_clusters):
#     ax[i+1].hist(days_to_death[clusters[i]], 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75, label='Smaple_Histogram')#, rwidth=0.25)
    # ax[1].plot(days_to_death[clusters[i]])

# plt.show()

save_fig(algo.__name__ + '.py',fig)

kmf = KaplanMeierFitter()
ax = ''
# print(len(days_to_death),len(death_observed))
# print(clusters[0])
# print(days_to_death[clusters[0]])
# print(death_observed[clusters[0]])

for i in range(num_clusters):
    if len(clusters[i]) :
        print(clusters[i])
        kmf.fit(days_to_death[clusters[i]], event_observed=death_observed[clusters[i]], label='KM_estimate for cluster:'+str(i))
        if i == 0:
            ax = kmf.survival_function_.plot()
        else:
            kmf.survival_function_.plot(ax=ax)
        print('Done for cluster ',i)
plt.title('Survival function of cluster');

plt.show()