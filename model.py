import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


def prueba(model_path, label_path, image_path):
    # Desactivar notación científica para claridad
    np.set_printoptions(suppress=True)

    # Cargar el modelo
    model = load_model(model_path, compile=False)

    # Cargar las etiquetas y limpiar los nombres
    class_names = [line.strip() for line in open(label_path, "r").readlines()]

    # Crear array con la forma adecuada para el modelo de Keras
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Cargar y procesar la imagen
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convertir la imagen en un array numpy y normalizar
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Realizar la predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]  # Obtener la etiqueta de la clase
    confidence_score = prediction[0][index]

    if index == 0:
        return "¡ADVERTENCIA! El lugar que está tratando de visitar es muy inseguro, por favor tenga precaución."
    elif index == 1:
        return "¡ALERTA! EL PRESIDENTE QUE ESTA VIENDO A CONTINUACIÓN ESTÁ COMETIENDO FRAUDE, MEJOR VOTE POR LUISA"
    elif index == 2:
        return "El lugar que quiere visitar es seguro, si ve algun error pruebe en diferentes angulos (recomendado)"
