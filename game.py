import random
import pygame
import math
from gameclasses import Rectangle,coord


pygame.init()

WIDTH,HEIGHT = 1900,1000

win = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

objlis=[]

font = pygame.font.Font('Gidole-Regular.otf', 25)

#texts[Draw,Force,Grav,Sim]

texts = [font.render('Draw',True,(255,255,255)),font.render('Force',True,(255,255,255)),font.render('Gravity',True,(255,255,255)),font.render('Start',True,(255,255,255))]
textsBool=[True,False,True,False]

grounds = [Rectangle(0,10,1000000000,(100,100,100),WIDTH,10),Rectangle(0,HEIGHT,1000000000,(100,100,100),10,WIDTH),Rectangle(0,HEIGHT+10,1000000000,(100,100,100),WIDTH,20),Rectangle(WIDTH-10,HEIGHT,1000000000,(100,100,100),10,WIDTH)]

click = False

while True:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            break
        if events.type==pygame.MOUSEBUTTONDOWN and textsBool[0]:
            posx,posy=pygame.mouse.get_pos()

            if not (posx>WIDTH-80 and posy<108):
                objlis.append(Rectangle(posx,coord(posy,HEIGHT),10,(random.randint(100,255),random.randint(100,255),random.randint(100,255)),20,20))
                if textsBool[1]:
                    objlis[len(objlis)-1].velx=10
                    objlis[len(objlis)-1].vely=0

    win.fill((0,0,0))

    for ind,elem in enumerate(objlis):

        #input
        if textsBool[2]:
            elem.ncForce(0,-9.8/60)
        if textsBool[3]:
            elem.update()
        elem.draw(win,HEIGHT)

        for ground in grounds:
    
            if pygame.Rect.colliderect(elem.getRectObj(HEIGHT),ground.getRectObj(HEIGHT)):
                elem.collision(ground)

        for i in range(ind+1,len(objlis)):
            if pygame.Rect.colliderect(elem.getRectObj(HEIGHT),objlis[i].getRectObj(HEIGHT)):
                elem.collision(objlis[i])
    
    
    for ground in grounds:
        ground.update()
        ground.draw(win,HEIGHT)

    texty=10

    #input from user (buttons)

    for ind,text in enumerate(texts):
        
        win.blit(text,(WIDTH-80,texty))
        
        mous = pygame.mouse.get_pos()

        textRec = text.get_rect()
        textRec.x,textRec.y=WIDTH-80,texty

        if textRec.collidepoint(mous):
            if pygame.mouse.get_pressed()[0] and click == False:
                textsBool[ind]=not textsBool[ind]
                click=True


        if pygame.mouse.get_pressed()[0]==0:
            click = False
        
        texty+=22


    pygame.display.update()

    clock.tick(60)