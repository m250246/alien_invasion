#!/usr/bin/env python
# coding: utf-8

class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        
        """Initialize the game's settings"""
        # Screen settings 
        self.sWidth = 1200
        self.sHeight = 800
        self.sBackground = (230,230,230)

        # Ship settings
        self.vShip = 1.5

        # Bullet settings
        self.vBullet = 1.0
        self.bWidth = 3
        self.bHeight= 15
        self.bColor = (10, 10, 60)
        self.bAllowed = 3
        
        # Alien settings
        self.vAlien = 1.0
        self.vFleet = 10
        self.fDirection = 1