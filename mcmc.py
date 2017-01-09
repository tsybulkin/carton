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
	q_profile = util.get_profile(q_img)
	u_curr = 0.1

	xy0, obj_nbr = scn.estimate_img(q_img, my_coords)
	scn = gen.init_scn()

	i = 0
	while i < steps_nbr:
		i += 1

		p_scn = gen.get_proposal(scn)
		p_img = take_image(p_scn)

		u = util.similarity(p_img, q_profile)



def init_camera():
	Cam = bpy.data.objects['Camera']
	Cam.location = MY_XYZ
	Cam.rotation_euler = MY_EULER



def init_light():
	Lamp = bpy.data.objects['Lamp']
	print("lamp location:", Lamp.location)
	


def take_image(p_scn):
	# TODO: render the scene and return the image

	return np.zeros(480,640,3)


if __name__ == '__main__':
	# TODO: pass q_mage as an argument
	img = np.zeros(480,640,3)

	run(img, 1)


