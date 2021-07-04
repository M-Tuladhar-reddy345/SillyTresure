import pygame
import time
import sprites

class Object(object):
	def __init__(self, x, y, objectname, img):

		self.image = img
		self.rect = self.image.get_rect()

		self.x = x
		self.y = y
		self.width = self.rect.width
		self.height = self.rect.height

		self.objectname = objectname

	def update(self,screen):
		if self.objectname != 'tresuremap':
			self.image = pygame.transform.scale(self.image, (self.width*2, self.height*2)) 
			self.rect = self.image.get_rect()
			self.newwidth = self.rect.width
			self.newheight = self.rect.height



		screen.blit(self.image, (self.x, self.y))


class Font():
	"""docstring for Font"""
	def __init__(self, text, screen, size):
		self.text = text
		self.size = size
		self.screen =screen

	def update(self):
		font = pygame.font.Font("data/text.ttf", self.size)
		text = font.render(self.text,False, (224,248,207))
		rect = pygame.draw.rect(self.screen, (7,24,33), pygame.Rect(10, 100*2, 256*2-20,44*2))
		self.screen.blit(text, (10+30 ,100*2+20))




objectmap1 = []
objectmap1.append(Object(170*2, -2, "s1", sprites.s1))
objectmap1.append(Object(256/2, (144/2), "sb", sprites.signboard))
objectmap1.append(Object(0+2, 0+2, "ar1", sprites.ar1))
objectmap1.append(Object((108*2)-4, (96*2)+13, "ar2", sprites.ar2))
objectmap1.append(Object(11*2, 100*2, "ar3", sprites.ar3))
objectmap1.append(Object((137*2)-2, (3*2)-3, 'b3', sprites.b3))
objectmap1.append(Object(170*2, 0, 'trees', sprites.trees))

objectmap2 = []
objectmap2.append(Object(0,0, "t1",sprites.treemap21))
objectmap2.append(Object(178*2,14*2, "t2",sprites.treemap22))


objectmap4 = []
objectmap4.append(Object(-14*2,-45*2,"t2" ,sprites.tree41))
objectmap4.append(Object(170*2,164*2,"t2" ,sprites.tree42))

objectmap5 = []
objectmap5.append(Object(0,0,"t2" ,sprites.tree51))
objectmap5.append(Object(125*2,80*2,"t2" ,sprites.tree52))

objectmap7 = []
objectmap7.append(Object(0,0,'t2', sprites.tree71))
objectmap7.append(Object(0,75*2,'t2', sprites.tree72))


objectmap10 = []
objectmap10.append(Object(0+3,0,'t2', sprites.tree101))
objectmap10.append(Object(0,90*2,'t2', sprites.tree102))
objectmap10.append(Object(160*2,73*2 , "sb2", sprites.signboard))

map1 = Object(100*2,65*2, "map",sprites.map1)
map2 = Object(111*2,65*2, "map",sprites.map1)
map3 = Object(111*2,65*2, "map",sprites.map1)


tresuremap1 = Object( 10*2, 10*2, "tresuremap", sprites.tresuremap1)
tresuremap2 = Object( 0, 10*2, "tresuremap", sprites.tresuremap2)
tresuremap3 = Object( 10*20, 10*2, "tresuremap", sprites.tresuremap3)
tresuremap4 = Object( 10*20, 10*2, "tresuremap", sprites.tresuremap4)

key =  Object( 158*2,73*2, "key", sprites.key)

mainmenu_backdrop = Object(0,0, 'backdrop', sprites.mainpage)

for i in objectmap1:
	print(i.objectname)