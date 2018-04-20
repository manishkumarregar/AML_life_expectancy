import os
from time import ctime
import matplotlib.pyplot as plot
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch

COLORS = ['crimson', 'indigo', 'chartreuse', 'olive', 'aqua',
        'orangered', 'blue', 'tan', 'silver', 'gold', 'goldenrod',
        'violet', 'maroon', 'brown', 'magenta', 'fuchsia', 'black',
        'coral', 'salmon', 'yellow', 'cyan', 'darkblue', 'orchid',
        'darkgreen', 'lightblue', 'tomato', 'purple', 'navy', 'ivory',
        'white', 'orange', 'khaki', 'lavender', 'aquamarine', 'red',
        'green', 'lime', 'lightgreen', 'grey', 'wheat', 'turquoise',
        'beige', 'chocolate', 'yellowgreen', 'sienna', 'plum', 'teal']

scatter = False
# COLORS = ['b', 'g', 'r', 'c', 'm', y', 'k', '']
def save_fig(algo,fig):
    foldername = algo.split('.')[0]
    foldername += '/'
    t = ctime()
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    DPI = fig.get_dpi()
    DefaultSize = fig.get_size_inches()
    fig.set_size_inches( (DefaultSize[0]*2, DefaultSize[1]*2) )
    # fig.set_size_inches( (3.448819, 2.614173) )

    fig.savefig(foldername + t + '.png',bbox_inches='tight')

def plot1(num_clusters,labels,X,centers,ax):
    # scatter = int(input("Want to join cluster center and it's members(0/1):"))
    for k, col in zip(range(num_clusters), COLORS):
        class_members = labels == k
        ax.plot(X[class_members, 0], X[class_members, 1], '.', color=col)
        if centers is not None:
            cluster_center = centers[k]
            ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
            if scatter:
                for x in X[class_members]:
                    ax.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
