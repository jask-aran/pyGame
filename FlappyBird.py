import pygame
import sys

# initialisation
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# import background
backgroundSurface = pygame.image.load('assets/background-day.png').convert()
backgroundSurface = pygame.transform.scale2x(backgroundSurface)

# import floor
floorSurface = pygame.image.load('assets/base.png').convert()
floorSurface = pygame.transform.scale2x(floorSurface)
floor_xpos = 0

birdSurface = pygame.image.load('assets/bluebird-midflap.png').convert()
birdSurface = pygame.transform.scale2x(birdSurface)
birdRect = birdSurface.get_rect(center=(100, 512))

# Game Variables
gravity = 0.25
birdMovement = 0


# move the floor
def drawFloor():
    screen.blit(floorSurface, (floor_xpos, 900))
    screen.blit(floorSurface, (floor_xpos + 576, 900))


# primary game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # force end
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # jump on spacebar press
            if event.key == pygame.K_SPACE:
                birdMovement = 0
                birdMovement -= 8
    # draw floor on screen
    screen.blit(backgroundSurface, (0, 0))

    # pull bird down per frame
    birdMovement += gravity
    birdRect.centery += birdMovement
    screen.blit(birdSurface, birdRect)

    # moove the floor back to the start when it leaves the screen
    floor_xpos -= 1
    drawFloor()
    if floor_xpos <= -576:
        floor_xpos = 0

    # tick rate
    pygame.display.update()
    clock.tick(120)

# watch this shit
