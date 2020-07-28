background = 'img/ecity.png'
satellite = 'img/lance.png'
icon = "img/icon.png"

import pygame
from pygame.locals import *

# Setting the Basic values
pygame.init()
clock = pygame.time.Clock()
SCREEN_SIZE = (1200, 500)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Pokemon")
background_image = pygame.image.load(background).convert()
satellite_image = pygame.image.load(satellite).convert_alpha()
title = pygame.image.load(icon).convert()
pygame.display.set_icon(title)
lance = pygame.transform.scale2x(satellite_image)
pause=False
#Create an event for F key fullscreen :
counter_fullscreen=0
# Define the rectangle for collision detection
# 1)Burned Tower 2)Big Main Rectangle
burned_tower = Rect((262, 108), (165,108))
main_rectangle=Rect((251,254),(565,600))
