import cv2 
import numpy as np
from imutils import contours as cnt_im

def get_points(img):
    
    #preprocessing to find contours
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_thre = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,39,10)
    
    #contours
    _,cnts,_ = cv2.findContours(img_thre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    #getting the largest contour by area
    largest_contour = cnts[0]
    for cnt in cnts:
        if cv2.contourArea(cnt)>cv2.contourArea(largest_contour):
            largest_contour = cnt
    
    #use a blank image to get lines from the largest_contours border
    img_blank = np.zeros(img.shape,np.uint8)
    img_blank = cv2.drawContours(img_blank,[largest_contour],-1,(0,255,0),2)
    
    edges = cv2.Canny(img_blank,40,150,apertureSize=3)
    lines = cv2.HoughLines(edges,1,np.pi/180,100)
    
    #filtering the lines so that we only have one line for each side
    
    horizontal = []
    vertical = []
    created = []
    flag = 0
    
    for line in lines:
        for (rho,theta) in line:
            flag = 0
            for (rho1,theta1) in created:
                if abs(rho-rho1)<10 and abs(theta-theta1)<10:
                    flag = 1
            if flag == 0:
                a = np.cos(theta)
                b = np.sin(theta)
                
                x1 = int(a*rho + 1000*(-b))
                y1 = int(b*rho + 1000*(a))
                x2 = int(a*rho - 1000*(-b))
                y2 = int(b*rho - 1000*(a))
                
                d = np.linalg.norm(np.array((x1,y1,0)) - np.array((x2,y2,0)))
#imp - >  #drawing line on main img
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
                slope = abs(1/np.tan(theta))
                if slope<1:
                    horizontal.append((rho,theta))
                else:
                    vertical.append((rho,theta))
                created.append((rho,theta))
    points = []
    #getting intersection points from lines
    
    for (rho,theta) in horizontal:
        for (rho1,theta1) in vertical:
            if(rho,theta) != (rho1,theta1):
                a = [[np.cos(theta),np.sin(theta)],[np.cos(theta1),np.sin(theta1)]]
                b = [rho,rho1]
                cor = np.linalg.solve(a,b)
                if list(cor) not in points:
                    points.append(list(cor))
    points.sort()

    center = (img.shape[0]/2,img.shape[1]/2)

    from scipy.spatial import distance
    print(center)


    

    if(len(points)>4):
        close = []
        sudoko_point = []
        min_distance = center[0]/2
        for pt1 in points:
            for pt2 in points:
                if (distance.euclidean(pt1,pt2)<(min_distance) and pt1[0] != pt2[0] and pt1[1] != pt2[1]):
                    if(distance.euclidean(pt1,center) < distance.euclidean(pt2,center)):
                        close.append(pt1)
                    else:
                        close.append(pt2)


        for pts in points:
            if(pts not in close):
                sudoko_point.append(pts)
    
    else:
        sudoko_point = points

    if (sudoko_point[0][1]>sudoko_point[1][1]):
            sudoko_point[0],sudoko_point[1]=sudoko_point[1],sudoko_point[0]
    if (sudoko_point[-1][1]<sudoko_point[-2][1]):
        sudoko_point[-1],sudoko_point[-2]=sudoko_point[-2],sudoko_point[-1]

    sudoko_point[1],sudoko_point[2]=sudoko_point[2],sudoko_point[1]

    if (len(sudoko_point)<4):
           #if number of pts detected is less than 4 then return whole image
        sudoko_point = [[0,0],[img.shape[0],0],[0,img.shape[1]],[img.shape[0],img.shape[1]]]
    else:
        #temp = sudoko_point[1]
        #sudoko_point[1] = sudoko_point[2]
        #sudoko_point[2] = temp 
        print("Points : ",sudoko_point)

 
    return sudoko_point