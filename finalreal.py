#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:02:39 2024

@author: carlgroundstine
"""

import pygame, simpleGE, space, random

""" bullet.py """

class Target (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("target-png--removebg-preview.png")
        self.setSize(75,75)
        self.position = (320,400)
        
       
  

class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.y = 10
        self.x = random.randint(0,self.screenWidth)
        self.colorRect("orange", (10, 3))
        self.setBoundAction(self.HIDE)
        #self.mass = 10
        self.hide()
        
        

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.speed = 15
            self.setBoundAction(self.HIDE)
          
            

class Planet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("moonplanet.png")
        self.setSize(110, 100)
        self.mass = 100
        self.x = 320
        self.y = 240
        
    def gravitate(self, body):
        distance = self.distanceTo(self.scene.ship.rect.center)
        force = (body.mass * self.mass)/distance **2
        direction = self.scene.ship.dirTo(self.rect.center)
        self.scene.ship.addForce(force, direction)    
    
class Instructions(simpleGE.Scene):
    def __init__(self,prevScore):
         super().__init__()
         self.setImage("space-background.jpg")
         self.responce = "Quit"
         
         self.directions = simpleGE.MultiLabel()
         self.directions.textLines = [
         "You are a SPACEMAN",
         "Ride the orbit path",
         "Shoot the target",
         "",
         "Good luck soldier"]
         
         self.directions.center = (320,200)
         self.directions.size = (500,250)
         
         self.btnPlay = simpleGE.Button()
         self.btnPlay.text = "Play"
         self.btnPlay.center = (100,400)
         
         self.btnQuit = simpleGE.Button()
         self.btnQuit.text = "Quit"
         self.btnQuit.center = (540,400)
        
         self.sprites = [self.directions,
                         self.btnPlay,
                         self.btnQuit]
     
        
    def process(self):
        if self.btnPlay.clicked:
            self.responce = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.responce = "Quit"
            self.stop()         

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("space-background.jpg")
        self.ship = space.Ship(self)
        self.bullet = Bullet(self, self.ship)
        self.planet = Planet(self)
        self.target = Target(self)
        self.sndTarget = simpleGE.Sound("random.wav")
        self.setCaption("Press the space bar to shoot.")
        self.y = 10
        self.x = random.randint(0,450)
        self.ship.setAngle(0)
        self.ship.speed = 3
    
        
        self.sprites = [self.ship, self.bullet, self.planet, self.target]
        
        
           
    def process (self):
        self.planet.gravitate(self.ship)
        self.ship.drawTrace("gray") 

        
        if Target(self).collidesWith(self.bullet):
            self.sndTarget.play()   
            
            self.stop()
  
    def processEvent (self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bullet.fire() 
            

 
def main():
    
    keepGoing = True
    lastScore = 0
    while keepGoing: 
        #lastScore = 0
        instructions = Instructions(lastScore)
        #instructions.setPrevScore(lastScore)
        instructions.start()
        
        if instructions.responce == "Play":
            game = Game()
            game.start()
            lastScore = game.score
            
        else: 
            keepGoing = False
#
    
if __name__ == "__main__":
    main()

        