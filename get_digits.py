import numpy as np
import cv2
from imutils import contours as cnt_im
from model_load import predict

def get_digits(img,model):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_thres = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,39,10)
    thresh1 = img_thres.copy()
    
    kernel = np.ones((1,1),np.uint8)
    thresh = cv2.morphologyEx(img_thres,cv2.MORPH_OPEN,kernel)
    thresh = cv2.dilate(thresh,kernel,iterations=3)
    kernel = np.ones((1,10),np.uint8)
    thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
    #kernel = np.ones((10,1),np.uint8)
    #thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
    

    thresh = cv2.bitwise_not(thresh)

    _,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    blank = np.zeros(img_gray.shape,np.uint8)


    final_contours = []
    for cnts in contours:
        epsilon = 0.04*cv2.arcLength(cnts,True)
        approx = cv2.approxPolyDP(cnts,epsilon,True)
        approx = cv2.convexHull(cnts)
        area = cv2.contourArea(approx)
        if area <=100000:
            final_contours.append(approx)
            
    rows,_ = cnt_im.sort_contours(final_contours,method = "left-to-right")
    
    kernel = np.ones((3,3),np.uint8)
    thresh1 = cv2.erode(thresh1,kernel,iterations=1)


    blank2 = blank.copy()
    
    for c in rows:
        blank = cv2.drawContours(blank,[c],-1,(255),-1)
        blank_base = cv2.drawContours(blank2,[c],-1,(255),-1)
        blank = cv2.bitwise_and(thresh1,blank,mask=blank)
    


    cv2.destroyAllWindows()
    _,cnts,_ = cv2.findContours(blank,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if cv2.contourArea(c) < 200:
            (x, y, w, h) = cv2.boundingRect(c)
            blank[y:y + h, x:x + w] = 0
            


    factor = blank.shape[0]//9
    unsolved = []
    for i in range(9):
        for j in range(9):
            part = blank[i*factor:(i+1)*factor, j*factor:(j+1)*factor ]
            part = cv2.resize(part,(28,28))
            cv2.imwrite("./croped_sudoko_box/{}_{}.jpg".format(i,j),part)
            num = predict(part,model)
            unsolved.append(num)
    for i in range(10):
        cv2.line(blank,(0,factor*i),(blank.shape[1],factor*i),(255),2,2)
        cv2.line(blank,(factor*i,0),(factor*i,blank.shape[0]),(255),2,2)
    
    return blank,unsolved
    
