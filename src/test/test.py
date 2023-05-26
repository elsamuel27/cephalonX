import pandas as pd
import tensorflow as tf
from sys import argv

# Cargamos el modelo y los datos de prueba
modelo = tf.keras.models.load_model(argv[1])
testData = pd.read_csv(argv[2], quotechar='"')
with open('tokenizer_config.txt', 'r', encoding='utf-8') as f:
    tokenizer_config_loaded = f.read()
    tokenizer_config_dict = eval(tokenizer_config_loaded)
    tokenizer = tf.keras.preprocessing.text.Tokenizer.from_config(tokenizer_config_dict)

# Le añadimos a la tabla una columna para las respuestas
testData["respuestas"] = ""
for index, row in testData.iterrows():
    respuesta = modelo.predict(row['preguntas']) # iteramos sobre las preguntas para pedirle cada una al modelo
    testData.at[index, 'respuestas'] = respuesta # y obviamente las guardamos cada una en su fila correspondiente

# Y queda exportar la nueva tabla
testData.to_csv(quotechar='"', lineterminator=",")