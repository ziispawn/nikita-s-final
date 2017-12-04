import pygame, os, sys
from pygame.locals import *

from bullet import *
from bitmapfont import *

"""
----------------------------------------------------------------------------------------------------
PlayerModel

The player model.
----------------------------------------------------------------------------------------------------
"""

class PlayerModel2:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.lives = 3
		self.score = 0
		self.speed = 100 # pixels per second

"""
----------------------------------------------------------------------------------------------------
Player
							
The tank at the bottom of the screen.
----------------------------------------------------------------------------------------------------
"""
class PlayerController2:
	
	def __init__(self, x, y):
		self.model = PlayerModel2(x, y)
		# self.x = x
		# self.y = y
		self.isPaused = False
		# self.lives = 3
		# self.score = 0
		# self.speed = 100 # pixels per sec
		self.bullets = BulletController(-200) # pixels per sec
		
	def pause(self, isPaused):
		self.isPaused = isPaused
		
	def update(self, gameTime):
		
		self.bullets.update(gameTime)
		
		if ( self.isPaused ):
			return
		
		keys = pygame.key.get_pressed()
		
		if (keys[K_d] and self.model.x < 800 - 32):
				self.model.x += 2
		elif (keys[K_a] and self.model.x > 0):
				self.model.x -= 2 
		elif (keys[K_s] and self.model.x < 800 - 32):
				self.model.y += 2 
		elif (keys[K_w] and self.model.x > 0):
				self.model.y -= 2 		
				
		if (keys[K_LSHIFT] and self.bullets.canFire()):
			x = self.model.x + 9 # bullet is 8 pixels
			y = self.model.y + 16
			self.bullets.addBullet(x, y)
			
	def hit(self, x, y, width, height):
		return (x >= self.model.x and y >= self.model.y and x + width <= self.model.x + 32 and y + height <= self.model.y + 32)

"""
----------------------------------------------------------------------------------------------------
"""
		
class Player2View:
	
	def __init__(self, player, imgpath):
		self.player = player
		self.image = pygame.image.load("mage.png")
		
	def render(self, surface):
		surface.blit(self.image, (self.player.model.x, self.player.model.y, 32, 32))


"""
----------------------------------------------------------------------------------------------------
PlayerLivesView
				
Renders the number of lives left for the player.
----------------------------------------------------------------------------------------------------
"""
class Player2LivesView:
	
	def __init__(self, player, imgpath):
		self.player = player
		self.image = pygame.image.load("mage.png")
		self.font = BitmapFont('fasttracker2-style_12x12.png', 12, 12)
		
	def render(self, surface):
		
		x = 8
		
		for life in range(0, self.player.model.lives):
			surface.blit(self.image, (x, 8, 32, 32))
			x += 40
			
		self.font.draw(surface, '1UP SCORE: ' + str(self.player.model.score), 160, 12)
		

if ( __name__ == '__main__'):
	
	pygame.init()
	fpsClock = pygame.time.Clock()
	
	surface = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Player Test');
	black = pygame.Color(0, 0, 0)
	
	player2 = PlayerController2(0, 400)
	player2View = Player2View(player2, 'mage.png')
	player2LivesView = Player2LivesView(player2, 'mage.png')
	
	while True:		
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		player2.update(fpsClock.get_time())
	
		surface.fill(black)
		player2View.render(surface)
		player2LivesView.render(surface)
		
		pygame.display.update()
		fpsClock.tick(30)

