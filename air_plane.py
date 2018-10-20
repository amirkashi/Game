import pygame
from pygame.locals import *
import random
import os
import pygame.mixer
import pygame.time
import math


class AirPlane():
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 800
        self.rocket_velocity = 10
        self.HELICOPTER_DRAW_TIME = 100
        self.HELICOPTER_ELAPSE_TIME = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.keys = [False, False]
        self.initial_air_plane_location = [225, 650]
        self.air_plane_locations = [0, 0]
        self.rockets_positions = []
        self.helicopter_draw_position = [[100, 20]]
        self.air_plane = pygame.image.load("files/airplane.png")
        self.sky = pygame.image.load("files/sky.gif")
        self.rocket = pygame.image.load("files/bomb.png")
        self.helicopter_1 = pygame.image.load("files/heli.png")
        self.helicopter_2 = helicopter_1
        
