import numpy as np
import cv2
from get_sudoko_image import read_img
from get_sudoko_box import get_points
from transform_sudoko_box import transform_perspective
from get_digits import get_digits 
from sudoko_solve import check_and_solve
from display_solution import display_sol
from transform_sudoko_box import transform_perspective_reverse
import tensorflow as tf
import numpy as np
import tensorflow.keras as keras



model = tf.keras.models.load_model("./model/m1.h5")

img = read_img()
while True:
        cv2.imshow("raw image",img)
        if cv2.waitKey(0) == ord('q'):
            break

cv2.destroyAllWindows()
#print(img.shape)

points = get_points(img)
img_trans = transform_perspective(img,points)

img_thres,unsolved_sudoko = get_digits(img_trans,model)

while True:
        cv2.imshow("Transformed",img_thres)
        if cv2.waitKey(0) == ord('q'):
            break

cv2.destroyAllWindows()

print(unsolved_sudoko)
solved = check_and_solve(unsolved_sudoko)
disp_img = display_sol(img_trans,unsolved_sudoko,solved)
#img_rev_trans = transform_perspective_reverse(disp_img,points,img)
