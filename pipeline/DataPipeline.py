import numpy as np
import pandas as pd
import csv



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
	-p2p(aMag)
	-p2p(gMag)


'''

class FeatureExtraction:

	def __init__(self, fileDir):
		self.rawDataFile = fileDir
		print(fileDir)
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

		



	def addFeatures(self):

		self.features['aMin'] = self.stats["aMag"]["min"]
		self.features['gMin'] = self.stats["gMag"]["min"]

		self.features['aMax'] = self.stats["aMag"]["max"]
		self.features['gMax'] = self.stats["gMag"]["max"]

		self.features['aAvg'] = self.stats["aMag"]["mean"]
		self.features['gAvg'] = self.stats["gMag"]["mean"]

		self.features['aStd'] = self.stats["aMag"]["std"]
		self.features['gStd'] = self.stats["gMag"]["std"]

		self.features['aP2P'] = self.stats["aMag"]["max"] - self.stats["aMag"]["min"]
		self.features['gP2P'] = self.stats["gMag"]["max"] - self.stats["gMag"]["min"]

		self.features['label'] = self.label




	def writeToFile(self, fileToWrite):

		with open(fileToWrite, 'r+',encoding="utf8") as f:
			header = next(csv.reader(f))
			dict_writer = csv.DictWriter(f, header, -999)
			dict_writer.writerow(self.features)






