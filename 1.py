

import numpy as np

width = 640
height = 480

#bpy.ops.mesh.primitive_cube_add()
#bpy.data.objects['Cube.001'].delete()

Cub = bpy.data.objects['Cube']
Cub1 = bpy.data.objects['Cube.002']
Cub1.location = Vector((3.,3.,1.))

Cub.dimensions = Vector((3.,3.,2.))
Cub.location = Vector((0.,0.,1.))

Cam = bpy.data.objects['Camera']

# render parameters
bpy.context.scene.render.engine = 'BLENDER_RENDER'
bpy.context.scene.render.resolution_x = width
bpy.context.scene.render.resolution_y = height
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 1

# switch on nodes
bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree
links = tree.links

# create input render layer node
rl = tree.nodes.new('CompositorNodeRLayers')
rl.location = 0,200

# create output node
v = tree.nodes.new('CompositorNodeViewer')
v.location = 200,200
v.use_alpha = False

# link Image output to Viewer input
links.new(rl.outputs[0], v.inputs[0])

ren = bpy.ops.render.render()

im_blend = bpy.data.images['Viewer Node']
print ('pixels:', len(im_blend.pixels))
im = 255*np.array(im_blend.pixels).reshape((height,width,4))
im = im[::-1,:,:].astype('uint8')

print (im[190:210,273:290,0])

print (dir(Cam))
