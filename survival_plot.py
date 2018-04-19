from lifelines import KaplanMeierFitter
from lifelines import AalenAdditiveFitter
import matplotlib.pyplot as plt
import pandas as pd

from saveResults import COLORS

def survival_func(clusters,days_to_death,death_observed,ax):
    model = KaplanMeierFitter()
    num_clusters = len(clusters.keys())
    for i in range(num_clusters):
        print(type(clusters[i]))
        if len(clusters[i]) > 1 :
            print(clusters[i])
            model.fit(days_to_death[clusters[i]], event_observed=death_observed[clusters[i]], label='cluster:'+str(i+1) + '(' + str(len(clusters[i])) + ')')
            model.survival_function_.plot(ax=ax,color=COLORS[i%len(COLORS)])
            print('Done for cluster ',i)
    ax.set_title('Survival function of cluster');

def hazard_func(clusters,days_to_death,death_observed,ax):
    model = AalenAdditiveFitter(coef_penalizer=1.0, fit_intercept=True)
    num_clusters = len(clusters.keys())
    for i in range(num_clusters):
        # print(clusters[i])
        if len(clusters[i]) > 1 :
            X = {}
            X['days_to_death'] = days_to_death[clusters[i]]
            X['death_observed'] = death_observed[clusters[i]]
            X = pd.DataFrame(X)
            model.fit(X, 'days_to_death', event_col='death_observed')
            model.plot(ax=ax,color=COLORS[i%len(COLORS)])
            print('Done for cluster ',i)
    ax.set_title('Cumulatice hazard of cluster');
