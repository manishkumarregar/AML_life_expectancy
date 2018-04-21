from scipy.stats import kde
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import operator

# Find groups in a 1-d array based on proximity(survival_grp_diff)
# survival_grp_diff is fixed here, but it can be modified to be an input
# possible_grps contains (cluster_index, days the cluster patient can survive with 0.5 probability)
def get_grps(possible_grps):

	# survival_grp_diff = int(input("What should be the difference between two survival group:(int)"))
	survival_grp_diff = 250
	possible_grps = sorted(possible_grps, key=operator.itemgetter(1))
	init = possible_grps[0][1]

	# group contains array of grouped clusters
	groups = [[possible_grps[0][0]]]
	for next in range(1,len(possible_grps)):
		if possible_grps[next][1] - init > survival_grp_diff:
			# New cluster
			groups.append([possible_grps[next][0]])
		else:
			# Append to cluster on left side of the current point
			groups[-1].append(possible_grps[next][0])
		init = possible_grps[next][1]
	print("*******")
	print('Number of Groups: ',len(groups))
	print("*******")
	return groups

if __name__ == '__main__':
	get_grps([])
