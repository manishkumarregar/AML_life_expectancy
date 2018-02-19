from pandas import read_csv
from sklearn import preprocessing as pp
import numpy as np

def load_data():
	"""read data from csv file and preprocess"""
	dataset = read_csv('HiSeqV2.csv', header=None,sep="\t")
	dataset.drop(dataset.index[0], inplace=True)

	X = dataset.iloc[:, 1:]
	return np.array(X.T)


load_data()