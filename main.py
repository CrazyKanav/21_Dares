import pygame
 
pygame.init()
 
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

X, Y = display_surface.get_size()

Y -= 700
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
font = pygame.font.Font('freesansbold.ttf', 52)
text = font.render('Welcome to 21 Dares', True, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
 
# infinite loop
while True:
 
    display_surface.fill(white)
 
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
        pygame.display.update()