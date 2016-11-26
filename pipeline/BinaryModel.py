import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB


class Model:

	def __init__(self):
		self.load_data()
		self.clf = GaussianNB()
		self.train()
		self.predict()
		print(self.get_training_accuracy())


	def load_data(self):
		train_csv = '../train/binaryClassificationTrain.csv'
		test_csv = '../test/binaryClassificationTest.csv'
		df_train = pd.read_csv(train_csv, header=0)
		df_test = pd.read_csv(test_csv, header=0)
		arr_train = df_train.values
		arr_test = df_test.values
		self.train_X = arr_train[0::,:-1]
		self.train_Y = arr_train[0::, -1]
		self.test_X = arr_test[0::, :-1]
		self.test_ID = arr_test[0::,-1]


	def train(self):
		self.clf.fit(self.train_X, self.train_Y)

	def predict(self):
		self.test_Y = self.clf.predict(self.test_X)

	def get_training_accuracy(self):
		return (self.clf.score(self.train_X, self.train_Y))




m = Model()


print("labels:")
print(m.test_ID)

print("prediction:")
print(m.test_Y)







