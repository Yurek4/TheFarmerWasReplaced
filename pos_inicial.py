def primeira_casa():
	x = get_pos_x()
	y = get_pos_y()
	print(x)

	while x != 0:
		move(West)
		x = x -1
	while y != 0:
		move(South)
		y = y -1
