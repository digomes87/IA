import numpy as np


tensor_1d = np.array([1.3, 1, 4.0, 23.99])


print(f"Array Numpy {tensor_1d}")
print(f"Elmento do array Numpy 1-D no índice 0: {tensor_1d[0]}")
print(f"Elmento do array Numpy 1-D no índice 2: {tensor_1d[2]}")


# criando tensorFlow com Tensorflow
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


tf_tensor_1d = tf.convert_to_tensor(tensor_1d, dtype= tf.float64)

print(f"Tensor 1-D: {tf_tensor_1d}")
print(f"Elmento do Tensor 1-D no índice 0: {tf_tensor_1d[0]}")
print(f"Elmento do Tensor 1-D no índice 2: {tf_tensor_1d[2]}")
