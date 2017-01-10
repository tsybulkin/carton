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



def run(q_img, steps_nbr=10):
	
	## delete default Cubes
	boxes = get_boxes()
	for b in boxes: b.select = True

	bpy.data.objects['Lamp'].select = False
	bpy.data.objects['Camera'].select = False
	bpy.ops.object.delete() 

	init_camera()
	init_light()

	q_profile = util.get_profile(q_img)
	u_curr = 0.0

	xy0, obj_nbr = scn.estimate_img(q_img, MY_XYZ, MY_EULER)
	scene = gen.init_scn(xy0, obj_nbr)
	build(scene)
	boxes = get_boxes()
	print("nbr of boxes:", len(boxes))

	i = 0
	while i < steps_nbr:
		i += 1
		print("round: ", i)

		p_scn = gen.get_proposal(scene)
		set_params(boxes, p_scn)
		p_img = take_image(p_scn)

		u = util.similarity(p_img, q_profile)
		if point_accepted(u,u_curr):
			scene = p_scn
			u_curr = u



def build(scene):
	for (xyz,th,dim) in scene:
		bpy.ops.mesh.primitive_cube_add(location=xyz)
		bpy.ops.transform.resize(value=0.5*dim)



def get_boxes():
	return [ ob for ob in bpy.data.objects if ob.type == 'MESH' ]



def set_params(boxes, scene):
	assert len(boxes) == len(scene)

	for i in range(len(boxes)):
		boxes[i].location = scene[i][0]
		boxes[i].dimensions = scene[i][2]
		# TODO: add later theta



def point_accepted(u2,u1):
	if u2 - u1 >= 0.: return True
	else: return np.random.uniform() < np.exp((u2-u1)*100)



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


