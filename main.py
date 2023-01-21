import pygame
pygame.init()
 
white = (255, 255, 255)
green = (0, 255, 0)
brown = (191, 101, 29)

display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

X, Y = display_surface.get_size()

color_dark = (100,100,100)
pygame.draw.rect(display_surface, color_dark, [590, 315, 80 , 30])
smallfont = pygame.font.SysFont('Corbel',16) 
text = smallfont.render('LOAD' , True , (50,50,50)) 
display_surface.blit(text , (600 , 320))

heading_Y = Y - 700
heading_X = X
 
# set the pygame window name
pygame.display.set_caption('Welcome Page')

#button

font = pygame.font.Font('freesansbold.ttf', 52)
text = font.render('Welcome to 21 Dares', True, brown)
textRect = text.get_rect()
textRect.center = (heading_X // 2, heading_Y // 2)


txt_D1='Basically, a online multiplayer game where players will take turns saying numbers 1,2'
txt_D2=' or + 3 and it will add up to the main thing, the person whose number reaches 21 has to'
txt_D3='do a dare. Dare will ask that person to turn on the webcam and the other players will ask '
txt_D4 ='that person to do a dare. In 3 mins that person has to do the dare. '
font_d = pygame.font.Font('freesansbold.ttf',30)
text_d1 = font_d.render(txt_D1,True,(255,120,0))
text_d1Rect = text_d1.get_rect()
text_d1Rect=(150,Y-200)
text_d2 = font_d.render(txt_D2,True,(255,120,0))
text_d2Rect = text_d2.get_rect()
text_d2Rect=(150,Y-170)
text_d3 = font_d.render(txt_D3,True,(255,120,0))
text_d3Rect = text_d3.get_rect()
text_d3Rect=(145,Y-140)
text_d4 = font_d.render(txt_D4,True,(255,120,0))
text_d4Rect = text_d4.get_rect()
text_d4Rect=(255,Y-110)

 
# infinite loop
while True:
 
    display_surface.fill(white)
 
    display_surface.blit(text, textRect)
    display_surface.blit(text_d1,text_d1Rect)
    display_surface.blit(text_d2,text_d2Rect)
    display_surface.blit(text_d3,text_d3Rect)
    display_surface.blit(text_d4,text_d4Rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if X / 2 -100<= mouse[0] <= X / 2 + 140 and Y / 2 <= mouse[1] <= Y / 2 :
                pygame.quit()
    

    pygame.display.update()