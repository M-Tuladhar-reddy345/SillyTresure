#imports
import pygame 
import player
import sprites
import objects
import time





#main game class
class Game():
	def __init__(self, screen, item, keys):
		self.screen = screen
		self.item = item
		self.keys =keys
		self.clock = pygame.time.Clock()

		#self.map1(40,72)
		self.intro()



	def map1(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
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
					font = objects.Font('press "E" to collect the map and press "B" to open map', screen, 10)
					font.update()
					if keys[pygame.K_e]:
						item['map1'] = 'collected'
						font = objects.Font('collected map1', screen, 20)
						font.update()
					

						
							

			if item['map1'] != None and playerr.y <=  -3:
				self.map2(130, 124)
			elif playerr.y <= -3:
				font = objects.Font('collect map 1', screen, 20)
				font.update()
			"""

			HERE IS SOMTHING U NEED TO DO BOI
			_______________________________________
			________________________________________||||||||||||



			"""
			if playerr.x <= -3:
				self.map8(256-21, 50)
			if playerr.y >= (144-20) *2:
				self.map9(121, 0)	

			if pygame.Rect.colliderect(pygame.Rect(playerr.x, playerr.y, playerr.width*2, playerr.height*2), pygame.Rect(39*2,70*2, 32, 26)):

				if item['key'] != None:
					font = objects.Font('press "E" to enter it works only when u have the key', screen, 10)
					font.update()
					if keys[pygame.K_e]:
						self.ending()

				
			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:


				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)




			#game update
			pygame.display.flip()
		pygame.quit()

	def map2(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map2,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap2:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap2)

			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)




			#index update
			index = (index + 1) % 4

			if playerr.y >= (144 -20)*2:
				self.map1(111, 0)

			elif playerr.y <= -3:
				self.map3(130, 124)


			#game update
			pygame.display.flip()
		pygame.quit()

	def map3(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map3,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap2:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap2)

			if item['map2'] == None:
				objects.map2.update(screen)
				if pygame.Rect.colliderect(pygame.Rect(playerr.x, playerr.y, playerr.width*2, playerr.height*2), pygame.Rect(objects.map2.x, objects.map2.y, objects.map2.newwidth, objects.map2.newheight)):
					font = objects.Font('press "E" to collect the map and press "n" to open map', screen, 10)
					font.update()
					if keys[pygame.K_e]:
						item['map2'] = 'collected'
						font = objects.Font('collected map2!', screen, 20)
						font.update()


			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)

			#index update
			index = (index + 1) % 4

			if playerr.y >= (144 -20)*2:
				self.map2(111, 0)


			elif playerr.y <= -3:
				self.map4(100, 125)
			#game update
			pygame.display.flip()
		pygame.quit()


	def map4(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map4,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap4:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap4)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)

			#index update
			index = (index + 1) % 4

			if playerr.y >= (144 -20)*2:
				self.map3(111, 0)

			if playerr.x <= 0:
				self.map5(256-21, 50)


			#game update
			pygame.display.flip()
		pygame.quit()


	def map5(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map5,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap5:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap5)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)

			#index update
			index = (index + 1) % 4

			if playerr.x >= (256-20)*2:
				self.map4(0, 111)

			if playerr.y <= -3:
				self.map6(110, 125)


			#game update
			pygame.display.flip()
		pygame.quit()

	def map6(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map4,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap4:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap4)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)

			#index update
			index = (index + 1) % 4

			if playerr.y >= (144 -20)*2:
				self.map5(121, 0)

			if playerr.x <= -3:
				self.map7(256-21, 100)




			#game update
			pygame.display.flip()
		pygame.quit()


	def map7(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map7,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap7:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap7)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)

			#index update
			index = (index + 1) % 4

			if playerr.y >= (144 -20)*2:
				self.map8(121, 0)

			if playerr.x >= (256- 20) *2:
				self.map6(256-10, 100)

			#game update
			pygame.display.flip()
		pygame.quit()

	def map8(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map5,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap5:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap5)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)


			#index update
			index = (index + 1) % 4

			if playerr.x >= (256-20)*2:
				self.map1(0, 75)

			if playerr.y <= -3:
				self.map7(125, 115)

			if item['map3'] == None:
				objects.map3.update(screen)
				if pygame.Rect.colliderect(pygame.Rect(playerr.x, playerr.y, playerr.width*2, playerr.height*2), pygame.Rect(objects.map3.x, objects.map3.y, objects.map3.newwidth, objects.map3.newheight)):
					font = objects.Font('press "E" to collect the map and press "m" to open map', screen, 10)
					font.update()
					if keys[pygame.K_e]:
						item['map3'] = 'collected'
						font = objects.Font('collected map3!', screen, 20)
						font.update()

			#game update
			pygame.display.flip()
		pygame.quit()

	def map9(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map5,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap5:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap5)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)


			#index update
			index = (index + 1) % 4

			if playerr.x >= (256-20)*2:
				self.map10(0 , 70)

			if playerr.y <= -3:
				self.map1(75, 144-21)

			#game update
			pygame.display.flip()
		pygame.quit()

	def map10(self,x,y):
		x = x
		y = y
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#calling classes
		playerr = player.Playerclass(x*2, y*2, screen)


		#=== Game Loop ==== 
		while run:
			clock.tick(8)
			screen.blit(sprites.map10,(0,0))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False


			for i in objects.objectmap10:
				i.update(screen)

			#player udate
			playerr.update(index, objects.objectmap10)



			if item['map1'] != None:
				if keys[pygame.K_b]:
					objects.tresuremap1.update(screen)
			if item['map2'] != None:
				if keys[pygame.K_n]:
					objects.tresuremap2.update(screen)
			if item['map3'] != None:
				if keys[pygame.K_m]:
					objects.tresuremap3.update(screen)

			if item['key'] == None:
				objects.key.update(screen)
				if pygame.Rect.colliderect(pygame.Rect(playerr.x, playerr.y, playerr.width*2, playerr.height*2), pygame.Rect(objects.key.x, objects.key.y, objects.key.newwidth, objects.key.newheight)):
					font = objects.Font('press "E" to collect the Key', screen, 10)
					font.update()
					if keys[pygame.K_e]:
						item['key'] = 'collected'
						font = objects.Font('collected key!', screen, 20)
						font.update()
			#index update
			index = (index + 1) % 4

			if playerr.x <= -3:
				self.map9(256-21, 50)


			#game update
			pygame.display.flip()
		pygame.quit()



	def ending(self):
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		#=== Game Loop ==== 

		while run:
			clock.tick(0.5)
			screen.fill((7,24,33))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False

			screen.blit(sprites.ending[index], (256/2, 144/2))


			index = index+1

			pygame.display.flip()

		pygame.quit()



	def intro(self):
		run = True
		index = 0
		screen = self.screen
		keys = self.keys
		item = self.item
		clock = self.clock
		opacity = 2
		opacity_2 = 300
		#=== Game Loop ==== 

		while run:
			clock.tick(30)
			screen.fill((7,24,33))
			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				# Quit event
				if event.type == pygame.QUIT:
					run = False

			
			if opacity < 255:
				objects.mainmenu_backdrop.image.set_alpha(opacity,0)
				opacity += 4

			else:
				objects.mainmenu_backdrop.image.set_alpha(opacity_2, 0)
				opacity_2 -= 3 

			if opacity_2 < 0:
				self.map1(40,72)


			objects.mainmenu_backdrop.update(screen)

			pygame.display.flip()

		pygame.quit()