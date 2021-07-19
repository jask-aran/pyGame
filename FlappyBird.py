import pygame
import sys


def drawFloor():
    screen.blit(floorSurface, (floor_xpos, 900))
    screen.blit(floorSurface, (floor_xpos + 576, 900))


# initialisation
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# import and scale background image
background = pygame.image.load('assets/background-day.png').convert()
background = pygame.transform.scale2x(background)
background_xpos = 0

# import and scale floor image
floorSurface = pygame.image.load('assets/base.png').convert()
floorSurface = pygame.transform.scale2x(floorSurface)
floor_xpos = 0

birdSurface = pygame.image.load('assets/bluebird-midflap.png').convert()
birdSurface = pygame.transform.scale2x(birdSurface)
birdRect = birdSurface.get_rect(center=(100, 512))

# Game Variables
gravity = 0.25
birdMovement = 0

# primary game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # force end
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdMovement = 0
                birdMovement -= 8

    screen.blit(background, (0, 0))

    birdMovement += gravity
    birdRect.centery += birdMovement
    screen.blit(birdSurface, birdRect)

    floor_xpos -= 1
    drawFloor()
    if floor_xpos <= -576:
        floor_xpos = 0

    pygame.display.update()
    clock.tick(120)
