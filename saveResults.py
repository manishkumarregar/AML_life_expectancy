import os
from time import ctime
import matplotlib.pyplot as plot
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch

COLORS = ['crimson', 'indigo', 'pink', 'chartreuse', 'olive', 'aqua',
        'orangered', 'blue', 'tan', 'silver', 'gold', 'goldenrod',
        'violet', 'maroon', 'brown', 'magenta', 'fuchsia', 'black',
        'coral', 'salmon', 'yellow', 'cyan', 'darkblue', 'orchid',
        'darkgreen', 'lightblue', 'tomato', 'purple', 'navy', 'ivory',
        'white', 'orange', 'khaki', 'lavender', 'aquamarine', 'red',
        'green', 'lime', 'lightgreen', 'grey', 'wheat', 'turquoise',
        'beige', 'chocolate', 'yellowgreen', 'sienna', 'plum', 'teal']
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
    fig.savefig(foldername + t + '.png',bbox_inches='tight')
