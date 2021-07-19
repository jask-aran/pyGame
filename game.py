import pygame
# imports

pygame.init()
# initialise pygame

displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('A Bit Racey')
# set display size and name

black = (0, 0, 0)
white = (255, 255, 255)
# colors

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
# loads clock, crash detection and car sprite


def car(x, y):
    gameDisplay.blit(carImg, (x, y))
# draw the car to the display


x = (displayWidth * 0.45)
y = (displayHeight * 0.8)
xChange = 0
carSpeed = 0
# car starting points, change in x position and speed


# Game function
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -5
            elif event.key == pygame.K_RIGHT:
                xChange = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xChange = 0

    x += xChange

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
