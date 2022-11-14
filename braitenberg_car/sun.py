from math import sin
from math import cos
from math import pi
import pygame
from pygame.math import Vector2


black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 50, 205, 50
yellow = 255, 255, 0



class Sun:
    def __init__(self, x_sun, y_sun, radius_sun) -> None:
        self.x_sun, self.y_sun = x_sun, y_sun
        
        self.radius_sun = radius_sun


    def draw_sun(self, screen):
        
        # Left wheel
        pygame.draw.circle(screen, color=yellow, center=Vector2(self.x_sun, self.y_sun), radius=self.radius_sun)
    
    def vector(self):
        return Vector2(self.x_sun, self.y_sun)

    def set_coord(self, x_sun, y_sun):
        self.x_sun, self.y_sun = x_sun, y_sun

        

