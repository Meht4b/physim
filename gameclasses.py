import pygame
import math

#to convert to normal coordinate system

def coord(y,height):
    return height-y
    


class Rectangle:
    def __init__(self,posx,posy,mass,colour,sizex,sizey):
        self.posx=posx
        self.posy=posy
        self.mass = mass
        self.colour=colour
        self.sizex=sizex
        self.sizey=sizey
        self.velx=0
        self.vely=0
        self.accelx=0
        self.accely=0

    def reset(self):
        self.accelx=0
        self.accely=0
        
    def collision(self,rec):       


        self.tempVelx=self.velx
        self.tempVely=self.vely

        self.velx=((self.mass-rec.mass)/(self.mass+rec.mass))*self.tempVelx+(2*rec.mass/(self.mass+rec.mass))*rec.velx
        self.vely=((self.mass-rec.mass)/(self.mass+rec.mass))*self.tempVely+(2*rec.mass/(self.mass+rec.mass))*rec.vely
     
    
        rec.velx=((rec.mass-self.mass)/(rec.mass+self.mass))*rec.velx+(2*self.mass/(self.mass+rec.mass))*self.tempVelx
        rec.vely=((rec.mass-self.mass)/(rec.mass+self.mass))*rec.vely+(2*self.mass/(self.mass+rec.mass))*self.tempVely


    def force(self,rec):
        self.accelx+=self.mass/rec.accelx*rec.mass
        self.accely+=self.mass/rec.accely*rec.mass

    def ncForce(self,accelx,accely):
        self.accelx+=accelx
        self.accely+=accely

    def update(self):
        self.posx+=self.velx
        self.posy+=self.vely

        self.velx+=self.accelx
        self.vely+=self.accely

        self.accely=0
        self.accelx=0




    def getRectObj(self,height):
        return pygame.Rect(self.posx,coord(self.posy,height),self.sizex,self.sizey)

    def draw(self,win,height):
        pygame.draw.circle(win,self.colour,(self.posx,self.posy),self.sizex)
    


