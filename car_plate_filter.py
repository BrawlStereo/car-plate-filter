import numpy as np
import cv2
import matplotlib.pyplot as plt

def procesar_placa(ruta_imagen, titulo, indice):
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

    # Binarizar la imagen y suavizar
    _, imagen = cv2.threshold(imagen, 110, 255, cv2.THRESH_BINARY_INV)
    imagen = cv2.medianBlur(imagen, 15)

    # Detección de bordes
    bordes = cv2.Canny(imagen, threshold1=100, threshold2=200)

    plt.subplot(2, 2, indice)
    plt.imshow(bordes, cmap='gray')
    plt.title(titulo)
    plt.axis('off')

plt.figure(figsize=(10, 10))
procesar_placa("placa_q.jpg", "Placa 1", 1)
procesar_placa("placa_2.jpg", "Placa 2", 2)
procesar_placa("placa_3.jpg", "Placa 3", 3)
procesar_placa("placa_4.jpg", "Placa 4", 4)
plt.subplot(2, 2, 1)

plt.tight_layout()
plt.show()