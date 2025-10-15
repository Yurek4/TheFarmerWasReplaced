def wood_collet():
	change_hat(Hats.Green_Hat)
	wood_now = num_items(Items.Wood)
	print(wood_now)
	
	
	if get_ground_type() == Grounds.Grassland:
		while wood_now < 1000000:
			for i in range(12):
				for v in range(get_world_size()):
					if can_harvest():
						harvest()
						x =  get_pos_x()
						y = get_pos_y()
						if ( x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
							plant(Entities.Tree)
							move(North)
							wood_now = num_items(Items.Wood)
						else:
							plant(Entities.Bush)
							move(North)
							wood_now = num_items(Items.Wood)
						
			move(East)
				
	
