
import numpy as np
from keras.models import load_model

# import time

model = load_model('./weights/arcface_h5/arcface_model.h5', compile=False)

def Represent(image):
    
    img = image.astype('float32')
    img /= 255.0
    img = np.expand_dims(img, 0)
    
    # model.compile() # without compile, model from 0.22 -> 0.17s
    model.run_eagerly = True #eagerly make model fix loop and when recieve result faster | when it true model from 0.66 -> 0.22s

    embedding = model.predict(img)[0].tolist() #0.66 #this is the first embedding and work exactly the source code

    return embedding

