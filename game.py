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
red = (255, 0, 0)
# colors

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
carWidth = 73
# loads clock, crash detection, car sprite and car sprite width (for hitboxes)


def car(x, y):
    gameDisplay.blit(carImg, (x, y))
# draw the car to the display


x = (displayWidth * 0.45)
y = (displayHeight * 0.8)
carSpeed = 0
# car starting points, change in x position and speed


# Game function
def game_loop():
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x, y)

        if x > displayWidth - carWidth:
            x = displayWidth - carWidth - 5
        elif x < 0:
            x = 5

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
