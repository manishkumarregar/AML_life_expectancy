import pandas as pd
from sklearn import preprocessing as pp
import numpy as np

def load_data():
	"""read data from csv file and preprocess"""
	# Reading gene profiles of patient
	gene_data = pd.read_csv('HiSeqV2.csv', header=None,sep="\t")
	# Reading survival profiles of patient
	patient_data = pd.read_csv('patient.csv', header=None,sep="\t")

	# patient ids in gene profile data
	patient_ids1 = [x.lower() for x in patient_data.iloc[0]]
	# patient ids in survival profile data
	patient_ids2 = [x.lower() for x in gene_data.iloc[0]]

	# Mapping for patient ids betwwen gene profile data and survival profile data
	index = []
	for i in range(len(patient_ids2)):
		for j in range(len(patient_ids1)):
			if(patient_ids1[j] in patient_ids2[i]):
				index.append(j)
				break

	# Survival data for patients
	days_to_death = []
	# death_observed is boolean array with True -> patient died, False -> patient's last follow up
	death_observed = []
	for x in index:

		# Death
		if(not pd.isnull(patient_data.iloc[4][x])):
			days = int(patient_data.iloc[4][x])
			days_to_death.append(days)
			death_observed.append(True)
		# Last Observed and Not Death
		elif(not pd.isnull(patient_data.iloc[5][x])):
			days = int(patient_data.iloc[5][x])
			days_to_death.append(days)
			death_observed.append(False)
		# Missing data
		else:
			days_to_death.append(np.nan)
			death_observed.append(False)

	# Missing data handlling for survival data of patient
	df = pd.DataFrame({'days_to_death': days_to_death},columns=['days_to_death'])
	imputer = pp.Imputer()
	days_to_death = imputer.fit_transform(df)[:,0]

	gene_data.drop(gene_data.index[0], inplace=True)
	X = gene_data.iloc[:, 1:]
	X = np.array(X.T)
	return X.astype(float), np.array(days_to_death).astype(float), np.array(death_observed)

# For testing
if __name__ == '__main__':
	load_data()
