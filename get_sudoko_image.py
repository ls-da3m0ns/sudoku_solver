import cv2
import numpy as np
from imutils import contours as cnt_im

def read_img():
    img = cv2.imread("./sudoku_imgs/sudoko.png",1)
    return img

def capture_img():
    img = None
    vedio = cv2.VideoCapture(0)
    while True:
        try:
            check,frame = vedio.read()
            if check != 1:
                print("Retrying")
                check,frame = vedio.read()
        except:
            print("Problem reading Image")
        
        cv2.imshow("Current Frame",frame)
        if cv2.waitKey(0) == ord('c'):
            img = frame
            break
    vedio.release()
    cv2.destroyAllWindows()
    return img
