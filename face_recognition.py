# -*- coding: utf-8 -*-
"""Face_Recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JuQAOmFWEa3IN0pZLk8EdgATmYQYPlxs
"""

!pip install face_recognition

import face_recognition as fr

import cv2

from google.colab.patches import cv2_imshow

import cv2

from google.colab import drive
drive.mount('/content/drive')

image= cv2.imread('/content/drive/My Drive/638113.jpg')

cv2_imshow(image)

locs=fr.face_locations(image)

print(len(locs), " faces detected")

