import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import cross_val_score
from sklearn import tree
import pickle





class Model:

	def __init__(self):
		self.load_data()
		#self.clf = GradientBoostingClassifier(n_estimators=10)
		self.clf = DecisionTreeClassifier(criterion="entropy")
		self.train()
		self.predict()
		print(self.get_training_accuracy())
		print(self.get_cv_accuracy())



	def load_data(self):
		train_csv = '../train/train.csv'
		test_csv = '../test/test.csv'
		self.df_train = pd.read_csv(train_csv, header=0)
		self.df_test = pd.read_csv(test_csv, header=0)
		arr_train = self.df_train.values
		arr_test = self.df_test.values
		self.train_X = arr_train[0::,:-1]
		#self.train_X = normalize(self.train_X, axis=1, norm='l2')
		self.train_Y = arr_train[0::, -1]
		self.test_X = arr_test[0::, :-1]
		#self.test_X = normalize(self.test_X, axis=1, norm='l2')
		self.test_ID = arr_test[0::,-1]


	def train(self):
		self.clf.fit(self.train_X, self.train_Y)

	def predict(self):
		self.test_Y = self.clf.predict(self.test_X)

	def get_training_accuracy(self):
		return (self.clf.score(self.train_X, self.train_Y))

	def get_cv_accuracy(self):
		return cross_val_score(self.clf, self.train_X, self.train_Y, cv=10)



m = Model()
feature_names = list(m.df_train.columns.values)
feature_names.remove('label')



print("labels:")
print(m.test_ID)

print("prediction:")
print(m.test_Y)

tree.export_graphviz(m.clf, out_file='/tmp/tree_clf.dot')







