import cv2

variant = 12
delta = 4 + 4*(variant % 3)

alpha = 1

container = cv2.imread('baboon.tif')
mean = 5
std = 1