def hay_collet():
	change_hat(Hats.Purple_Hat)
	hay_now = num_items(Items.Hay)
	print(hay_now)
	if get_ground_type() == Grounds.Grassland:
		while hay_now < 1000000:
		
			for i in range(12):
				for v in range(get_world_size()):
					if can_harvest():
						harvest()
						hay_now = num_items(Items.Hay)
						move(North)					
				move(East)		
