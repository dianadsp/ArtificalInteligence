# coding=utf-8
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
#from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor



#from sklearn.metrics import classification_report
from sklearn.metrics import classification_report
import sklearn.metrics
from sklearn.metrics import r2_score


os.chdir("/home/oem/Desktop/ia/arbol")

import tflearn.datasets.mnist as mnist
pred_train,tar_train, pred_test, tar_test = mnist.load_data(one_hot=True)

#import tflearn.datasets.mnist as mnist
#X, Y, testX, testY = mnist.load_data(one_hot=True)


pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

regressor=DecisionTreeRegressor()

regression=regressor.fit(pred_train,tar_train)

#Predecimos para los valores del grupo Test
predictions=regression.predict(pred_test)
#sklearn.metrics.confusion_matrix(tar_test,predictions)

#sklearn.metrics.accuracy_score(tar_test, predictions)
r2_score(tar_test, predictions)

from sklearn import tree
from io import StringIO
from IPython.display import Image

#Pintamos el árbol
out = StringIO()
tree.export_graphviz(regressor, out_file='treeMacarena.dot')



