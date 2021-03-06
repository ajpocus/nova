#!/usr/bin/env python

# nova.py: a pygame demo which draws circles
# Copyright 2011 Austin Pocus, see LICENSE for details

# TODO: - write circle class
#	- distill main logic into functions, possible circle methods
#	- modify main logic to change properties of circle
#	- upon mousebuttonup[0], save circle to permanent list

import pygame
from pygame.locals import *

class Circle:
    def __init__(self, screen, origin, radius):
	self.screen = screen
	self.origin = origin
	self.radius = radius
	if radius < 100:
	    self.color = (255, 0, 0)	# red
	elif radius < 300:
	    self.color = (255, 255, 0)	# yellow
	else:
	    self.color = (0, 0, 255)	# blue

    def rect(self):
	left = self.origin[0] - self.radius
	top = self.origin[1] + self.radius
	width = height = self.radius * 2
	self.rect = pygame.Rect(left, top, width, height)

def test():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    screen = pygame.display.get_surface()
    black = (0,0,0)
    white = (255,255,255)
    circles = []
    circle = None

    while True:
	try:
	    circle
	except NameError:
	    circle = False

	for event in pygame.event.get():
	    if event.type == MOUSEBUTTONDOWN and event.button == 1:
		origin = pygame.mouse.get_pos()
		circle = Circle(screen, origin, radius=1)

	    if event.type == MOUSEMOTION and event.buttons[0] == 1:
		pos = pygame.mouse.get_pos()
		circle.radius = abs(origin[0] - pos[0])
		screen.fill(black)
		for c in circles:
		    pygame.draw.circle(screen, c.color, c.origin, c.radius)
		pygame.draw.circle(screen, circle.color,
				    circle.origin, circle.radius)
		pygame.display.flip()

	    if event.type == MOUSEBUTTONUP and event.button == 1 and circle:
		circles.append(circle)
		circle = False

	for c in circles:
	    screen.fill(black)
	    pygame.draw.circle(screen, c.color, c.origin, c.radius)
	    pygame.display.flip()
