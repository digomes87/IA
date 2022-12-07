from re import S
import pandas
import numpy as np
from tensorflow import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD


# como o dataset nao possui header, vamos incluir
dados = pandas.read_csv("wine.data", names=["Class", "Alcohol", "Malic Alic", "Ash", "Alcanility of Ash", "Magnerium",
                                            "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
                                            "Color intensity", "Hue", "Proline"])

# obtendo os valos de classe e amazennando em value_class
value_class = dados["Class"].values

print(value_class)

#ajustando o formato de value_class
value_class_train = np_utils.to_categorical(value_class)
print(value_class_train)


# keras espera receber as classes em diferentes colunas. Como temos 3 classes, precisamos de 3 colunas
value_class_train = value_class_train[:, 1:4]

print(value_class_train)

del(dados["Class"])
dados = dados.values


model = Sequential()

model.add(Dense(40, input_dim = 13, kernel_initializer='normal', activation='relu'))
model.add(Dense(10, kernel_initializer='normal', activation='sigmoid'))
model.add(Dropout(0.10))
model.add(Dense(5, kernel_initializer='normal', activation='softmax'))


opt = keras.optimizers.Adam(
    lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['acc'])
model.fit(dados, value_class_train, epochs=1600, verbose=1)
score = model.evaluate(dados, value_class_train , verbose=0)
print(score)