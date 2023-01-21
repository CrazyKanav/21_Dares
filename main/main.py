import pygame
from network import Player
pygame.init()
 

player = Player()
player_name = player.getName()

white = (255, 255, 255)
green = (0, 255, 0)
brown = (191, 101, 29)

display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

X, Y = display_surface.get_size()

heading_Y = Y - 700
heading_X = X
 
# set the pygame window name
pygame.display.set_caption('Welcome Page')
 
font = pygame.font.Font('freesansbold.ttf', 52)
text = font.render('Welcome to 21 Dares', True, brown)
textRect = text.get_rect()
textRect.center = (heading_X // 2, heading_Y // 2)

font_d = pygame.font.Font('freesansbold.ttf',30)
def line1():
    txt_D1='Basically, a online multiplayer game where players will take turns saying numbers 1,2'
    text_d1 = font_d.render(txt_D1,True,(255,120,0))
    text_d1Rect = text_d1.get_rect()
    text_d1Rect=(150,Y-200)

    return text_d1, text_d1Rect

def line2():
    txt_D2=' or + 3 and it will add up to the main thing, the person whose number reaches 21 has to'
    text_d2 = font_d.render(txt_D2,True,(255,120,0))
    text_d2Rect = text_d2.get_rect()
    text_d2Rect=(150,Y-170)

    return text_d2, text_d2Rect

def line3():
    txt_D3='do a dare. Dare will ask that person to turn on the webcam and the other players will ask '
    text_d3 = font_d.render(txt_D3,True,(255,120,0))
    text_d3Rect = text_d3.get_rect()
    text_d3Rect=(145,Y-140)

    return text_d3, text_d3Rect

def line4():
    txt_D4 ='that person to do a dare. In 3 mins that person has to do the dare. '
    text_d4 = font_d.render(txt_D4,True,(255,120,0))
    text_d4Rect = text_d4.get_rect()
    text_d4Rect=(255,Y-110)

    return text_d4, text_d4Rect

# Name
name_font = pygame.font.Font('freesansbold.ttf', 42)
name = font.render(player_name, True, (0,0,0))
name_rect = name.get_rect()
name_rect=(50,50)


 
# infinite loop
while True:
    display_surface.fill(white)
    
    display_surface.blit(text, textRect)

    text_d1, text_d1Rect = line1()
    display_surface.blit(text_d1,text_d1Rect)

    text_d2, text_d2Rect = line2()
    display_surface.blit(text_d2,text_d2Rect)

    text_d3, text_d3Rect = line3()
    display_surface.blit(text_d3,text_d3Rect)

    text_d4, text_d4Rect = line4()
    display_surface.blit(text_d4,text_d4Rect)

    display_surface.blit(name, name_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
        pygame.display.update()