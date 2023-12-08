import tensorflow as tf

from Helper import *

def modelator(rinput):
    return result

def modelrunner(rinput):
    model = tf.keras.models.load_model()
    data = modelator(rinput)
    result = model.predict(data)
    return result