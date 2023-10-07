import numpy as np
import cv2

blank_img= np.zeros((512,512, 3), np.int8)

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_img, (x, y), 100, (0,255,0), -1)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(blank_img, (x, y), 100, (255,0,0), -1)
        
cv2.namedWindow("drawing")
cv2.setMouseCallback('drawing', draw_circle)

while True:
    cv2.imshow('drawing', blank_img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break