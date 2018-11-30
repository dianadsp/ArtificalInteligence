# coding=utf-8

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn.metrics

from sklearn import tree
from io import StringIO
from IPython.display import Image


#Después, indicamos en qué directorio vamos a trabajar. 
os.chdir("/home/oem/Desktop/ia/arbol")

#Cargamos el fichero de datos.
import tflearn.datasets.mnist as mnist
tar_train, tar_test, pred_train, pred_test = mnist.load_data(one_hot=True)



#Comprobamos el tamaño de las diferentes muestras (pred=predictora; tar=target, objetivo). La salida en cada caso es una pareja de datos: el tamaño de la muestra y el número de variables
pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

#Construimos el árbol con los datos de entrenamiento
classifier=DecisionTreeClassifier()
classifier=classifier.fit(pred_train,tar_train)

#Predecimos para los valores del grupo Test
predictions=classifier.predict(pred_test)

#Pedimos la matriz de confusión de las predicciones del grupo Test. La diagonal de esta matriz se lee: arriba a la izda True Negatives y abajo a la dcha True Positives. 
sklearn.metrics.confusion_matrix(tar_test,predictions)

#Sacamos el índice Accuracy Score, que resume la Matriz de Confusión y la cantidad de aciertos.
sklearn.metrics.accuracy_score(tar_test, predictions)

#Para dibujar el árbol hay que importar otra serie de cosas


#Pintamos el árbol
#out = StringIO()
#tree.export_graphviz(classifier, out_file=’treeMacarena.dot’)

