import numpy as np 
from PIL import Image

from scanner import calling_card
from save_to_pdf import single_image2pdf, multiple_images2pdf

def convert_image_to_pdf():

	"""
		Takes in an input image, converts to PDF
	"""

	filename = input('Enter image file name : ')

	#scan image first, return saved image path
	scan_path = calling_card(filename)

	#convert single image to pdf
	single_image2pdf(filename = scan_path, pdf_name = 'Sample single image PDF')

def convert_images_to_pdf():

	"""
		Takes in multiple images, converts to scanned copies, then combines all images into a single PDF
	"""
	images = []
	scan_dir = 'Scanned/'

	to_break = 1

	while to_break:
	
		to_break = int(input('Press 1 to enter a new image name to convert. Otherwise Press 0.\nYour Choice : '))

		if to_break != 0 and to_break != 1:

			print('Invalid Option. Exiting')

			return

		if to_break == 1:

			# input an image
			image = input('Enter Image name : ')
			images.append(image)

		elif to_break == 0:

			#all images to be scanned have been selected
			print('All images have been selected.')

	#scan all images
	if images != []:

		for image in images:
			
			_ = calling_card(image) #scan image

		#convert all the scanned images to a single pdf
		multiple_images2pdf(files = scan_dir, pdf_name = 'Sample multiple images to PDF')

convert_images_to_pdf() #test