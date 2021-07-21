import pygame
import sys
import random

# initialisation
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
font = pygame.font.Font('04b_19.ttf', 40)

# move the floor


def drawFloor():
    screen.blit(floorSurface, (floor_xpos, 900))
    screen.blit(floorSurface, (floor_xpos + 576, 900))


def pipeCreate():
    pipeRandom = random.choice(pipeheight)
    pipeTop = pipeSurface.get_rect(midtop=(700, pipeRandom))
    pipeBottom = pipeSurface.get_rect(midbottom=(700, pipeRandom - 300))
    return pipeTop, pipeBottom


def pipeMove(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def pipeDraw(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipeSurface, pipe)
        else:
            pipeFlip = pygame.transform.flip(pipeSurface, False, True)
            screen.blit(pipeFlip, pipe)


def collision(pipes):
    for pipe in pipes:
        if birdRect.colliderect(pipe):
            return False
    if birdRect.top <= -100 or birdRect.bottom >= 900:
        return False

    return True


def rotateBird(bird):
    rotatedBird = pygame.transform.rotozoom(bird, -birdMovement * 3, 1)
    return rotatedBird


def birdAnimation():
    newBird = bird_frames[birdIndex]
    newBirdRect = newBird.get_rect(center=(100, birdRect.centery))
    return newBird, newBirdRect


def scoreDisplay():
    scoreSurface = font.render('Score', True, (255, 255, 255))


# import texture
endText = pygame.image.load('assets/suck.png').convert()

# import background
backgroundSurface = pygame.image.load('assets/background-day.png').convert()
backgroundSurface = pygame.transform.scale2x(backgroundSurface)

# import floor
floorSurface = pygame.image.load('assets/base.png').convert()
floorSurface = pygame.transform.scale2x(floorSurface)
floor_xpos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load(
    'assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load(
    'assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load(
    'assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
birdIndex = 0
birdSurface = bird_frames[birdIndex]
birdRect = birdSurface.get_rect(center=(100, 512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# import pipes
pipeSurface = pygame.image.load('assets/pipe-green.png')
pipeSurface = pygame.transform.scale2x(pipeSurface)
pipeList = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipeheight = [400, 600, 800]

# Game Variables
gravity = 0.25
birdMovement = 0
gameActive = True
score = 0
highScore = 0


# primary game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # force end
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # jump on spacebar press
            if event.key == pygame.K_SPACE and gameActive:
                birdMovement = 0
                birdMovement -= 8
            if event.key == pygame.K_SPACE and not gameActive:
                gameActive = True
                pipeList.clear()
                birdMovement = 0
                birdMovement -= 4
                birdRect.center = (100, 512)

        if event.type == SPAWNPIPE:
            pipeList.extend(pipeCreate())

        if event.type == BIRDFLAP:
            if birdIndex < 2:
                birdIndex += 1
            else:
                birdIndex = 0

            birdSurface, birdRect = birdAnimation()

    # draw floor on screen
    screen.blit(backgroundSurface, (0, 0))

    if gameActive:
        # pull bird down
        birdMovement += gravity

        rotatedBird = rotateBird(birdSurface)

        birdRect.centery += birdMovement
        screen.blit(rotatedBird, birdRect)
        collision(pipeList)
        gameActive = collision(pipeList)

        # pipe moving
        pipeList = pipeMove(pipeList)
        pipeDraw(pipeList)
    else:
        screen.blit(endText, (65, 100))

    # moove the floor back to the start when it leaves the screen
    floor_xpos -= 1
    drawFloor()
    if floor_xpos <= -576:
        floor_xpos = 0

    # tick rate
    pygame.display.update()
    clock.tick(120)

# watch this shit
