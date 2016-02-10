
def count_neighbours(grid,row,col):
	count_of_dot = 0
	if (row == 0) and (col == len(grid[row])-1):
		z = grid[row]
		z_left=z[col-1] 
		x = grid[row+1]
		x_center=x[col]
		x_left=x[col-1]
		if z_left ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_left ==1:
			count_of_dot+=1
	elif (row == (len(grid)-1)) and (col == len(grid[row])-1):
		z = grid[row]
		z_left=z[col-1] 
		x = grid[row-1]
		x_center=x[col]
		x_left=x[col-1]
		if z_left ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_left ==1:
			count_of_dot+=1	
	elif (row == (len(grid)-1)) and (col == 0):
		z = grid[row]
		z_rigt=z[col+1] 
		x = grid[row-1]
		x_center=x[col]
		x_right=x[col+1]
		if z_rigt ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_right ==1:
			count_of_dot+=1
	elif row == 0:
		z = grid[row]
		z_rigt=z[col+1]
		z_left=z[col-1] 
		x = grid[row+1]
		x_center=x[col]
		x_right=x[col+1]
		x_left=x[col-1]
		if z_rigt ==1:
			count_of_dot +=1
		if z_left ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_left ==1:
			count_of_dot+=1
		if x_right ==1:
			count_of_dot +=1
	elif row == (len(grid)-1):
		z = grid[row]
		z_rigt=z[col+1]
		z_left=z[col-1] 
		x = grid[row-1]
		x_center=x[col]
		x_right=x[col+1]
		x_left=x[col-1]
		if z_rigt ==1:
			count_of_dot +=1
		if z_left ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_left ==1:
			count_of_dot+=1
		if x_right ==1:
			count_of_dot +=1
	elif col == (len(grid[row])-1):
		z = grid[row]
		z_left=z[col-1] 
		x = grid[row+1]
		x_center=x[col]
		x_left=x[col-1]
		y = grid[row-1]
		y_center=y[col]
		y_left=y[col-1]
		if z_left ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_left ==1:
			count_of_dot+=1
		if y_center==1:
			count_of_dot+=1
		if y_left ==1:
			count_of_dot+=1
	elif row > 0:
		z= grid[row]
		z_rigt=z[col+1]
		z_left=z[col-1] 
		x = grid[row+1]
		x_center=x[col]
		x_right=x[col+1]
		x_left=x[col-1]
		y = grid[row-1]
		y_center=y[col]
		y_right=y[col+1]
		y_left=y[col-1]
		if z_rigt ==1:
			count_of_dot +=1
		if z_left ==1:
			count_of_dot +=1
		if x_center ==1:
			count_of_dot+=1
		if x_left ==1:
			count_of_dot+=1
		if x_right ==1:
			count_of_dot +=1
		if y_center ==1:
			count_of_dot +=1
		if y_left ==1:
			count_of_dot +=1
		if y_right ==1:
			count_of_dot +=1
	return count_of_dot


print count_neighbours(((1, 0, 0, 1, 0),
                  		(0, 1, 0, 0, 0),
                  		(0, 0, 1, 0, 1),
                  		(1, 1, 0, 0, 0),
                  		(1, 1, 1, 0, 0),
                  		(0, 1, 1, 1, 1)), 5, 0)

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
