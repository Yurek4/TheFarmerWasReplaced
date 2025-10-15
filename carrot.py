
def carrot_collet():
	carrot_now = num_items(Items.Carrot) 
	change_hat(Hats.Gray_Hat)
	print(carrot_now)
	hay_now = num_items(Items.Hay)
	wood_now = num_items(Items.Wood)
	if get_ground_type() == Grounds.Soil:
		while carrot_now < 1000000:
			for i in range (12):
				for v in range(get_world_size()):
					carrot_now = num_items(Items.Carrot)
					plant(Entities.Carrot)
					move(North)
					if can_harvest():
						harvest()
						plant(Entities.Carrot)
				move(East)
	
		
	
	
