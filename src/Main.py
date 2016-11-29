from Engine import Engine


e  = Engine()
e.createSamples('temp.csv')
e.predict('../saved-objects/clf.pkl')