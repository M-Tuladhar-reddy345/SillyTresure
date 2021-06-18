#imports

import pygame


#load sprite images // Data
moveforward = [pygame.image.load('data/player/moveforward/moveforward0.png'),
				pygame.image.load('data/player/moveforward/moveforward1.png'),
				pygame.image.load('data/player/moveforward/moveforward2.png'),
				pygame.image.load('data/player/moveforward/moveforward3.png'),
]
moveback = [pygame.image.load('data/player/mainback/moveback0.png'),
				pygame.image.load('data/player/mainback/moveback1.png'),
				pygame.image.load('data/player/mainback/moveback2.png'),
				pygame.image.load('data/player/mainback/moveback3.png'),
]
moveleft = [pygame.image.load('data/player/mainleft/moveleft0.png'),
			pygame.image.load('data/player/mainleft/moveleft1.png'),
			pygame.image.load('data/player/mainleft/moveleft2.png'),
			pygame.image.load('data/player/mainleft/moveleft0.png'),
]

moveright =[pygame.image.load('data/player/mainright/moveright0.png'),
			pygame.image.load('data/player/mainright/moveright1.png'),
			pygame.image.load('data/player/mainright/moveright2.png'),
			pygame.image.load('data/player/mainright/moveright0.png'),
]

ancientmap1 = pygame.transform.scale(pygame.image.load('data/maps/map1.png'), (256*2, 144*2))
map2 = pygame.transform.scale(pygame.image.load('data/maps/map2.png'), (256*2, 144*2))


signboard = pygame.image.load('data/objects/signboard.png')
ar1 = pygame.image.load('data/objects/anceintruin1.png')
ar2 = pygame.image.load('data/objects/anceintruin2.png')
ar3 = pygame.image.load('data/objects/anceintruin3.png')
s1 = pygame.image.load('data/objects/statue1.png')
b1 = pygame.image.load('data/objects/bush1.png')
b2 = pygame.image.load('data/objects/bush2.png')
b3 = pygame.image.load('data/objects/map1/bush3.png')
trees = pygame.image.load('data/objects/map1/tree.png')
treemap21 =  pygame.image.load('data/objects/map2/tree1.png')
treemap22 =  pygame.image.load('data/objects/map2/tree2.png')
map1 = pygame.image.load('data/objects/map.png')


tresuremap1 = pygame.image.load('data/tresuremaps/map1.png')