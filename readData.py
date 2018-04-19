import pandas as pd
from sklearn import preprocessing as pp
import numpy as np

def load_data():
	"""read data from csv file and preprocess"""
	gene_data = pd.read_csv('HiSeqV2.csv', header=None,sep="\t")
	patient_data = pd.read_csv('patient.csv', header=None,sep="\t")

	patient_ids1 = [x.lower() for x in patient_data.iloc[0]]
	patient_ids2 = [x.lower() for x in gene_data.iloc[0]]

	index = []
	for i in range(len(patient_ids2)):
		for j in range(len(patient_ids1)):
			if(patient_ids1[j] in patient_ids2[i]):
				index.append(j)
				break
	days_to_death = []
	death_observed = []
	total = 0
	count_observed = 0
	for x in index:

		# Death
		if(not pd.isnull(patient_data.iloc[4][x])):
			days = int(patient_data.iloc[4][x])
			days_to_death.append(days)
			death_observed.append(True)
			total += days
			count_observed += 1
		# Last Observed and Not Death
		elif(not pd.isnull(patient_data.iloc[5][x])):
			days = int(patient_data.iloc[5][x])
			days_to_death.append(days)
			death_observed.append(False)
			total += days
			count_observed += 1
		# Missing data
		else:
			days_to_death.append(np.nan)
			death_observed.append(False)

	# print(days_to_death)
	# print(death_observed)
	df = pd.DataFrame({'days_to_death': days_to_death},columns=['days_to_death'])
	imputer = pp.Imputer()
	days_to_death = imputer.fit_transform(df)[:,0]
	# print(days_to_death)
	gene_data.drop(gene_data.index[0], inplace=True)

	X = gene_data.iloc[:, 1:]
	X = np.array(X.T)
	return X.astype(float), np.array(days_to_death).astype(float), np.array(death_observed)

def laod_data_live():
	"""read data from csv file and preprocess"""
	patient_data = pd.read_csv('patient.csv', header=None,sep="\t")
	gene_data = pd.read_csv('HiSeqV2.csv', header=None,sep="\t")
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
		if(not pd.isnull(patient_data.iloc[4][x])):
			days_to_death.append(patient_data.iloc[4][x])
		elif(not pd.isnull(patient_data.iloc[5][x])):
			days_to_death.append(patient_data.iloc[5][x])
		else:
			days_to_death.append(0)
	# print(days_to_death)
if __name__ == '__main__':
	load_data()
