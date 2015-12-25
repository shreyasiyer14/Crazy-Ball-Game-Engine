import pygame
import random
import time
from Brick import *
from Level import *
from Sprite import *
from IntroCircle import *
from threading import *

pygame.init()
white = (255,255,255)
black = (0,0,0)
red=(255,0,0)
green=(0,155,0)
yellow=(200,200,0)

#Import Comic Sans Font for using in displaying the score.
font=pygame.font.SysFont("comicsansms", 20)

#Setting the frames per second, the frequency of refreshing of the screen.
fps = pygame.time.Clock()

#Setting up the main window.
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Crazy Ball')

#Import the image files to be used as sliders.
icon = pygame.image.load('Sprites/slider.bmp')
pygame.display.set_icon(icon)

smallfont=pygame.font.SysFont("courier", 25)
medfont=pygame.font.SysFont("courier", 50)
largefont=pygame.font.SysFont("courier", 80)

#Load music files.
pygame.mixer.init(frequency=44100, size=-16,channels= 2, buffer=4096)
pygame.mixer.music.load('Sounds/BeatWave.mp3')

#Multithreading music sounds, to play continuously in the background.
def gameSound():
	pygame.mixer.music.load('Sounds/Seasons.mp3')
	pygame.mixer.music.play(-1)

#Function to initialize text objects of different sizes.
def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text,True,color)
	elif size == "medium":
		textSurface = medfont.render(text,True,color)
	elif size == "large":
		textSurface = largefont.render(text,True,color)

	return textSurface,textSurface.get_rect()

def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
	textSurf,textRect = text_objects(msg,color,size)
	textRect.center = (buttonx+(buttonwidth/2)),(buttony+(buttonheight/2))
	gameDisplay.blit(textSurf,textRect)

#Blitting message to the screen, such as "Game over" or "You Win!".
def message_to_screen(msg,color,y_displace=0,size = "small"):
	textSurf,textRect = text_objects(msg,color,size)
	textRect.center =(800/2),(600/2)+y_displace
	gameDisplay.blit(textSurf,textRect)

#Displaying the score.
def score(count):
    scores = font.render("Score: "+str(count),1,(255,255,255))
    gameDisplay.blit(scores,(20,20))

#Starting screen.
def game_info():
	info = True
	while info:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(black)
		message_to_screen("Controls",red,-100,size="large")
		message_to_screen("To move the slider up : w",red,-30)
		message_to_screen("To move the slider down : s",red,10)
		message_to_screen("To move the bottom slider right : right arrow key",red,50)
		message_to_screen("To move the bottom slider left : left arrow key",red,90)
		message_to_screen("Pause : p",red,130)
				
		button("Play",150,500,100,50,(150,50,50),green,action="Play")
		button("Back",350,500,100,50,(50,150,50),green,action="Back")
		button("Quit",550,500,100,50,(50,50,150),green,action="Quit")

		pygame.display.update()
		fps.tick(20)

def button(text,x,y,width,height,inactive_color,active_color,action=None):
	cur=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()

	if x<cur[0]<x+width and y<cur[1]<y+height:
		pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
		if click[0] == 1 and action!=None:
			if action == "Quit":
				pygame.quit()
				quit()

			elif action == "Play":
		                pygame.mixer.music.stop()
				Thread(target = gameSound).start()
				gameLoop()

			elif action == "Info":
				game_info()
			
			if action == "Back":
				game_intro()
	else:
		pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))

	text_to_button(text,white,x,y,width,height)

randcirclelist = []

