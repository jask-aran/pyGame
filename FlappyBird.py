import pygame
import sys


def drawFloor():
    screen.blit(floor_surface, (floor_xpos, 900))
    screen.blit(floor_surface, (floor_xpos + 576, 900))


# initialisation
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# import and scale background image
background = pygame.image.load('assets/background-day.png').convert()
background = pygame.transform.scale2x(background)

# import and scale floor image
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_xpos = 0

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    floor_xpos -= 1
    drawFloor()
    if floor_xpos <= -576:
        floor_xpos = 0

    pygame.display.update()
    clock.tick(120)
