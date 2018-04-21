import numpy as np
from sklearn.decomposition import NMF
from readData import load_data
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import operator


def reduce_dim(X):

	# Control for selecting genes based on variance of genes accross patients
	var_elemination = int(input('Apply variance based elemination on gene data:(0/1)'))
	reduced_X = X
	if var_elemination == 1:
		num_features = int(input('Enter the number of genes to retain:'))
		variances = np.var(X,axis=0)
		variances = [(i,var) for i,var in enumerate(variances)]

		# Soring genes based on variance
		variances = sorted(variances, key=operator.itemgetter(1), reverse=True)
		# Indices of 'num_features' of genes with highest variance
		useful_genes = [variances[i][0] for i in range(num_features)]
		reduced_X = X[:,useful_genes]

	# Control for generating mega-genes using non-negative matrix factorization
	nmf = int(input('Apply NMF on remaing gene data:(0/1)'))
	if nmf == 1:
		num_features = int(input('Enter new dimension for remaining gene data:'))
		model = NMF(n_components=num_features, init='random', random_state=0)
		reduced_X = model.fit_transform(X)
	return reduced_X

# Reducing data to lower dimension for plotting
def plotable(X):
	plot_columns = X
	if X.shape[1] > 2:
		# Create a PCA model.
		pca_2 = PCA(2)
		# Fit the PCA model on the numeric columns from earlier.
		plot_columns = pca_2.fit_transform(X)
	return plot_columns

# For testing purpose
if __name__ == '__main__':
	X, days_to_death, death_observed = load_data()
	reduce_dim(X)
