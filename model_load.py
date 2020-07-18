import tensorflow as tf
import numpy as np
import tensorflow.keras as keras


#model = tf.keras.models.load_model("m1.h5")

def predict(image,model):
    image = image.reshape(-1,28,28,1)/255.
    prediction = model.predict([image])
    return int(prediction.argmax())