#
# This module compares two images and estimates its similarity
#
import numpy as np
from scipy import ndimage, misc

TOLLERANCE = 10. # total diference in pixels 


def similarity(v, v_golden):
	if len(v) == 0: 
		raise "Nothing to compare to each other as one set is empty"

	
	# TODO: for each edge in the first sorted list find a closest edge
	#	in the second list and measure the distance between edge verteces

	# edge format: (type, uv1, uv2). All edges are sorted on u1

	utility = sum( TOLLERANCE / (TOLLERANCE + min_dist(edge,v_golden)) for edge in v ) + \
				sum( TOLLERANCE / (TOLLERANCE + min_dist(ed_gold,v)) for ed_gold in v_golden )
	
	return utility



def min_dist(edge, other_edges):
	return min( np.linalg.norm(edge[0]-ed[0])+np.linalg.norm(edge[1]-ed[1]) 
					for ed in other_edges)



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


