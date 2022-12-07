from pyexpat import model
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD
from keras.utils import np_utils

model = Sequential()

model.add(Dense(40, input_dim = 13, kernel_initializer='normal', activation='relu'))
model.add(Dense(10, kernel_initializer='normal', activation='sigmoid'))
model.add(Dropout(0.10))
model.add(Dense(5, kernel_initializer='normal', activation='softmax'))


opt = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon= le-08, decay=0.0)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['acc'])
model.fit(dados, y, epochs=1600, verbose=1)
score = model.evaluate(dados, y , verbose=0)
print(score)