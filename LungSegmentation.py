# -*- coding: utf-8 -*-

import cv2
from skimage.segmentation import clear_border

img=cv2.imread('case1_1.png',0)
cv2.imshow("origin image",img)

th,ostu_img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img_tmp=255-ostu_img

img_tmp=clear_border(img_tmp)

se_fill=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(21,21))
img_fill = cv2.morphologyEx(img_tmp, cv2.MORPH_CLOSE, se_fill)

se_open=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(21,21))
img_segmentation = cv2.morphologyEx(img_fill, cv2.MORPH_OPEN, se_open)
cv2.imshow("segmentation",img_segmentation)


paren=img & img_segmentation
cv2.imshow("image fusion",paren)

cv2.waitKey()