#Start Screen.
def game_intro():
    intro = True
    #Two balls with random coordinates, for display. 
    ball_x=random.randrange(5,500)
    ball_y=random.randrange(5,500)

    ball_x2=random.randrange(5,500)
    ball_y2=random.randrange(5,500)
    dx=random.randrange(-10,10)
    dy=random.randrange(1,10)

    dx2=random.randrange(-10,10)
    dy2=random.randrange(1,10)
    pygame.mixer.music.play(-1)
    
    while intro:
	#Initialize a Circle object, and append it to a list.
	randcircle = IntroCircle(5)
	randcirclelist.append(randcircle)
	
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
        		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

        ball_x+=dx
	ball_y+=dy
	
        ball_x2+=dx2
	ball_y2+=dy2

	#The condition to change the direction of the balls when the ball hits the edges of the screen.
        if ball_x<=0:
        	dx*=-1
	elif ball_x>=790:
                dx*=-1
        if ball_y>=590:
       		dy *= -1
	elif ball_y<0:
                dy*=-1

        if ball_x2<=0:
        	dx2*=-1
	elif ball_x2>=790:
                dx2*=-1
        if ball_y2>=590:
       		dy2 *= -1
	elif ball_y2<0:
                dy2*=-1

	gameDisplay.fill(black)

	message_to_screen("Crazy Ball",(255,100,100),-100,size="large")
        pygame.draw.circle(gameDisplay, (255,255,155),(ball_x, ball_y), 10, 2)
        pygame.draw.circle(gameDisplay, (255,255,155),(ball_x2, ball_y2), 10, 2)				
	for circle in randcirclelist:
		circle.update()
		if circle.radius >= 500:	
			randcirclelist.remove(circle)
		circle.render(gameDisplay)
	button("Play",150,500,100,50,(150,50,50),green,action="Play")
	button("Info",350,500,100,50,(50,150,50),green,action="Info")
	button("Quit",550,500,100,50,(50,50,150),green,action="Quit")
	pygame.display.update()
	fps.tick(20)

#Pause the game.
def pause():
	paused = True
	
	message_to_screen("Paused",red,-100,size="medium")
	message_to_screen("Press S to continue or Q to quit",green,25,size="small")
	pygame.display.update()

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
		fps.tick(5)
#Function that will be called when the player successfully completes the game.
def levelcomplete(count):
    paused = True
    message_to_screen("Congratulations!",white,-100,size="large")
    message_to_screen("You Win!",(155,155,155),-50,size="medium")  
    score(count)    
    message_to_screen("Press S to continue or Q to quit",green,25,size="small")
    pygame.display.update()
        
    while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
				 gameLoop()
                        elif event.key == pygame.K_q:
                                pygame.quit()
                                quit()
            fps.tick(5)


slider = pygame.image.load('Sprites/slider.bmp')
slider2 = pygame.transform.rotate(slider, -90)

