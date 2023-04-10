import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/test.jpeg", 0)
equ = cv2.equalizeHist(img)

plt.hist(img.flat, bins=100, range=(0, 255))
plt.show()

plt.hist(equ.flat, bins=100, range=(0, 255))
plt.show()

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl_img = clahe.apply(img)

plt.hist(cl_img.flat, bins=100, range=(0, 255))
plt.show()