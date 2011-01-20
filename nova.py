#!/usr/bin/env python

import pygame
from pygame.locals import *

def circle():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    screen = pygame.display.get_surface()
    black = (0,0,0)
    white = (255,255,255)
    
    while True:
	for event in pygame.event.get():
	    if event.type == MOUSEBUTTONDOWN and event.button == 1:
		origin = pygame.mouse.get_pos()
	    if event.type == MOUSEMOTION and event.buttons[0] == 1:
		pos = pygame.mouse.get_pos()
		rad = abs(origin[0] - pos[0])
		screen.fill(black)
	        pygame.draw.circle(screen, white, origin, rad)
		pygame.display.flip()

