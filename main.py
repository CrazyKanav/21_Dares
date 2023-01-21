import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Show Text')

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Welcome to 21 Dares', True, green, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)


running = True
while running:
    screen.fill(white)
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

pygame.display.flip()
