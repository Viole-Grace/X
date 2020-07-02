import PIL

from PIL import Image

import os

#use the directory to scan for all images taken

def single_image2pdf(filename, pdf_name = 'Image_to_PDF.pdf'):

	image = Image.open(filename)

	if '.' in pdf_name:

		if pdf_name.split('.')[1] != 'pdf': #if extension for pdf name is not .pdf
			pdf_name = pdf_name.split('.')[0]+str('pdf') #add .pdf extension 

	else:

		pdf_name = pdf_name+str('.pdf')

	#save it into a directory called 'Converted PDF'
	if 'Converted PDF' not in os.listdir():
		os.mkdir('Converted PDF')

	image.save('Converted PDF/'+str(pdf_name), 'PDF', resolution=100.0, save_all = True)

	print('Converted Image to PDF.')

	return None

def multiple_images2pdf(files='Scanned', pdf_name = 'Image_to_PDF.pdf'):
	"""
		Takes in a directory of images and makes a single PDF of all the images.
		files = a directory name
	"""

	image_list = [] #list to store images

	for file in os.listdir(files): #for each scanned image in folder

		print("Image name : {}".format(file))

		image = Image.open(files+'/'+str(file))

		image_list.append(image)

	print("Number of images to be converted : {}".format(len(image_list)))

	if '.' in pdf_name:

		if pdf_name.split('.')[1] != 'pdf': #if extension for pdf name is not .pdf
			pdf_name = pdf_name.split('.')[0]+str('pdf') #add .pdf extension

	else:

		pdf_name = pdf_name+str('.pdf')

	#save it into a directory called 'Converted PDF'
	if 'Converted PDF' not in os.listdir():
		os.mkdir('Converted PDF')

	image.save('Converted PDF/'+str(pdf_name), 'PDF', resolution=100.0, save_all = True, append_images=image_list)

	print('Converted Images to PDF.')

	return None


# multiple_images2pdf('Scanned','LMAO') #test