import pygame, os, sys
from pygame.locals import *

from raspigame import *
from swarm import *
from player import *
from collision import *


class PlayGameState(GameState):
	
	def __init__(self, game, gameOverState):
		super(PlayGameState, self).__init__(game)
		self.controllers = None
		self.renderers = None
		self.player_controller = None
		self.player_controller2 = None
		self.gameOverState = gameOverState
		self.initialise()
		
	def onEnter(self, previousState):
		self.player_controller.pause(False)

	def initialise(self):
		

		self.player_controller = PlayerController(0, 540)
		player_renderer = PlayerView(self.player_controller, 'swordsman.png')
		lives_renderer = PlayerLivesView(self.player_controller, 'swordsman.png')
		bullet_renderer = BulletView(self.player_controller.bullets, 'sword.png')
		alienbullet_renderer = BulletView(self.player_controller.bullets, 'fireball.png')

		self.swarm_controller = PlayerController(0, 540)
		player2_renderer = Player2View(self.Player_controller2, 'mage.png')
		lives2_renderer = Player2LivesView(self.player_controller2, 'mage.png')
		bullet_renderer = BulletView(self.player_controller2.bullets, 'mage.png')
		alienbullet_renderer = BulletView(self.player_controller2.bullets, 'fireball.png')

		explosion_controller = ExplosionController(self.game)
		collision_controller = CollisionController(self.game, self.swarm_controller, self.player_controller, explosion_controller, self)

		explosion_view = ExplosionView(explosion_controller.list.explosions, 'explosion.png', 32, 32)

		self.renderers = [  bullet_renderer, lives_renderer, player_renderer, alienbullet_renderer, player2_renderer,lives2_renderer, explosion_view ]
		self.controllers = [ self.player_controller2, self.player_controller, collision_controller, explosion_controller ]

	def update(self, gameTime):
		for ctrl in self.controllers:
			ctrl.update(gameTime)	
			
		if ( self.player_controller.model.lives == 0 ):
			self.game.changeState( self.gameOverState )
			
		if ( self.player_controller2.model.lives == 0):

			levelUpMessage = InterstitialState( invadersGame, 'player 1 wins ', 2000, self )

	def draw(self, surface):
		for view in self.renderers:
			ctrl.update(gameTime)
