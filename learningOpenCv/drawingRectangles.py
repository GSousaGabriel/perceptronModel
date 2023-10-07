import numpy as np
import cv2

img= np.zeros((512, 512, 3))
drawing= False
ix, iy= -1, -1

def draw_rectangle(event, x, y, flags, param):
    global ix,iy,drawing
    
    if event == cv2.EVENT_MOUSEMOVE and drawing:
        print('rttfdsafasd')
        cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), 3)
        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing= False
        cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), 3)
    
    elif event == cv2.EVENT_LBUTTONDOWN:
        drawing= True
        ix,iy= x,y
        print(drawing)

cv2.namedWindow('rectanglesTest')
cv2.setMouseCallback('rectanglesTest', draw_rectangle)

while True:
    cv2.imshow('rectanglesTest', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()