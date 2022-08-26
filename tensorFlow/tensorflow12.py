import numpy as np


tensor_1d = np.array([(1,2,3,4,5),(12,34,5,5,23),(123,3434,231,23452)])


print(f"Array Numpy {tensor_1d}")
print(f"Elmento do array Numpy 1-D no índice [3][3]: {tensor_1d[3][3]}")
print(f"Elmento do array Numpy 1-D no índice [0:2][0:2]: {tensor_1d[0:2, 0:3]}")


# criando tensorFlow com Tensorflow
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


tf_tensor_1d = tf.convert_to_tensor(tensor_1d, dtype= tf.float64)

print(f"Tensor 1-D: {tf_tensor_1d}")
print(f"Elmento do Tensor 1-D no índice 0: {tf_tensor_1d[0]}")
print(f"Elmento do Tensor 1-D no índice 2: {tf_tensor_1d[2]}")
