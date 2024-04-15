# FinalSpace
Final Project
Jack Van Meter
Elevator pitch document
Computer science 120
4-10-2024

Initial idea:

Random obstacle gravity target practice.

Diving deeper:
You are in space and your goal is to shoot and hit the target. There are two planets that have different masses so in turn they also have different gravity fields. You must shoot a “space bullet” through the planets gravity fields to hit the target. You will only have 5 attempts until you are forced to restart. 

Screens:

Menu:
Will be the starting menu displaying the directions, play, and quit.

Game play mode:
Background is a picture of space.(https://stock.adobe.com/search?k=space+cartoon) In this background there will be 5 sprites being, the target, big planet, little planet, space bullet, space man. In the top right corner there will be an ammo left screen displaying what is left. When the ammo gets to 0 the game quits and takes you to the main menu. Your best ammo count will be displayed as well. 

Sprites:

Target: will be an image, with random regeneration when game is quit or won. Will only repopulate on the top quarter of the screes though so the gravity planets can interfere correctly. A sound will also be attached and activated when space bullet sprite hits. 

bigPlanet: will be under the control of orbits. I will set the mass to double the mass of the smallPlanet (subject to change). This sprite will be a image and will also have a random feature. Every time the game is completed or quit it will populate in the bottom ¾ of the screen.  A sound will also be attached and activate if hit. 

smallPlanet: will be under the control of orbits. I will set the mass to half the mass of bigPlanet (subject to change). This sprite will be a image and will also have a random feature. Every time the game is completed or quit it will populate in the bottom ¾ of the screen. A sound will also be attached and activate if hit.

spaceman: This will be our main character sprite. He will be able to move on the y plane on the bottom of the screen. Wrapping will be the case for motion here. When the spacebar is pressed, the spaceman will fire a spaceBullet. The space bar will also trigger a sound effect. Image found here (https://www.vectorstock.com/royalty-free-vector/astronaut-or-spaceman-cartoon-character-vector-38306455) 

spaceBullet: This will be a 5 X 5 pixel box that will move from the spaceman. Will be activated when the space bar is pressed. The bullets will move in a straight line and then will be under the effects of the gravity of the planets on its way to the target. The exit behavior of the bullet will just be leave. 

Game sketch:



   


![image](https://github.com/JackVM2001/FinalSpace/assets/156926086/6155c8f6-c0f2-42c2-b685-5d9285a08e18)
