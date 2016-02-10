def count_neighbours(tapl_s,ver,hor):
	count_of_dot = 0
	tapl_dest = tapl_s[ver]
	len_m_t = len(tapl_s) -1
	len_s = len(tapl_dest)-1
	len_a = len(tapl_s)-1

	if ver  0:
		tap_up_m = tapl_s[ver-1]
		point_up_m = tap_up_m[hor]
		point_up_l = tap_up_m[hor-1]
		point_up_r = tap_up_m[hor+1]
		if point_up_m == 1:
			count_of_dot += 1
		if point_up_l == 1:
			count_of_dot += 1
		if point_up_r == 1:
			count_of_dot += 1
		# middle pice
		tap_m = tapl_s[ver]
		point_l = tap_m[hor-1]
		point_r = tap_m[hor+1]
		if point_l == 1:
			count_of_dot += 1
		if point_r == 1:
			count_of_dot += 1
		# bottom pice
		tap_bott_m = tapl_s[ver+1]
		point_bott_m = tap_bott_m[hor]
		point_bott_l = tap_bott_m[hor-1]
		point_bott_r = tap_bott_m[hor+1]
		if point_bott_m == 1:
			count_of_dot += 1
		if point_bott_l == 1:
			count_of_dot += 1
		if point_bott_r == 1:
			count_of_dot += 1
	#square
	elif (((hor == 0) or (hor == len_m_t)) and ((ver == 0) or (ver == len_a))):
		#up right
		if (ver == 0) and (hor == len_m_t):
			tapl_bot_t = tapl_s[ver+1]
			#round dot
			tapl_l = tapl_dest[hor -1]
			tapl_b = tapl_bot_t[hor]
			tapl_b2 = tapl_bot_t[hor-1]
			if tapl_l == 1:
				count_of_dot +=1
			if tapl_b == 1:
				count_of_dot +=1
			if tapl_b2 == 1:
				count_of_dot +=1
		#bottom right
		if (ver == len_a) and (hor == len_m_t):
			tapl_up_t = tapl_s[ver-1]
			#round dot
			tapl_l = tapl_dest[hor -1]
			tapl_up = tapl_up_t[hor]
			tapl_up2 = tapl_up_t[hor-1]
			if tapl_l == 1:
				count_of_dot +=1
			if tapl_up == 1:
				count_of_dot +=1
			if tapl_up2 == 1:
				count_of_dot +=1
		#up left
		if (ver == 0) and (hor == 0):
			tapl_bottom_left =  tapl_s[ver+1]
			#round dot
			tapl_r = tapl_dest[hor +1]
			tapl_r_b= tapl_bottom_left[hor]
			tapl_r_b2 = tapl_bottom_left[hor+1]
			if tapl_r == 1:
				count_of_dot +=1
			if tapl_r_b == 1:
				count_of_dot +=1
			if tapl_r_b2 == 1:
				count_of_dot +=1
		#bottom left
		if (ver == len_a) and (hor == 0):
			tapl_up_t2 = tapl_s[ver-1]
			#round dot
			tapl_l2 = tapl_dest[hor +1]
			tapl_up2 = tapl_up_t2[hor]
			tapl_up22 = tapl_up_t2[hor+1]
			if tapl_l2 == 1:
				count_of_dot +=1
			if tapl_up2 == 1:
				count_of_dot +=1
			if tapl_up22 == 1:
				count_of_dot +=1
	
	return count_of_dot




print count_neighbours(((1, 0, 0, 1, 0),
                  		(0, 1, 0, 0, 0),
                  		(0, 0, 1, 0, 1),
                  		(1, 0, 0, 0, 0),
                  		(0, 0, 1, 0, 0),), 1, 2)

print count_neighbours(((1, 0, 0, 1, 0),
                  		(0, 1, 0, 0, 0),
                  		(0, 0, 1, 0, 1),
                  		(1, 0, 0, 0, 0),
                  		(0, 0, 1, 0, 0),), 0, 0)

print count_neighbours(((1, 1, 1),
                  	    (1, 1, 1),
                        (1, 1, 1),), 1, 2)

print count_neighbours(((0, 0, 0),
                        (0, 1, 0),
                        (0, 0, 0),), 1, 1)