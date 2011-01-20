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

	left = origin[0] - radius
	top = origin[1] + radius
	width = height = radius*2
	self.rect = pygame.Rect(left, top, width, height)

    def draw(self):
	self.screen.fill((0, 0, 0), rect=self.rect)
	pygame.draw.circle(self.screen, self.color, self.origin, self.radius)
	pygame.display.update(self.rect)

def test():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    screen = pygame.display.get_surface()
    black = (0,0,0)
    white = (255,255,255)
    circles = []

    while True:
	for event in pygame.event.get():
	    if event.type == MOUSEBUTTONDOWN and event.button == 1:
		origin = pygame.mouse.get_pos()
		radius = 1
		circle = Circle(screen, origin, radius)
	    if event.type == MOUSEMOTION and event.buttons[0] == 1:
		pos = pygame.mouse.get_pos()
		circle.radius = abs(origin[0] - pos[0])
		circle.draw()
	    if event.type == MOUSEBUTTONUP and event.button == 1 and circle:
		circles.append(circle)
		circle = False

	for circle in circles:
	    circle.draw()

