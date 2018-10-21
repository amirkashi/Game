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
        self.helicopter_velocity = 1
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.keys = [False, False]
        self.air_plane_location_begin = [225, 650]
        self.air_plane_location_during_game = [0, 0]
        self.rockets_positions = []
        self.helicopter_draw_position = [[100, 20]]
        self.air_plane = pygame.image.load("files/airplane.png")
        self.sky = pygame.image.load("files/sky.gif")
        self.rocket = pygame.image.load("files/bomb.png")
        self.helicopter_1 = pygame.image.load("files/heli.png")
        self.helicopter_2 = self.helicopter_1

    def create_background(self):
        for x in range(self.WIDTH / self.sky.get_width() + 1):
            for y in range(self.HEIGHT / self.sky.get_height() + 1):
                self.screen.blit(self.sky, (x * 200, y * 200))

    def move_rockets(self):
        for rocket_position in self.rockets_positions:
            index = 0
            rocket_position[2] -= self.rocket_velocity
            if rocket_position[2] < -100 or 1000 < rocket_position[2]:
                self.rockets_positions.pop(index)
            index += 1
        for rocket_position in self.rockets_positions:
            self.screen.blit(self.rocket, (rocket_position[1], rocket_position[2]))

    def helicopter_time_release(self):
        if self.helicopter_draw_time == 0:
            self.helicopter_draw_position.append([random.randint(self.WIDTH // 10, self.WIDTH-self.WIDTH//10), 0])
            self.helicopter_draw_time = self.helicopter_elapse_time

    def start_the_game(self):
        print("Welcome!")
        print("z move to the left")
        print("c move to the right")
        print("q to quit the game")
        print("left click to shoot")
        pygame.init()
        while 1:
            self.create_background()
            self.screen.blit(self.air_plane, self.air_plane_location_begin)
            self.move_rockets()
            self.helicopter_time_release()
            index_helicopter = 0
            for helicopter_position in self.helicopter_draw_position:
                helicopter_position[1] += self.helicopter_velocity
                helicopter_rectangle = pygame.Rect(self.helicopter_2.get_rect())
                helicopter_rectangle.top = helicopter_position[1]
                helicopter_rectangle.left = helicopter_position[0]
                index_rocket = 0
                for rocket_position in self.rockets_positions:
                    rocket_rectangle = pygame.Rect(self.rocket.get_rect())
                    rocket_rectangle.top = rocket_position[1]
                    rocket_rectangle.left = rocket_position[2]
                    if helicopter_rectangle.colliderect(rocket_rectangle):
                        self.air_plane_location_begin[0] += 1
                        self.helicopter_draw_position.pop(index_helicopter)
                        self.rockets_positions.pop(index_rocket)
                index_helicopter += 1
                index_rocket += 1
            for helicopter_position in self.helicopter_draw_position:
                self.screen.blit(self.helicopter_1, helicopter_position)
            self.helicopter_draw_time -= 1
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_z:
                        self.keys[0] = True
                    elif event.key == K_c:  
                        self.keys[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_z:
                        self.keys[0] = False
                    elif event.key == pygame.K_c:
                        self.keys[1] = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        print("Thanks for playing")
                        exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self.air_plane_location_during_game[1] += 1
                    self.rockets_positions.append([math.atan2(mouse_position[1]-(self.air_plane_location_begin[1]+70), 
                                    mouse_position[0]-(self.air_plane_location_begin[0])), 
                                    self.air_plane_location_begin[0]+70, self.air_plane_location_begin[1]+70])
            if self.keys[0]:
                self.air_plane_location_begin[0] -= 2
            elif self.keys[1]:
                self.air_plane_location_begin[0] += 2
            
