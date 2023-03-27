import numpy as np
from IPython.display import Image



def signal(x):
    return 1/(1+ np.exp(-x))

image(url = 'sigmoid-formula.png')

inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

outpu = sigmoid([np.dot(weightsm, inputs)]+ bias)

print(outpu)

