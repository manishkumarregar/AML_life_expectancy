import os
from time import ctime
import matplotlib.pyplot as plot
def save_fig(algo,fig):
    foldername = algo.split('.')[0]
    foldername += '/'
    t = ctime()
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    DPI = fig.get_dpi()
    DefaultSize = fig.get_size_inches()
    fig.set_size_inches( (DefaultSize[0]*2, DefaultSize[1]*2) )
    fig.savefig(foldername + t + '.png',bbox_inches='tight')
