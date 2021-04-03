# Import Statements
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy



# Building Neural Network Using Sequential Model


# Creating the Layers to be used in the sequential
firstlayer = Dense(units=4, input_shape=(1,), activation='relu')
secondlayer = Dense(units=8, activation='relu')
outputlayer = Dense(units=2, activation='softmax')

# The outputlayer has only two units, one for counterfeit and the other for real currency.

# Create the Sequential Model Here, put the layers in correct order of left to right
model = Sequential([firstlayer, secondlayer, outputlayer])

# Check the model is created
model.summary()

if __name__ == '__main__':
    print("Beans")
