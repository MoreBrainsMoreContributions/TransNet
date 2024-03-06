import tensorflow as tf
print(tf.test.is_built_with_cuda())

import tensorflow as tf
print(tf.compat.v1.config.experimental.list_physical_devices('GPU'))