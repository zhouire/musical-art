import cv2
import numpy as np
import imgtomusic

drawing = False # true if mouse is pressed
ix,iy = -1,-1
mode = False # if True, draw rectangle. Press 'm' to toggle to curve
color = (122,122,122) #press c to center new color
brush_size= 2 #press s to change brush size


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),color,-1)
            else:
                cv2.circle(img,(x,y),brush_size,color,-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),color,-1)
        else:
            cv2.circle(img,(x,y),brush_size,color,-1)
            
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img) 
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('s'):
         brush_size = int(input('new brush size: '))
    elif k == ord('c'):
         R = int(input('new R value: '))
         G = int(input('new G value: '))
         B = int(input('new B value: '))
         color = (B,G,R)
    elif k == 27:
        cv2.imwrite("img.jpg", img)
        break

cv2.destroyAllWindows()