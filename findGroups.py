from scipy.stats import kde
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import operator

def get_grps1(possible_grps):
	x = np.array(possible_grps)
	density = kde.gaussian_kde(x) # x: list of price
	xgrid = np.linspace(x.min(), x.max(), x.size)
	plt.plot(xgrid, density(xgrid))
	# plt.show()

def get_grps(possible_grps):
	# survival_grp_diff = int(input("What should be the difference between two survival group:(int)"))
	survival_grp_diff = 250
	possible_grps = [(i,possible_grps[i]) for i in range(len(possible_grps))]
	possible_grps = sorted(possible_grps, key=operator.itemgetter(1))
	# print(possible_grps)
	init = possible_grps[0][1]
	clusters = [[possible_grps[0][0]]]
	for next in range(1,len(possible_grps)):
		if possible_grps[next][1] - init > survival_grp_diff:
			# New cluster
			clusters.append([possible_grps[next][0]])
		else:
			clusters[-1].append(possible_grps[next][0])
		init = possible_grps[next][1]
	print(clusters)
	print("*******")
	print('Number of Groups: ',len(clusters))
	print("*******")
	return clusters

if __name__ == '__main__':
	get_grps([])
