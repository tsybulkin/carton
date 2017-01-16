#
# This module contains generative model of the scene
#

import numpy as np

MIN_SIZE = 0.2
MAX_SIZE = 0.6

K = np.array([  [500., 0., 320.],
				[0., 500., 240.],
				[0.,   0., 1.]])

## Camera angles
phi = np.pi / 9.   ## 20 degrees
th = np.pi / 4.


## Euler angles for zxz proper scheme with the third angle equals zero
c1,s1 = np.cos(phi),np.sin(phi)
c2,s2 = np.cos(th),np.sin(th)
DIST = 5.  # the distance of camera from the origin (0,0,0)  

Rt = np.array([ [ s2,	-c2, 0., 0.],
				[-s1*c2, -s1*s2, -c1, 0.],
				[ c1*c2,  c1*s2, -s1, DIST] ])

XYZc = np.array([-DIST*c1*c2, -DIST*c1*s2, DIST*s1])



def get_init_point(n=2):
	if n < 1: raise "There must be at least one object"

	return [ (np.random.randn(2), MIN_SIZE + np.random.rand(3) * (MAX_SIZE-MIN_SIZE) ) 
				for _ in range(n) ]



def get_vedges(scene):
	for (xy, dimensions) in scene:
		## find the farthest vertex and exclude it
		dx,dy,_ = dimensions / 2
		lower_verteces = [ xy + np.array([dx*i,0]) + np.array([0,dy*j]) 
							for i in [-1,1] for j in [-1,1] ]

		dist_to_vertices = [ (np.linalg.norm(XYZc[:2] - lower_verteces),v) 
								for v in lower_verteces]
		visible_vertices = sorted(dist_to_vertices,key=lambda tup:tup[0])
		visible_vertices.pop()
		print 'visible vertices:', visible_vertices


		## return projected edges

	return []



def xyz2uv(xyz):
	u,v,w = K.dot(Rt).dot(np.hstack([xyz,1.]))
	return np.array([u/w,v/w])



def get_proposal(scene):
	""" Modifies objects properties and returns them
	"""
	new_scn = []
	for (xy,dim) in scene:
		dim1 = dim + 0.5 * np.random.randn(3)
		for i in range(3):
			if dim1[i] < MIN_SIZE: dim1[i] = MIN_SIZE
			if dim1[i] > MAX_SIZE: dim1[i] = MAX_SIZE

		x = xy[0] + 0.5 * np.random.randn(1)
		y = xy[1] + 0.5 * np.random.randn(1)
		

		new_scn.append( (np.array([x,y]), dim1) )

	return new_scn




