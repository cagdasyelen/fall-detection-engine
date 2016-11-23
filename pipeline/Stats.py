import numpy as np
import pandas as pd


class Stats(object):


    #init to 0 for all attributes
    accAvgX = 0
    accStdDevX = 0
    accMinX = 0
    accMaxX = 0
    accAvgY = 0
    accStdDevY = 0
    accMinY = 0
    accMaxY = 0
    accAvgZ = 0
    accStdDevZ = 0
    accMinZ = 0
    accMaxZ = 0

    accAvgMag = 0
    accStdDevMag = 0
    accMinMag = 0
    accMaxMag = 0


    gyroAvgX = 0
    gyroStdDevX = 0
    gyroMinX = 0
    gyroMaxX = 0
    gyroAvgY = 0
    gyroStdDevY = 0
    gyroMinY = 0
    gyroMaxY = 0
    gyroAvgZ = 0
    gyroStdDevZ = 0
    gyroMinZ = 0
    gyroMaxZ = 0

    gyroAvgMag = 0
    gyroStdDevMag = 0
    gyroMinMag = 0
    gyroMaxMag = 0

    def __init__(self, filePath):
        self.df = pd.read_csv(filePath, header=0, index_col=0)



