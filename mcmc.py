#
#

import bpy,os,sys
import numpy as np
import scipy

blend_dir = os.path.basename(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

import imp
import gen, util, scn

imp.reload(gen)
imp.reload(util)
imp.reload(scn)

MY_XYZ = Vector((4.,-4., 1.78))
MY_EULER = Euler((1.35, 0., 0.85), 'XYZ')



def run(q_img, steps_nbr=100):
	## delete default Cube
	bpy.data.objects['Lamp'].select = False
	bpy.data.objects['Camera'].select = False
	bpy.data.objects['Cube'].select = True
	bpy.ops.object.delete() 

	init_camera()
	init_light()

	q_profile = util.get_profile(q_img)
	u_curr = 0.1

	xy0, obj_nbr = scn.estimate_img(q_img, MY_XYZ, MY_EULER)
	scene = gen.init_scn(xy0, obj_nbr)
	build(scene)

	i = 0
	while i < steps_nbr:
		i += 1

		p_scn = gen.get_proposal(scene)
		p_img = take_image(p_scn)

		u = util.similarity(p_img, q_profile)


def build(scene):
	for (xyz,th,dim) in scene:
		bpy.ops.mesh.primitive_cube_add(location=xyz)
		bpy.ops.transform.resize(value=0.5*dim)





def init_camera():
	Cam = bpy.data.objects['Camera']
	Cam.location = MY_XYZ
	Cam.rotation_euler = MY_EULER



def init_light():
	Lamp = bpy.data.objects['Lamp']
	print("lamp location:", Lamp.location)
	


def take_image(p_scn):
	# TODO: render the scene and return the image

	return np.zeros((480,640,3),np.dtype(np.uint8))


if __name__ == '__main__':
	# TODO: pass q_mage as an argument
	img = np.zeros((480,640,3),np.dtype(np.uint8))

	run(img, 1)


