#
#


import numpy as np
import scipy

import gen,util

MY_XYZ = Vector((6.,-4., 1.78))
MY_EULER = Euler((1.3, 0., 0.8), 'XYZ')


def run(q_img, steps_nbr=100):
	init_camera()
	init_light()

	xy0, obj_nbr = scn.estimate_img(q_img, my_coords)
	scn = gen.init_scn()

	i = 0
	while i < steps_nbr:
		i += 1

		p_scn = gen.get_proposal(scn)

		u = util.similarity()



def init_camera():
	Cam = bpy.data.objects['Camera']
	Cam.location = MY_XYZ
	Cam.rotation_euler = MY_EULER



def init_light():
	Lamp = bpy.data.objects['Lamp']
	
