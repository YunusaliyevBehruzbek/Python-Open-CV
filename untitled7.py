# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZQL3k4Hji1rLrhtLjPELsTx_tR0trDra
"""

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("rasm1.jpg")
rasm1=cv2.imread("rasm2.jpg")
rasm2=cv2.imread("rasm3.jpg")
rasm3=cv2.imread("rasm4.jpg")
rasm4=cv2.imread("rasm5.jpg")
cv2_imshow(rasm)
cv2_imshow(rasm1)
cv2_imshow(rasm2)
cv2_imshow(rasm3)
cv2_imshow(rasm4)
oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab import drive
drive.mount('/content/drive')