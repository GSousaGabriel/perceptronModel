import numpy as np
import cv2


img= cv2.imread('../ACARMANBOSS.jpg')

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 30, (255,0,0), 2)
        
cv2.namedWindow('drawing')
cv2.setMouseCallback('drawing', draw_circle)

while True:
    cv2.imshow('drawing', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()