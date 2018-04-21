from lifelines import KaplanMeierFitter
from lifelines import AalenAdditiveFitter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from saveResults import COLORS

def survival_func(clusters,days_to_death,death_observed,ax):
    # Kaplan-Meier Fitter for getting survival function
    model = KaplanMeierFitter()
    num_clusters = len(clusters.keys())
    possible_grps = []
    for i in range(num_clusters):
        if len(clusters[i]) > 1 :
            label = 'cluster'+str(i+1) + '(' + str(len(clusters[i])) + ')'
            model.fit(days_to_death[clusters[i]], event_observed=death_observed[clusters[i]], label=label)
            model.survival_function_.plot(ax=ax,color=COLORS[i%len(COLORS)])

            # Survival function datapoints
            df = model.survival_function_
            x = np.array(df.index.tolist())
            y = np.array(df[label].tolist())

            less_indices = np.argwhere(y <= 0.5)
            more_indices = np.argwhere(y >= 0.5)

            days_half_prob = 0
            less = False
            more = False
            if less_indices.size > 0:
                print(x[less_indices[0,0]])
                if abs(y[less_indices[0,0]]-0.5) < 0.1:
                    days_half_prob += x[less_indices[0,0]]
                    less = True
            if more_indices.size > 0:
                print(x[more_indices[-1,-1]])
                if abs(y[more_indices[-1,-1]]-0.5) < 0.1:
                    days_half_prob += x[more_indices[-1,-1]]
                    more = True

            if less and more:
                possible_grps.append([i+1, days_half_prob/2])
            elif less or more:
                possible_grps.append([i+1, days_half_prob])

    ax.set_title('Survival function of clusters')
    xmin,xmax = ax.get_xlim()
    # Reference line corrosponding to 0.5 probability
    ax.axhline(y=0.5,linestyle='-',color='k',xmin=xmin,xmax=xmax)
    return possible_grps
