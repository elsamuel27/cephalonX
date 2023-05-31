Ya que el modelo se está entrenando aquí mismo y tenemos acceso a sus archivos, ergo, podemos cargarlo en un script de Python y pedirle hacer predicciones, podemos exprimir precisamente eso para agilizar mucho el proceso de probarlo "manualmente". Está hecho de la siguiente manera
- Guardamos preguntas para hacerle en un archivo CSV. Ésto nos permite escribir preguntas nuevas o quitar otras sin tocar nada dentro del código
- Hacemos un script en Python que carga todo ésto:
    - Las preguntas del CSV
    - El modelo ya entrenado
    - Su tokenizador correspondiente
- Las preguntas en éstos momentos están en un DataFrame de Pandas (o tabla) con 2 columnas;
    - "preguntas", que tiene las preguntas que apuntamos anteriormente
    - "respuestas", que está vacía
- Iteramos sobre la tabla, realizando el siguiente procedimiento para cada fila de la tabla:
    - Procesamos la pregunta con el tokenizador
    - Le pedimos al modelo que responda a la pregunta
    - Procesamos su respuesta
    - La guardamos en la misma fila, en la columna para las respuestas
- Exportamos la tabla y vemos sus respuestas

Qué puedo decir, le he pillado el gusto a manejar archivos CSV, a hacer scripts en Python y haber hecho ésto para las pruebas del modelo me parece brillante

Lo único que no sé si usar un script de Python o un cuaderno de Jypiter, de momento lo escribo en ambos y vamos viendo, aunque seguramente gane el script porque se me hace más fácil para GitHub Actions
