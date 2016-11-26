import numpy as np
import pandas as pd



'''

This class gets the raw data and extracts 
the features prior to the classification stage

Features to be extracted from raw data:

	-min(aMag)
	-max(aMag)
	-mean(aMag)
	-std(aMag)
	-min(gMag)
	-max(gMag)
	-mean(gMag)
	-std(gMag)


'''

class FeatureExtraction:

	def __init__(self, fileDir):
		self.rawDataFile = fileDir
		self.rawDf = pd.read_csv(fileDir, header=0, index_col=0)

		#Adding mag of acc and gyro to pandas frame
		self.rawDf["aMag"] = ( self.rawDf["ax"]**2 + self.rawDf["ay"]**2 + self.rawDf["az"]**2 )**(0.5)
		self.rawDf["gMag"] = ( self.rawDf["gx"]**2 + self.rawDf["gy"]**2 + self.rawDf["gz"]**2 )**(0.5)

		#calculate basic stats once and use later
		self.stats = self.rawDf.describe()

		#features init
		self.features = {}


		#put the label for different severity levels based on the filename
		if(fileDir[len(fileDir) - 5] == "1"):
			self.label = 1
		elif(fileDir[len(fileDir) - 5] == "2"):
			self.label = 2
		elif(fileDir[len(fileDir) - 5] == "3"):
			self.label = 3
		else:
			self.label = 0

		



	def addFeatures(self,addMin,addMax,addAvg,addStd):

		if(addMin == True):
			self.features['aMin'] = self.stats["aMag"]["min"]
			self.features['gMin'] = self.stats["gMag"]["min"]

		if(addMax == True):
			self.features['aMax'] = self.stats["aMag"]["max"]
			self.features['gMax'] = self.stats["gMag"]["max"]

		if(addAvg == True):
			self.features['aAvg'] = self.stats["aMag"]["mean"]
			self.features['gAvg'] = self.stats["gMag"]["mean"]

		if(addStd == True):
			self.features['aStd'] = self.stats["aMag"]["std"]
			self.features['gStd'] = self.stats["gMag"]["std"]


		print(self.features)
	


		
	def getAccMag(self):
		return self.rawDf["aMag"]


	def getGyroMag(self):
		return self.rawDf["gMag"]










f = FeatureExtraction("../raw-data/sample32_fall0.csv")
f.addFeatures(True, True, True, True)








