import numpy as np 

def mangekyo(target):
	"""
		Take a target image, figure out the corners of the target area.

		Courtesy of pyimagesearch - Refer to https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/ for more information
	"""

	target = target.reshape((4,2))
	new_target = np.zeros((4,2), dtype = np.float32)

	add = target.sum(1)
	new_target[0] = target[np.argmin(add)]
	new_target[2] = target[np.argmax(add)]

	diff = np.diff(target, axis = 1)

	new_target[1] = target[np.argmin(diff)]
	new_target[3] = target[np.argmax(diff)]

	return new_target