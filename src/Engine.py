import pandas as pd
import numpy as np


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



		
		self.samples = self.samples.reshape(7,10)






