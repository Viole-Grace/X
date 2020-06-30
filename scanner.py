import cv2
import numpy as np 

import time


import sharingan
from sharingan import mangekyo

def map_input(img):

	"""
		Take a single image as input, resize and convert to grayscale, return the image
	"""

	image = cv2.imread(img)
	image = cv2.resize(image, (720,720)) #720p resolution
	orig = image.copy()

	grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
	# cv2.imshow('Grayscaled Image', image)

	# time.sleep(2)

	blurred_image = cv2.GaussianBlur(grayscale, (5,5), 0) #kernel size = 7x7
	# ret, sharpened_image = cv2.threshold(grayscale, 30, 255, cv2.THRESH_BINARY) 
	# cv2.imshow('Gaussian Blur on Grayscaled Image', blurred_image)

	# time.sleep(3)

	return orig, blurred_image #returns a copy of the original image and the blurred grayscale version of the image, resized to 720x720

def eagle_eye(image):
	"""
		Detect edges and find contours for an image, then extract the key area of an image
		Returns key area of the image
	"""
	canny_edges = cv2.Canny(image, 30, 50) #min = 30, max = 50 as threshold for pixels
	# cv2.imshow('Edges detected', canny_edges)

	contours, _ = cv2.findContours(canny_edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #simple approximation for necessary boundaries
	contours = sorted(contours, key = cv2.contourArea, reverse=True) #get all contours. Reverse = True will give you the biggest one since its sorted

	for c in contours:

		p = cv2.arcLength(c, True) #find a square / closed shape. Returns an approximate square
		approx = cv2.approxPolyDP(c, 0.02*p, True) #try with other values between 0~0.1

		if len(approx) == 4: #if it has 4 corners / sides
			target = approx

			break

	approx = mangekyo(target) #find endpoints of a target area

	tenketsu = np.float32([[0,0],[720,0],[720,720],[0,720]]) #720x720 target mapping

	output = cv2.getPerspectiveTransform(approx, tenketsu) #eagle eye view of the target area

	return output #return the eagle eye view of the image

def fuuin(output, copy):

	"""
		Sealing function. Takes the output mapped, overlays it on a copy of the image and returns a scanned copy
	"""

	scanned_copy = cv2.warpPerspective(copy, output, (720,720)) #720x720 version of the image

	# cv2.imshow('Scanned Copy',scanned_copy) #show the scanned copy
	return scanned_copy

def calling_card():


	#get the inputs first

	# filename = input("Please enter an image filename to convert to a scanned copy : ")

	filename = 'hello.jpg'

	copy, blurred_image = map_input(filename)
	# time.sleep(3)
	print(blurred_image[0], len(blurred_image))
	output = eagle_eye(blurred_image)
	print(output[0], len(output))
	scanned_copy = fuuin(output, copy)
	print(scanned_copy[0], len(scanned_copy))
	# cv2.imshow('Scanned', scanned_copy)

	time.sleep(5)
	cv2.imwrite(filename.split('.')[0]+str('_scanned.jpg'), scanned_copy)

calling_card() #call all functions