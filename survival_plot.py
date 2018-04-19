from lifelines import KaplanMeierFitter
from lifelines import AalenAdditiveFitter
import matplotlib.pyplot as plt
import pandas as pd

def survival_func(clusters,days_to_death,death_observed):
    model = KaplanMeierFitter()
    ax = ''
    # print(len(days_to_death),len(death_observed))
    # print(clusters[0])
    # print(days_to_death[clusters[0]])
    # print(death_observed[clusters[0]])
    num_clusters = len(clusters.keys())
    for i in range(num_clusters):
        if len(clusters[i]) :
            print(clusters[i])
            model.fit(days_to_death[clusters[i]], event_observed=death_observed[clusters[i]], label='KM_estimate for cluster:'+str(i))
            if i == 0:
                ax = model.survival_function_.plot()
            else:
                model.survival_function_.plot(ax=ax)
            print('Done for cluster ',i)
    plt.title('Survival function of cluster');

    plt.show()

def hazard_func(clusters,days_to_death,death_observed):
    model = AalenAdditiveFitter(coef_penalizer=1.0, fit_intercept=True)
    ax = ''
    # print(len(days_to_death),len(death_observed))
    # print(clusters[0])
    # print(days_to_death[clusters[0]])
    # print(death_observed[clusters[0]])
    num_clusters = len(clusters.keys())
    for i in range(num_clusters):
        if len(clusters[i]) :
            X = {}
            X['days_to_death'] = days_to_death[clusters[i]]
            X['death_observed'] = death_observed[clusters[i]]
            X = pd.DataFrame(X)
            model.fit(X, 'days_to_death', event_col='death_observed')
            if i == 0:
                ax = model.plot()
            else:
                model.plot(ax=ax)
            print('Done for cluster ',i)
    plt.title('Cumulatice hazard of cluster');

    plt.show()
