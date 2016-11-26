import numpy as np
import pandas as pd



'''

This class gets the raw data and extracts 
the features prior to the classification stage

Features to be extracted from raw data:

	-Magnitude of acc
	-Magnitude of gyro

'''

class FeatureExtraction:

	def __init__(self, fileDir):
		self.rawDataFile = fileDir
		self.rawDf = pd.read_csv(fileDir, header=0, index_col=0)

		#Adding mag of acc and gyro to pandas frame

		self.rawDf["aMag"] = ( self.rawDf["ax"]**2 + self.rawDf["ay"]**2 + self.rawDf["az"]**2 )**(0.5)
		self.rawDf["gMag"] = ( self.rawDf["gx"]**2 + self.rawDf["gy"]**2 + self.rawDf["gz"]**2 )**(0.5)

		
	def getAccMag(self):
		return self.rawDf["aMag"]


	def getGyroMag(self):
		return self.rawDf["gMag"]








f = FeatureExtraction("../raw-data/sample23_fall0.csv")








