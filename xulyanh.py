import cv2
import numpy as np

#Doc anh
img = cv2.imread('key.jpg',1)
img.
cv2.imshow('Hinh',img)

#Chuyen sang hinh xam
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Hinh Xam',img2)

#Chuyen sang anh nhi ơhan
img3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 5)
cv2.imshow('Hinh Nhi Phan',img3)

#Can bang Histograms
img4 = cv2.equalizeHist(img2)
cv2.imshow('Histograms',img4)

#Bo loc Gaussian
img5 = cv2.GaussianBlur(img3,(15,15),0)
cv2.imshow('Gaussian',img5)

#Bo loc Median
img6 = cv2.medianBlur(img3,15)
cv2.imshow('Median',img6)

#Camera => Chuyen Sang Anh Xam
cap = cv2.VideoCapture(0)
if (cap.isOpened() == False): 
  print("Unable to read camera feed")

while(True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('Camera',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