#Function to detect the collision and return value whether the collision was horizontal or vertical.
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
           	if (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
            	    return True,3
           	elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
            	    return True,4
		elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
                    return True,3
	    	elif (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
            	    return True,4
	    	else:
		    return False,0 

#Main game loop.
def gameLoop():
	#Score
        count = 0
        
	randIndex = random.randrange(0,3)
        level_obj = Level(randIndex)
        level = level_obj.levels()
	brickList = []
	#Set up a color for each row of the bricks.
	for y in range(len(level)):
		color = (random.randrange(50,200),random.randrange(50,200),random.randrange(50,100))
    		for x in range(len(level[y])):
        		if (level[y][x] == 1):
        	    			brickList.append(Brick(x*32, y*32,color))
	
	gameExit = False
	gameOver = False
	
	cur_x_1 = 400
	cur_y_1 = 550

	cur_x_2 = 20
	cur_y_2 = 300

	x_change_1=0
	y_change_1=0


	x_change_2=0
	y_change_2=0

	ball_x=random.randrange(250,400)
	ball_y=random.randrange(250,500)
	
	#To initialize the sprite object.
	spriteball = Sprite(ball_x, ball_y)
	#dx=random.randrange(3,5)
	#dy=random.randrange(3,5)
	dy = 7
	dx = 7
    	
	while not gameExit:
	        pygame.draw.circle(gameDisplay, white, (0,0),10,0)
		if gameOver == True:
			message_to_screen("Game over",(0,255,150),-50,size = "large")
			message_to_screen("Press S to play again or Q to quit",white,50,size = "small")
			pygame.display.update()

		while gameOver == True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key ==	pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_s:
						gameLoop()	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
		#Keyboard events.
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change_1=-15
					y_change_1=0
				elif event.key == pygame.K_RIGHT:
					x_change_1=15
					y_change_1=0
				
				elif event.key == pygame.K_UP:
					x_change_2=0
					y_change_2=-15
				elif event.key == pygame.K_DOWN:
					x_change_2=0
					y_change_2=15
				elif event.key == pygame.K_p:
					pause()
		
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change_1 = 0
					y_change_1 = 0
       				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
              				x_change_2 = 0
               				y_change_2 = 0
	
		
		cur_x_1+=x_change_1
		cur_y_1+=y_change_1
   		cur_x_2+=x_change_2
		cur_y_2+=y_change_2
		if cur_x_1 >= 720:
			cur_x_1 = 720
		if cur_x_1 <= 0:
			cur_x_1 = 0
		if cur_y_2 >= 520:
			cur_y_2 = 520
		if cur_y_2 <= 0:
			cur_y_2 = 0
			
		#Collision with the sliders.
		a1,b1=detectCollisions(ball_x, ball_y, 10,10,cur_x_1, cur_y_1-12,80,10)
		
		if (ball_y + 10) > cur_y_1 and (ball_x+10 < cur_x_1 or ball_x > cur_x_1+80):
			a1 == False
			gameOver = True
		if a1 == True:
			dy*=-1
			dx = dx + (ball_x - cur_x_1-40)/20 - x_change_1/3
       		#pygame.mixer.music.load('Sounds/Boing.mp3')
           	#pygame.mixer.music.play(1)
		
		a2,b2 = detectCollisions(ball_x, ball_y, 10,10, cur_x_2,cur_y_2, 25,80)
		if a2==True:
			dx*=-1
			dy = dy + (ball_y - cur_y_2 -40)/20 - y_change_2/3
			#pygame.mixer.music.load('Sounds/Boing.mp3')
            		#pygame.mixer.music.play(1)
			
		if ball_x<=0: 
			gameOver = True
		elif ball_x>=790:
			dx*=-1
		if ball_y>=590:
			gameOver = True
		elif ball_y<0:
			dy*=-1

		#ball_x+=dx
		#ball_y+=dy
		gameDisplay.fill(black)
	 	gameDisplay.blit(slider, (cur_x_1, cur_y_1))
	   	gameDisplay.blit(slider2, (cur_x_2, cur_y_2))
	   	for brick in brickList:
		#If the ball collides with the brick, then remove the brick from brickList.
		     a,b = detectCollisions(ball_x, ball_y, 10,10,brick.x, brick.y, brick.width, brick.height)
	       	     if a == True and b == 3:
			    brickList.remove(brick)
			    dy *= -1
			    dx *= 1
            	   	    count+=1
                            #pygame.mixer.music.load('Sounds/Brick.mp3')
                     	    #pygame.mixer.music.play(1)
			    #ball_y+=dy

	       	     elif a == True and b == 4:
			    brickList.remove(brick)
			    dx *= -1
		            dy *= 1
	                    count+=1
                     	   # pygame.mixer.music.load('Sounds/Brick.mp3')
                     	    #pygame.mixer.music.play(1)
			    #ball_x+=dx
		ball_x+=dx
		ball_y+=dy
		#Update the x and y coordinates of the sprite.
		spriteball.x=ball_x
		spriteball.y=ball_y
		spriteball.update(gameDisplay)
		
	        if len(brickList)==0:
        	    levelcomplete(count)

		#Update the bricks and display the score accordingly.
		for brick in brickList:
	            brick.render(gameDisplay)
	       	    score(count)
		pygame.display.update()
		fps.tick(30)
	
	pygame.quit()
	quit()	

game_intro()
gameLoop()
