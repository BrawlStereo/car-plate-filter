import numpy as np
import cv2
import matplotlib.pyplot as plt

def procesar_placa(img_path, titulo, index):
    # Cargar la imagen
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Binarizar la imagen y suavizar
    _, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)
    img = cv2.medianBlur(img, 15)

    # Detección de bordes
    edges = cv2.Canny(img, threshold1=100, threshold2=200)

    plt.subplot(2, 2, index)
    plt.imshow(edges, cmap='gray')
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