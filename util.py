#
# This module compares two images and estimates its similarity
#
import numpy as np
from scipy import ndimage, misc


def similarity(img, q_profile): 
	p_profile = get_profile(img)

	# TODO: compare profiles and return the degree of its similarity
	return np.random.uniform()




def get_profile(img): 
	""" The function returns a list of points in 4-dimensional space (ro, th, t1, t2),
		which represent the edges extracted from the image, where
		(ro, th) - is a line in polar referrence frame and
		t1, t2 - two scalars defining an edge laying in this line
	"""
	gray = np.average(img[:,:,:3],axis=2)
	print('gray shape:',gray.shape)
	mask = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
	edges = np.zeros(gray.shape)
	edges = abs(ndimage.convolve(gray,mask))

	#sx = ndimage.sobel(img, axis=0, mode='constant')
	#sy = ndimage.sobel(img, axis=1, mode='constant')
	#sob = np.hypot(sx, sy)
	misc.imsave('8.png',edges)


