import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from numpy.random import seed

#Define 100 como semente de randomização na inicialização de pesos
seed(100)
tf.random.set_seed(100)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[0]])

#Define rede neural com 2 entradas, 2 neurônios na camada oculta, 1 neurônio de saída
model = Sequential()
model.add(Dense(2, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

#Taxa de aprendizado é 0.1
sgd = SGD(lr=0.1)
model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

#Treinamento
model.fit(X, Y, batch_size=1, epochs=10000)

#Avaliação
_, accuracy = model.evaluate(X, Y)
print('Precisão: %.2f' % (accuracy*100))

print(model.predict_proba(X))
print(model.predict_classes(X))