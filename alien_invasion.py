#!/usr/bin/env python
# coding: utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((self.settings.sWidth, self.settings.sHeight))
        self.settings.sWidth = self.screen.get_rect().width
        self.settings.sHeight = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.fleet()
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self.events()
            self.ship.update()
            self.bUpdate()
            self.aUpdate()
            self.newScreen()
    def bUpdate(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
            # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.pos.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens. Get rid of the bullet and alien.
        #collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
    def aUpdate(self):
        """Update the positions of all aliens in the fleet."""
        self.fEdges()
        self.aliens.update()
    def fEdges(self):
        """Respond appropriately if any a lines have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.edges():
                self.moveFleet()
                break
    def moveFleet(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.pos.y += self.settings.vFleet
        self.settings.fDirection *= -1
    def events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown(event)
            elif event.type == pygame.KEYUP:
                self.keyup(event)
    def keydown(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moveR = True
        elif event.key == pygame.K_LEFT:
            self.ship.moveL = True
        elif event.key == pygame.K_z:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire()
    def keyup(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moveR = False
        elif event.key == pygame.K_LEFT:
            self.ship.moveL = False
    def fire(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bAllowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def fleet(self):
        """Create the fleet of aliens."""
        new_alien = Alien(self)
        aWidth, aHeight = new_alien.pos.size
        spaceX = self.settings.sWidth - (2*aWidth)
        alienNum = spaceX // (2* aWidth)

        # Determine the number of rows of aliens that fit on the screen.
        shipH = self.ship.pos.height
        spaceY = (self.settings.sHeight - (3*aHeight) - shipH)
        rows = spaceY // (2*aHeight)

        # Create the full fleet of aliens.
        for row in range(rows):
            for num in range(alienNum):
                self.makeAlien(num, row)
    def makeAlien(self, num, row):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        aWidth, aHeight = new_alien.pos.size
        new_alien.x = aWidth + (2*aWidth*num)
        new_alien.pos.x = new_alien.x
        new_alien.pos.y = aHeight = (2*aHeight*row)
        self.aliens.add(new_alien)
    def newScreen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.sBackground)
        self.ship.moveShip()
        for bullet in self.bullets.sprites():
            bullet.drawB()
        for alien in self.aliens.sprites():
            alien.drawA()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    alienI = AlienInvasion()
    alienI.run_game()
