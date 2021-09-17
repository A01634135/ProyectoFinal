import cv2
import numpy as np
 
frame_largo = 200
frame_alto = 200
cap = cv2.VideoCapture(0)
cap.set(3, frame_largo)
cap.set(4, frame_alto)
 
 
def empty(a):
    pass
 
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
    imgHsv = cv2.cvtColor(imag, cv2.COLOR_BGR2HSV)
 
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VAL Min", "HSV")
    v_max = cv2.getTrackbarPos("VAL Max", "HSV")
 
    ini = np.array([h_min, s_min, v_min])
    fin = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, ini, fin)
    res = cv2.bitwise_and(imag, imag, mask = mask)
 
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    h_stack = np.hstack([imag, mask, res])
    cv2.imshow('Horizontal Stacking', h_stack)
    
    if cv2.waitKey(1) and 0xFF == ord('p'):
        break
 
cap.release()
cv2.destroyAllWindows()
