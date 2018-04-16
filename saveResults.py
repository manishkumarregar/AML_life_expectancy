import os
from time import ctime
import matplotlib.pyplot as plot
def save_fig(algo,fig):
    foldername = algo.split('.')[0]
    foldername += '/'
    t = ctime()
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    fig.savefig(foldername + t + '.png',bbox_inches='tight')
