import cv2
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
 
color_hsv = [[0, 191, 0, 22, 255, 255],
            [34, 91, 80, 179, 255, 255]]
color_bgr = [[51, 153, 255], #naranja
             [51, 255, 51]] #verde
puntos =  []
 

def encontrar_color(imag, color_hsv, color_bgr):

    imag_hsv = cv2.cvtColor(imag, cv2.COLOR_BGR2HSV)
    cont = 0
    puntos2 = []

    for color in color_hsv:
        ini = np.array(color[0:3])
        fin = np.array(color[3:6])
        mask = cv2.inRange(imag_hsv, ini, fin)
        x, y = encontrar_contorno(mask)
        cv2.circle(imag_final, (x, y), 15, color_bgr[cont], cv2.FILLED)
        
        if x != 0 and y != 0:
            puntos2.append([x, y, cont])
        cont += 1

    return puntos2
 

def encontrar_contorno(imag):
    contornos, hierarchy = cv2.findContours(imag, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for contor in contornos:
        area = cv2.contourArea(contor)
        if area > 500:
            perim = cv2.arcLength(contor, True)
            aprox = cv2.approxPolyDP(contor, 0.02 * perim, True)
            x, y, w, h = cv2.boundingRect(aprox)

    return x + w // 2, y #obtiene el punto medio en el punto alto
 

def drawOnCanvas(puntos,color_bgr):
    for punt in puntos:
        cv2.circle(imag_final, (punt[0], punt[1]), 10, color_bgr[punt[2]], cv2.FILLED)
 
 
while True:
    exito, imag = cap.read()
    imag_final = imag.copy()
    puntos2 = encontrar_color(imag, color_hsv, color_bgr)
    
    if len(puntos2) != 0:
        for newP in puntos2:
            puntos.append(newP)
    if len(puntos) != 0:
        drawOnCanvas(puntos, color_bgr)
 
    cv2.imshow("Result", imag_final)
    if cv2.waitKey(1) and 0xFF == ord('p'):
        break
