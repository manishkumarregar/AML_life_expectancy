from pandas import read_csv
from pandas import isnull, to_numeric
from sklearn import preprocessing as pp
import numpy as np

def load_data():
	"""read data from csv file and preprocess"""
	gene_data = read_csv('HiSeqV2.csv', header=None,sep="\t")
	patient_data = read_csv('patient.csv', header=None,sep="\t")

	patient_ids1 = [x.lower() for x in patient_data.iloc[0]]
	patient_ids2 = [x.lower() for x in gene_data.iloc[0]]

	index = []
	for i in range(len(patient_ids2)):
		for j in range(len(patient_ids1)):
			if(patient_ids1[j] in patient_ids2[i]):
				index.append(j)
				break
	days_to_death = []
	for x in index:
		if(not isnull(patient_data.iloc[4][x])):
			days_to_death.append(patient_data.iloc[4][x])
		elif(not isnull(patient_data.iloc[5][x])):
			days_to_death.append(patient_data.iloc[5][x])
		else:
			days_to_death.append(0)

	gene_data.drop(gene_data.index[0], inplace=True)

	X = gene_data.iloc[:, 1:]
	X = np.array(X.T)
	return X.astype(float), np.array(days_to_death).astype(float)

def laod_data_live():
	"""read data from csv file and preprocess"""
	patient_data = read_csv('patient.csv', header=None,sep="\t")
	gene_data = read_csv('HiSeqV2.csv', header=None,sep="\t")
	patient_ids1 = [x.lower() for x in patient_data.iloc[0]]
	patient_ids2 = [x.lower() for x in gene_data.iloc[0]]

	index = []
	for i in range(len(patient_ids2)):
		for j in range(len(patient_ids1)):
			if(patient_ids1[j] in patient_ids2[i]):
				index.append(j)
				break
	days_to_death = []
	for x in index:
		if(not isnull(patient_data.iloc[4][x])):
			days_to_death.append(patient_data.iloc[4][x])
		elif(not isnull(patient_data.iloc[5][x])):
			days_to_death.append(patient_data.iloc[5][x])
		else:
			days_to_death.append(0)
	# print(days_to_death)
laod_data_live()
