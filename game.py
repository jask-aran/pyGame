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
# car starting points


# Game function
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
