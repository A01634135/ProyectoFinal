"""
Programa que despliega un menu para encontrar los valores minimos y maximos de HSV de un color.
Recibe un video en vivo y despliega un menu con trackbars, y 3 ventanas con el video original, una mascara y su resultado bitwise
"""


import cv2
import numpy as np
 
frame_largo = 200
frame_alto = 200
cap = cv2.VideoCapture(0) #recibe video de la camara default
cap.set(3, frame_largo)
cap.set(4, frame_alto)
 

""" Funcion que no regresa nada """
def empty(a):
    pass


""" Crea una ventana con menu en el que hay 6 trackbars  """
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL Min", "HSV", 0, 255, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VAL Max", "HSV", 255, 255, empty)
 
 
while True:
 
    exito, imag = cap.read()
    imgHsv = cv2.cvtColor(imag, cv2.COLOR_BGR2HSV) #convierte la imagen de color a HSV
 
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VAL Min", "HSV")
    v_max = cv2.getTrackbarPos("VAL Max", "HSV")
 
    ini = np.array([h_min, s_min, v_min])
    fin = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, ini, fin) #crea una mascara con los valores HSV
    res = cv2.bitwise_and(imag, imag, mask = mask) #conjuncion and de la mascara e imagen
 
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    h_stack = np.hstack([imag, mask, res])
    cv2.imshow('Horizontal Stacking', h_stack) #muestra ventana con las versiones de la imagen
    
    if cv2.waitKey(1) and 0xFF == ord('p'): #termina el programa
        break
 

cap.release()
cv2.destroyAllWindows()
