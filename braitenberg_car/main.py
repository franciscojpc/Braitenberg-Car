from car import Car
from sun import Sun

from random import randint

import pygame


pygame.init()

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 50,205,50

def run():
    game_over = False
    screen_size = width, height = 1000, 800
    
    
    radius = 20
    c = 1e-5
    lam = .5
    car = Car(
        randint(0, width),
        randint(0, height),
        width, height,
        radius=radius,
        c=c,
        lam=lam,
        color=green

        )

    car2 = Car(
        randint(0, width),
        randint(0, height),
        width, height,
        radius=radius,
        c=c,
        lam=lam,
        color=red

        )
    x_sun, y_sun = randint(0, width), randint(0, width)
    radius_sun = 40
    sun = Sun(x_sun, y_sun, radius_sun)
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)
    
    pygame.display.set_caption('Braitenberg Car')
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(white)
        mouse_pos = pygame.mouse.get_pos()
        x_sun = mouse_pos[0]
        y_sun = mouse_pos[1]

        sun.set_coord(x_sun, y_sun)   

        sun.draw_sun(screen=screen)

        car.draw_car(screen=screen, position_sun=sun.vector())
        car2.draw_car(screen=screen, position_sun=sun.vector())

        pygame.display.flip()
        # car.set_position(
        #     randint(0, width),
        #     randint(0, height),
        # )
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    
    run()