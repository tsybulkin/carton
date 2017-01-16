#
#

import numpy as np

import gen, util, scn



def run(q_img, steps_nbr=10):
	golden_point = gen.get_init_point()
	vset_golden = gen.get_vedges(golden_point)

	point = gen.get_init_point()
	u_curr = 0.  # initial similarity
	
	i = 0
	while i < steps_nbr:
		i += 1
		if i%100 == 0: print("round: ", i)

		new_point = gen.get_proposal(point)
		vset = gen.get_vedges(new_point)

		u = util.similarity(vset, vset_golden)
		if point_accepted(u,u_curr):
			print 'new point:', new_point
			point = new_point
			u_curr = u

	


def point_accepted(u2,u1):
	if u2 - u1 >= 0.: return True
	else: return np.random.uniform() < np.exp((u2-u1)*100)







if __name__ == '__main__':
	# TODO: pass q_mage as an argument
	img = np.zeros((480,640,3),np.dtype(np.uint8))

	run(img, 1000)


