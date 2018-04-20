from lifelines import KaplanMeierFitter
from lifelines import AalenAdditiveFitter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from saveResults import COLORS

def survival_func(clusters,days_to_death,death_observed,ax):
    model = KaplanMeierFitter()
    num_clusters = len(clusters.keys())
    possible_grps = []
    for i in range(num_clusters):
        print(type(clusters[i]))
        if len(clusters[i]) > 1 :
            print(clusters[i])
            label = 'cluster'+str(i+1) + '(' + str(len(clusters[i])) + ')'
            model.fit(days_to_death[clusters[i]], event_observed=death_observed[clusters[i]], label=label)
            model.survival_function_.plot(ax=ax,color=COLORS[i%len(COLORS)])
            print('Done for cluster ',i)

            df = model.survival_function_
            x = np.array(df.index.tolist())
            y = np.array(df[label].tolist())
            print(df)
            # print('Geater 0.5',np.argwhere(y >= 0.5)[-1][-1])
            # print('Lesser 0.5',np.argwhere(y <= 0.5)[0][0])

            less_indices = np.argwhere(y <= 0.5)
            more_indices = np.argwhere(y >= 0.5)

            days_half_prob = 0
            count = 0
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
            print(less,more)
            if less and more:
                possible_grps.append(days_half_prob/2)
            else:
                possible_grps.append(days_half_prob)


            # if less_indices.size > 0:
            #     days_half_prob += x[less_indices[0,0]]
            #     count += 1
            # if more_indices.size > 0:
            #     days_half_prob += x[more_indices[-1,-1]]
            #     count += 1
            # if count == 1:
            #     if less_indices.size >0:
            #         if abs(x[less_indices[0,0]]-0.5) < 0.05:
            #             days_half_prob /= count
            #             possible_grps.append(days_half_prob)
            #     else:
            #         if abs(x[more_indices[-1,-1]]-0.5) < 0.05:
            #             days_half_prob /= count
            #             possible_grps.append(days_half_prob)
            # elif count == 2:
            #     days_half_prob /= count
            #     possible_grps.append(days_half_prob)

            # print(days_half_prob)

            # print(np.interp(0.5, x, y))

    ax.set_title('Survival function of cluster')
    xmin,xmax = ax.get_xlim()
    ax.axhline(y=0.5,linestyle='-',color='k',xmin=xmin,xmax=xmax)
    return possible_grps

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
