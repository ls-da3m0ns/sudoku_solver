import numpy as np
import cv2 
def transform_perspective(img,points,size=720):
    """
    size here is the final output size
    """
    pts_source = np.float32(points)
    pts_dest = np.float32([[0,0],[size,0],[0,size],[size,size]])
    print(pts_dest,pts_source)
    print(type(pts_source))
    transform = cv2.getPerspectiveTransform(pts_source,pts_dest)
    img_trans = cv2.warpPerspective(img,transform,(size,size))
    
    return img_trans

def transform_perspective_reverse(img,points,original,size=720):
    pts_dest = np.float32(points)
    pts_source = np.float32([[0,0],[size,0],[0,size],[size,size]])

    transform = cv2.getPerspectiveTransform(pts_source,pts_dest)
    img_trans = cv2.warpPerspective(img,transform,(original.shape[1],original.shape[0]))

    return img_trans
