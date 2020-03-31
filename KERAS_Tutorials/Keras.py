from numpy import genfromtxt
import numpy
import keras
from keras.models import Sequential
from keras.layers import Dense
import sklearn


# load the dataset

dataset = genfromtxt('C:\\Development_Projects\\GIS_Machine_Learning\\GIS_Machine_Learning\\KERAS_Tutorials\\pima.csv', delimiter=',')
scale = sklearn.preprocessing.MinMaxScaler(feature_range= (0,1))


X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10, verbose=0)
# make class predictions with the model
predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))