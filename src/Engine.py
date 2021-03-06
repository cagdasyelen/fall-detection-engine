import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import time
import os
'''

This class creates the samples(ml inputs) from the file which contains raw sensor data
by looking at a snapshop every 0.5 sec interval (jumping 5 samples)

'''

class Engine:

	def __init__(self):
		self.samples = []
		self.samples = np.array(self.samples)


	def createFeatures(self, arr):

		aMag = np.sqrt(arr[0::,0]*arr[0::,0] + arr[0::,1]*arr[0::,1] + arr[0::,2]*arr[0::,2])
		gMag = np.sqrt(arr[0::,3]*arr[0::,3] + arr[0::,4]*arr[0::,4] + arr[0::,5]*arr[0::,5])
		

		#magArr = np.transpose(np.matrix([aMag, gMag])) 

		features = {}
		features['aMin'] = np.min(aMag)
		features['gMin'] = np.min(gMag)
		features['aMax'] = np.max(aMag)
		features['gMax'] = np.max(gMag)
		features['aAvg'] = np.mean(aMag)
		features['gAvg'] = np.mean(gMag)
		features['aStd'] = np.std(aMag)
		features['gStd'] = np.std(gMag)
		features['aP2P'] = np.max(aMag) - np.min(aMag)
		features['gP2P'] = np.max(gMag) - np.min(gMag)


		npArr = np.array(sorted(features.items()))

		self.samples = np.append(self.samples, npArr[0::,1].astype(float), axis = 0)



	def createSamples(self, fileName):
		if (not os.path.isfile('data.csv')):
			return False 
		self.rawData = pd.read_csv(fileName, header=0, index_col=0)
		self.rawArr = self.rawData.values

		self.numOfRows = self.rawArr.shape[0]

		n = int((self.numOfRows - 30)/5) + 2
		cnt = 0



		while cnt < n:
			if(cnt == n -1 ):
				self.createFeatures(self.rawArr[5*cnt:self.numOfRows, 0::])
			else:
				self.createFeatures(self.rawArr[5*cnt:(5*cnt+30), 0::])
			cnt=cnt + 1



		
		self.samples = self.samples.reshape(n,10)
		return True
	
	def predict(self, clfFile):
		with open(clfFile, 'rb') as input:
			self.clf = pickle.load(input)

		return self.clf.predict(self.samples)


while(1):
	e  = Engine()
	isFile=e.createSamples('data.csv')
	if(isFile):
		print("File found!")
		results = e.predict('clf.pkl')
		os.system("rm -rf data.csv")
		with open('severity.txt', 'w+') as file:
			file.write(str(int(max(results))))
			file.write("\nSensorTag2650");
	time.sleep(3)
	






