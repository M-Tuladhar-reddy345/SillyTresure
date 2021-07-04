#Imports
import pygame 
import player
import sprites
import objects
import time
import os
from game import Game

# configs
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((256 *2,144*2))
clock = pygame.time.Clock()

item = {'map1':None, 'map2':None, "map3":None, 'key':None}
keys = pygame.key.get_pressed()

#backround = pygame.mixer.music.load(os.path.join('data', 'music.wav'))
#backround.music.play(-1)


Game(screen,item, keys)
	

                                                                                                                                                                                          

