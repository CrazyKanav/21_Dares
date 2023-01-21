import pygame
 
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
 
# assigning values to X and Y variable
X = 400
Y = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
font_t = pygame.font.Font('freesansbold.ttf', 32)
text_t = font_t.render('Welcome to 21 Dares', True, green, blue)
text_tRect = text_t.get_rect()
text_tRect.center = (X // 2, Y // 2)

font_d = pygame.font.Font('freesansbold.ttf',20)
text_d = font_d.render('Basically, a online multiplayer game where players will take turns saying numbers 1,2 or 3 and it will add up to the main thing, the person whose number reaches 21 has to do a dare. Dare will ask that person to turn on the webcam and the other players will ask that person to do a dare. In 3 mins that person has to do the dare. ',True,black)
text_dRect = text_d.get_rect()
text_dRect.center = (0, 400)
 
# infinite loop
while True:
 
    display_surface.fill(white)
 
    display_surface.blit(text_t, text_tRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
        pygame.display.update()