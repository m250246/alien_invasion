#!/usr/bin/env python
# coding: utf-8
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screenSize = game.screen.get_rect()
        
        # Load the ship image and get its pos.
        self.image = pygame.image.load('Images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (100,150))
        self.pos = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.pos.midbottom = self.screenSize.midbottom
        
        # STore a decimal value for the ship's horizontal position.
        self.x = float(self.pos.x)
        # Movement Flag
        self.moveR = False
        self.moveL = False
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moveR and self.pos.right < self.screenSize.right:
            self.x += self.settings.vShip
        if self.moveL and self.pos.left > 0:
            self.x -= self.settings.vShip
        
        # Update pos object from self.x.
        self.pos.x = self.x
    def moveShip(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.pos)