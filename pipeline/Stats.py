import numpy as np
import pandas as pd


class Stats(object):


    #init to 0 for all attributes
    #TODO: implement magnitude fields and methods
    accX = pd.DataFrame()
    accY = pd.DataFrame()
    accZ = pd.DataFrame()
    accMag = pd.DataFrame()


    gyroX = pd.DataFrame()
    gyroY = pd.DataFrame()
    gyroZ = pd.DataFrame()
    gyroMag = pd.DataFrame()

    def __init__(self, filePath):
        self.df = pd.read_csv(filePath, header=0, index_col=0)

        self.statsDf = self.df.describe()

        self.accX = self.statsDf['ax']
        self.accY = self.statsDf['ay']
        self.accZ = self.statsDf['az']

        self.gyroX = self.statsDf['gx']
        self.gyroY = self.statsDf['gy']
        self.gyroZ = self.statsDf['gz']








