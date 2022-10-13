#!/usr/bin/env python
# coding: utf-8

import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bColor
        
        # Create a bullet pos at (0,0) and then set correct position
        self.pos = pygame.Rect(0, 0, self.settings.bWidth, self.settings.bHeight)
        self.pos.midtop = game.ship.pos.midtop
        
        # Store the bullet's position as a decimal value
        self.y = float(self.pos.y)
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.vBullet
        # Update the position.
        self.pos.y = self.y
        
    def drawB(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.pos)