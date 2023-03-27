import tensorflow as tf
from tensorflow import keras

# help libraries
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt', 'Trouser', 'Pulloover', 'Dress']

train_images = train_images/255.0
test_images = test_images/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(test_images, train_labels, epochs=15)
 
test_loss, test_acc = model.evaluate(test_labels, test_images)

print("Teste acc", test_loss)