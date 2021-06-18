#Imports
import pygame 
import player
import sprites
import objects
import time

# configs
pygame.init()

screen = pygame.display.set_mode((256 *2,144*2))
clock = pygame.time.Clock()

item = {'map1':None, 'map2':None, "map3":None}

def map1(x,y):
	x = x
	y = y
	run = True
	index = 0
	#calling classes
	playerr = player.Playerclass(x*2, y*2, screen)


	#=== Game Loop ==== 
	while run:
		clock.tick(8)
		screen.blit(sprites.ancientmap1,(0,0))
		keys = pygame.key.get_pressed()

		for event in pygame.event.get():
			# Quit event
			if event.type == pygame.QUIT:
				run = False

		#rendering diffrent objects
		
		for i in objects.objectmap1:
			i.update(screen)
		#player udate
		playerr.update(index, objects.objectmap1)

		#index update
		index = (index + 1) % 4

		# check map collison
		if item['map1'] == None:
			objects.map1.update(screen)
			if pygame.Rect.colliderect(pygame.Rect(playerr.x, playerr.y, playerr.width*2, playerr.height*2), pygame.Rect(objects.map1.x, objects.map1.y, objects.map1.newwidth, objects.map1.newheight)):
				font = objects.Font('press "E" to collect the map and press "m" to open map', screen, 10)
				font.update()
				if keys[pygame.K_e]:
					item['map1'] = 'collected'
					font = objects.Font('collected map1', screen, 20)
					font.update()
				

					
						

		if item['map1'] != None and playerr.y <=  -3:
			map2(130, 124)
		elif playerr.y <= -3:
			font = objects.Font('collect map 1', screen, 20)
			font.update()
			
		if item['map1'] != None:
			if keys[pygame.K_m]:
				objects.tresuremap1.update(screen)
				if ['map2'] != None:
					if keys[pygame.K_RIGHT]:
						pass



		#game update
		pygame.display.flip()
	pygame.quit()

def map2(x,y):
	x = x
	y = y
	run = True
	index = 0

	#calling classes
	playerr = player.Playerclass(x*2, y*2, screen)


	#=== Game Loop ==== 
	while run:
		clock.tick(8)
		screen.blit(sprites.map2,(0,0))

		for event in pygame.event.get():
			# Quit event
			if event.type == pygame.QUIT:
				run = False


		for i in objects.objectmap2:
			i.update(screen)

		#player udate
		playerr.update(index, objects.objectmap2)

		#index update
		index = (index + 1) % 4

		if playerr.y >= (144 -20)*2:
			map1(111, 0)

		#game update
		pygame.display.flip()
	pygame.quit()



map1(40,72)


