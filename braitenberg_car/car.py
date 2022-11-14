from math import sin
from math import cos
from math import pi

from utils import calculate_dist_major
from utils import calculate_dist


import pygame
from pygame.math import Vector2


black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 50,205,50





class Car:
    def __init__(self, x, y, width, height, radius, c=1e-3, lam=1/2, color=red) -> None:
        self.x1, self.y1 = x, y
        self.x2, self.y2 = (x+radius*2), y
        self.ant_x1, self.ant_y1 = self.x1, (self.y1 - radius)
        self.ant_x2, self.ant_y2 = self.x2, (self.y2 - radius) 
        self.c = c
        self.radius = radius
        self.dist_major = calculate_dist_major(width, height)
        self.lam = lam
        self.color = color
        

        self.distantia_between_wheels = x+radius*2
        self.width, self.height = width, height        
        
        self.radius = radius
        self.checK_position_and_correction()
        self.theta = 0

    def set_position_wheel1(self):
        self.theta += self.c * self.L2 * (self.lam)

        self.x2 = self.x1 + self.radius * 2 * sin(self.theta)
        self.y2 = self.y1 + self.radius * 2 * cos(self.theta)
        self.ant_x2 = self.x2 + self.radius * sin(self.theta+pi/2)
        self.ant_y2 = self.y2 + self.radius * cos(self.theta+pi/2)

        self.ant_x1 = self.x1 + self.radius * sin(self.theta+pi/2)
        self.ant_y1 = self.y1 + self.radius * cos(self.theta+pi/2)
    
    def set_position_wheel2(self):
        # checar si la velovidad es igual y si es igual duplicar velocidad
        self.theta -= self.c * self.L1 + self.L2 * (1-self.lam)
        self.x1 = self.x2 + self.radius * 2 * sin(self.theta)
        self.y1 = self.y2 + self.radius * 2 * cos(self.theta)
        self.ant_x1 = self.x1 + self.radius * sin(self.theta+pi/2)
        self.ant_y1 = self.y1 + self.radius * cos(self.theta+pi/2)

        self.ant_x2 = self.x2 + self.radius * sin(self.theta+pi/2)
        self.ant_y2 = self.y2 + self.radius * cos(self.theta+pi/2)
        

    def check_position_sun_wheel1(self, position_sun: Vector2):
        v1 = Vector2(self.x1, self.y1)
        self.L1 = self.dist_major / (calculate_dist(v1, position_sun) + 100)
    
    def check_position_sun_wheel2(self, position_sun: Vector2):
        v1 = Vector2(self.x2, self.y2)
        self.L2 = self.dist_major / (calculate_dist(v1, position_sun) + 100)


    def draw_car(self, screen, position_sun):
        self.checK_position_and_correction()
        
        
        # Left wheel
        pygame.draw.circle(screen, color=self.color, center=Vector2(self.x1, self.y1), radius=self.radius)
        # Right wheel
        pygame.draw.circle(screen, color=self.color, center=Vector2(self.x2, self.y2), radius=self.radius)
        
        # Left antenna
        pygame.draw.circle(screen, color=green, center=Vector2(self.ant_x1, self.ant_y1), radius=self.radius/5)
        # Right antenna
        pygame.draw.circle(screen, color=green, center=Vector2(self.ant_x2, self.ant_y2), radius=self.radius/5)
        self.check_position_sun_wheel2(position_sun)   
        self.set_position_wheel1()
        self.check_position_sun_wheel1(position_sun)
        self.set_position_wheel2()
        

        

    def checK_position_and_correction(self):
        pass
        # if self.x1 <= self.radius:
        #     self.x1 = self.radius
        # if self.x1 >= (self.width - self.radius):
        #     self.x1 = self.width - self.radius
        # if self.y1 <= self.radius:
        #     self.y1 = self.radius
        # if self.y1 >= (self.height - self.radius):
        #     self.y1 = self.height - self.radius