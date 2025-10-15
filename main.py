import pos_inicial
import Terreno
import hay
import Wood
import carrot


pos_inicial.primeira_casa()



while True:

	
	if get_ground_type() == Grounds.Grassland:
		hay.hay_collet()
		Wood.wood_collet()

	Terreno.prepararTerreno()
	carrot.carrot_collet()
