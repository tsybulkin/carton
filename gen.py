#
# This module contains generative model of the scene
#

import numpy as np


def get_proposal(scn):
	# TODO:

	return 0.



def init_scn(xy0, obj_nbr):

	# TODO: return initial scene
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

