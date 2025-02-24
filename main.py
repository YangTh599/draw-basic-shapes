import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *

def init_game():
    pygame.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window, shapes):
    window.fill(WHITE) # 15
    
    for shape in shapes:
        shape.draw()


    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    window = init_game()
    clock = pygame.time.Clock()

    run = True

    l = Line(window, THANOS, [10,10], [50,50], 5)
    rectangle1 = Rectangle(window, COTTON_CANDY, 90,90,100,200)
    c1 = Circ(window, (400,500),  LIME, 50, 10)

    shapes = [l,rectangle1,c1]

    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # QUIT
        #         run = False
        #         break
        
        draw(window, shapes) # UPDATES SCREEN


    pygame.quit()
    quit()

class Line():

    def __init__(self,window, color, start_coord, end_coord, width):
        self.window = window
        self.color = color
        self.start = start_coord
        self.end = end_coord
        self.width = width

    def draw(self):
        pygame.draw.line(self.window,self.color, self.start, self.end, self.width)

class Rectangle():

    def __init__(self, window, color, x, y ,width=1, length=1, line_width=0):
        self.rect = pygame.Rect(x,y,width,length)
        self.window = window
        self.color = color
        self.line_width = line_width

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect, self.line_width)

class Circ():
    
    def __init__(self, window, center_coords, color, radius, width=0):
        self.window = window
        self.color = color
        self.center = center_coords
        self.r = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.center, self.r, self.width)


if __name__ == "__main__": 
    main()

