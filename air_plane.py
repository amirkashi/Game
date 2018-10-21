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
        self.helicopter_draw_time = 100
        self.helicopter_elapse_time = 100
        self.rocket_velocity = 10
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

    def create_background(self):
        for x in range(self.WIDTH / sky.get_width() + 1):
            for y in range(self.HEIGHT / sky.get_height() + 1):
                screen.blit(self.sky, (x * 200, y * 200))

    def move_rockets(self):
        for rocket_position in self.rockets_positions:
            index = 0
            rocket_position[2] -= self.rocket_velocity
            if rocket_position[2] < -100 or 1000 < rocket_position[2]:
                self.rockets_positions.pop(index)
            index += 1
        for rocket_position in self.rockets_positions:
            screen.blit(self.rocket, (rocket_position[1], rocket_position[2]))

    def make_helicopter(self):
        if self.helicopter_draw_time == 0:
            self.helicopter_draw_position.append([random.randint(self.WIDTH // 10, self.WIDTH-self.WIDTH//10), 0])
            self.helicopter_draw_time = self.helicopter_elapse_time


