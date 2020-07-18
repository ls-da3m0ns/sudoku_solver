import cv2
import os
import numpy as np


def display_sol(image,unsolved,solved,shape = 720):
    blank = np.zeros((720,720),np.uint8)
    unsolved = np.array(unsolved).reshape(9,9)
    for i in range(9):
        for j in range(9):
            x_cord = (i)*int(shape/9) +30
            y_cord = (j)*int(shape/9) +50
            if unsolved[j,i] == 0:
                cv2.putText(image,str(solved[j,i]),(x_cord,y_cord),cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),2)

    while True:
            cv2.imshow("Solved",image)
            if cv2.waitKey(0) == ord('q'):
                break

    cv2.destroyAllWindows()

    return image

