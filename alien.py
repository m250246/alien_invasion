import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        # Load the alien image and set its pos attribut.
        self.image = pygame.image.load('Images/alien.bmp')
        self.pos = self.image.get_rect()
        #self.pos = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.pos.x = self.pos.width
        self.pos.y = self.pos.height
        # Store the alien's exact horizontal position.
        #self.rect = self.pos
        self.x = float(self.pos.x)
        
    def edges(self):
        """Return True if alien is at edge of screen."""
        screen = self.screen.get_rect()
        if self.pos.right >= screen.right or self.pos.left <= 0:
            return True
        
    def update(self):
        """Move an alien to the right."""
        self.x += (self.settings.vAlien * self.settings.fDirection)
        self.pos.x = self.x
        
    def drawA(self):
        self.screen.blit(self.image, self.pos)
        

        