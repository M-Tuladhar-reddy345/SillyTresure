#Imports
import pygame
import sprites
import objects as ob

class Playerclass(object):
	"""Playerclass 
	x, y, = pos
	screen = where to blit
	"""
	def __init__(self, x, y, screen):
		self.x = x
		self.y = y
		self.screen = screen
		self.left = False
		self.right= False
		self.down = True
		self.up = False
		self.last = 'down'
		self.width = 15
		self.height = 20
		self.canmove = True


	def update(self, index, objects):
		self.keys = pygame.key.get_pressed()
		#movement
		#move down
		if self.keys[pygame.K_DOWN]:
			self.left = False
			self.right= False
			self.down = True
			self.up = False
			self.last = 'down'
			index = (index + 1) % 4

			if self.y <= (144 - 20)*2 and self.canmove:
				self.y += 8
			for i in objects:
				if pygame.Rect.colliderect(pygame.Rect(self.x, self.y, self.width*2, self.height*2), pygame.Rect(i.x, i.y, i.newwidth, i.newheight)):
					self.y -=8
					continue



		#move left		
		elif self.keys[pygame.K_LEFT]:
			self.left = True
			self.right= False
			self.down = False
			self.up = False
			self.last = 'left'
			self.index = (index + 1) % 4 
			if self.x >= 0  and self.canmove:
				self.x -= 8
			for i in objects:
				if pygame.Rect.colliderect(pygame.Rect(self.x, self.y, self.width*2, self.height*2), pygame.Rect(i.x, i.y, i.newwidth, i.newheight)):
					self.x += 8
					continue


		#moveright
		elif self.keys[pygame.K_RIGHT]:
			self.left = False
			self.right= True
			self.down = False
			self.up = False
			self.last = 'right'
			index = (index + 1) % 4
			if self.x <= (256- 12)*2 and self.canmove:
				self.x += 8
			for i in objects:
				if pygame.Rect.colliderect(pygame.Rect(self.x, self.y, self.width*2, self.height*2), pygame.Rect(i.x, i.y, i.newwidth, i.newheight)):
					self.x -= 8
					continue



		#moveup
		elif self.keys[pygame.K_UP] :
			self.left = False
			self.right= False
			self.down = False
			self.up = True
			self.last = 'up'
			index = (index + 1) % 4
			if self.y >= -3 and self.canmove:
				self.y -= 8
			for i in objects:
				if pygame.Rect.colliderect(pygame.Rect(self.x, self.y, self.width*2, self.height*2), pygame.Rect(i.x, i.y, i.newwidth, i.newheight)):
					if i.objectname =='sb':
						self.font = ob.Font('Unkown ruins', self.screen, 20)
						self.font.update()

					self.y +=8


		#if no move
		else: 
			#self.left = False
			#self.right= False
			#self.down = True
			#self.up = False
			index = 0

		#bliting according to the condition

		if self.down and self.last == 'down':
			self.image = sprites.moveforward[index]
	
		elif self.right and self.last == 'right':
			self.image = sprites.moveright[index]
			
		elif self.up and self.last == 'up':
			self.image = sprites.moveback[index]

		elif  self.left and self.last == 'left':
			self.image = sprites.moveleft[index]
		self. image = pygame.transform.scale(self.image, (self.width*2, self.height*2)) 

		self.image.convert_alpha()
		self.rect = self.image.get_rect()


		self.screen.blit(self.image, (self.x, self.y))


