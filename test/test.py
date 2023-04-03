import pandas as pd
import tensorflow as tf
from sys import argv

modelo = tf.keras.models.load_model(argv[1])

testData = pd.read_csv(argv[2], delimiter=",", quotechar='"')