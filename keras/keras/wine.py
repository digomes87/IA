from re import S
import pandas
import numpy as np
from keras.utils import np_utils

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