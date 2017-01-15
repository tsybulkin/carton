#
# This module contains generative model of the scene
#

import numpy as np

MIN_SIZE = 0.2
MAX_SIZE = 0.6

K = np.array([  [500., 0., 320.],
				[0., 500., 240.],
				[0.,   0., 1.]])
Rt = np.array([ [0., -1., 0., 0.],
				[0., 0., -1., 1.],
				[1., 0., 0., 5.] ])


def get_init_point(n=2):
	return [ (np.random.randn(2), MIN_SIZE + np.random.rand(3) * (MAX_SIZE-MIN_SIZE) ) 
				for _ in range(n) ]


def get_vedges(scene):
	for (xy, dimensions) in scene:
		## find the farthest vertex and exclude it
		pass
		## return projected edges
	return []



def xyz2uv(xyz):
	u,v,w = K.dot(-Rt).dot(np.hstack([xyz,1.]))
	return np.array([u/w,v/w])






######### old code ##########################


def get_proposal(point):
	""" Modifies objects properties and returns them
	"""
	new_scn = []
	for (xyz,th,dim) in scene:
		dim1 = dim + 0.5 * np.random.randn(3)
		for i in range(3):
			if dim1[i] < 0.2: dim1[i] = 0.2
			if dim1[i] > 0.6: dim1[i] = 0.6

		x = xyz[0] + 0.5 * np.random.randn(1)
		y = xyz[1] + 0.5 * np.random.randn(1)
		z = dim1[2] / 2

		new_scn.append( (np.array([x,y,z]),th, dim1) )

	return new_scn



def init_scn(xy0, obj_nbr):
	""" Generates a given number of objects around a given point xy0
	Returns the list of object properties in a tuple (xyz, th, dimensions) 
	"""
	scene = []

	for _ in range(obj_nbr):
		w1 = np.random.uniform(0.2, 0.6)
		w2 = np.random.uniform(0.2, 0.6)
		w3 = np.random.uniform(0.2, 0.6)
		x = xy0[0] + np.random.uniform(-1.5, 1.5)
		y = xy0[1] + np.random.uniform(-1.5, 1.5)
		z = w3 / 2
		th = np.random.uniform(-np.pi/2, np.pi/2)

		xyz = np.array([x,y,z])
		dim = np.array([w1,w2,w3])

		scene.append((xyz,th,dim))

	return scene


