from math import sqrt

from pygame import Vector2




def calculate_dist(v1: Vector2, v2: Vector2) -> float:
    x1, y1 = v1
    x2, y2 = v2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def calculate_dist_major(width, height):
    return sqrt(width**2 + height**2)