import pygame, simpleGE, random

""" space.py 
    illustrates space movement using simpleGE
    ship images modified from Ari's spritelib.
"""

class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "cruise": pygame.image.load("spaceman.png"),
            "left":   pygame.image.load("spaceman.png"),
            "right":  pygame.image.load("spaceman.png"),
            "thrust": pygame.image.load("spaceman.png")}
        self.copyImage(self.images["cruise"])
        self.setSize(50,50)
        #self.position = (100,50)
        self.y = 10
        self.x = random.randint(0,self.screenWidth)
        self.moveSpeed = 5
        self.mass = 10
        self.setBoundAction(self.BOUNCE)
        
 
        
        def process(self):
            if self.isKeyPressed(pygame.K_LEFT):
                self.x -=self.moveSpeed
            if self.isKeyPressed(pygame.K_RIGHT):
                self.x +=self.moveSpeed
                
        # self.copyImage(self.images["cruise"])
        # if self.isKeyPressed(pygame.K_LEFT):
        #     self.imageAngle += 5
        #     self.copyImage(self.images["right"])
        # if self.isKeyPressed(pygame.K_RIGHT):
        #     self.imageAngle -= 5
        #     self.copyImage(self.images["left"])    
        # if self.isKeyPressed(pygame.K_UP):
        #     self.addForce(.2, self.imageAngle)
        #     self.copyImage(self.images["thrust"])
            
def main():
    game = simpleGE.Scene()
    game.setCaption("Pygame in SPAAAAACE!")
    ship = Ship(game)
    game.sprites = [ship]
    game.start()
    
if __name__ == "__main__":
    main()

