import pandas as pd
import tensorflow as tf
from sys import argv
import os

# Cargamos el modelo y los datos de prueba
modelo = tf.keras.models.load_model(argv[1])
testData = pd.read_csv(argv[2], quotechar='"')
with open('tokenizer_config.txt', 'r', encoding='utf-8') as f:
    tokenizer_config_loaded = f.read()
    tokenizer_config_dict = eval(tokenizer_config_loaded)
    tokenizer = tf.keras.preprocessing.text.Tokenizer.from_config(tokenizer_config_dict)

for index, row in testData.iterrows(): # iteramos sobre la tabla para hacer lo siguiente
    respuesta = modelo.predict(testData.at[index, 'preguntas']) # le pedimos, para cada pregunta, la respuesta al modelo
    testData.at[index, 'respuestas'] = respuesta # y guardamos cada respuesta en su fila correspondiente

# Y queda exportar la nueva tabla
os.makedirs("salidas")
testData.to_csv("salidas/test.csv", quotechar='"', lineterminator=",")
testData.to_html("salidas/test.html")
