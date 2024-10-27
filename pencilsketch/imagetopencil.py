import cv2 as cv
import sys

img = cv.imread('fatcat.jpg')
grayscaleimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
negativeimg = 255 - grayscaleimg
negativeimg = cv.GaussianBlur(negativeimg, (101, 101), 0)
negativeimg = 255 - negativeimg
negativeimg = cv.divide(grayscaleimg, negativeimg, scale=255.0)
alpha = 1.2
beta = -123
negativeimg = cv.convertScaleAbs(negativeimg, alpha=alpha, beta=beta)

if negativeimg is None:
    sys.exit("Could not read the image.")
cv.imshow('Grayscale', negativeimg )
k = cv.waitKey(0)
cv.imwrite('fatsketchcat.jpg', negativeimg)