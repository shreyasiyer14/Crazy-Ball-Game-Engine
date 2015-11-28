import pygame
import random
import math
from Brick import *
pygame.init()
font=pygame.font.SysFont("courier", 15)
resx=800
resy=600
gameDisplay = pygame.display.set_mode((resx,resy))
pygame.display.set_caption("Crazy Ball")
ext = 0
lx = resx/2
ly = 0
lx1 = resx/2
ly1 = resy-5
chx = 0
chx1 = 0
gq = 0
clock = pygame.time.Clock()
bx = random.randint(20,resx-20)
by = resy/2
cbx = 5
cby = 5
count=0
level = [
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
         [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
         [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
         [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
         [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
         [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]         
         ]

brickList = []

for y in range(len(level)):
    for x in range(len(level[y])):
        if (level[y][x] == 1):
                if y==2:
                    brickList.append(Brick(x*32, y*32,(0,0,255)))
                if y==3:
                    brickList.append(Brick(x*32, y*32,(0,155,105)))
                if y==4:
                    brickList.append(Brick(x*32, y*32,(155,0,55)))
                if y==5:
                    brickList.append(Brick(x*32, y*32,(155,0,155)))
                if y==6:
                    brickList.append(Brick(x*32, y*32,(155,155,5)))
                if y==7:
                    brickList.append(Brick(x*32, y*32,(25,255,5)))
                if y==8:
                    brickList.append(Brick(x*32, y*32,(225,205,105)))

def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
	    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
                return True,3
            elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
                return True,3
            elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
                return True,3
            elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
                return True,4
	    else:
		return False,0 

def ball(x,y):
	gameDisplay.fill((255,255,255),rect=[x,y,10,10])


while not ext:
	while gq!= 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()  
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					chx1 = -10
				if event.key == pygame.K_RIGHT:
					chx1 = 10
				if event.key == pygame.K_a:
					chx = -10
				if event.key == pygame.K_d:
					chx = 10
		
			if event.type == pygame.KEYUP:
				if  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					chx1 = 0 
				if  event.key == pygame.K_a or event.key == pygame.K_d:
					chx = 0 
		if (bx <= 0 ): cbx=-cbx
		if (bx >= resx-10 ): cbx = -cbx
		bx += cbx
		by += cby
		lx += chx
		lx1 += chx1
		if lx < 0: lx = 0
		if lx > resx-100: lx = resx-100
		if lx1 < 0: lx1 = 0
		if lx1 > resx-100: lx1 = resx-100
		if by < 0 or by>resy-10:
			gq = 1
			break
		#collision
		if (((cby > 0) and by == ly-10) or ((cby<0) and by == ly + 5))  and lx-10<bx<lx+100:
			cby = -cby
			cbx = cbx + (bx-lx-50)/25 - chx/3
			count=count+1
		if (((cby > 0) and by == ly1-10) or ((cby<0) and by == ly1 + 5))  and lx1-10<bx<lx1+100:
			cby = -cby
			cbx = cbx + (bx-lx1-50)/25 - chx1/3 
			count=count+1
		gameDisplay.fill((0,0,0))
		gameDisplay.fill((255,0,0),rect=[lx,ly,100,5])
		gameDisplay.fill((255,0,0),rect=[lx1,ly1,100,5])
		dx,dy = cbx,cby
		for brick in brickList:
    			a,b = detectCollisions(bx, by, 10,10,brick.x, brick.y, brick.width, brick.height)
        		if a == True and b == 3:
            			brickList.remove(brick)
                		dy *= -1
                		dx *= 1
                    		by+=dy
                        
                        elif a == True and b == 4:
                            	brickList.remove(brick)
                                dx *= -1
                                dy *= 1
                                bx+=dx
		
		score = font.render("Score: "+str(count),1,(255,255,255))
		gameDisplay.blit(score,(20,20))
		ball(bx,by)
	        for brick in brickList:
        	        brick.render(gameDisplay)
        

		pygame.display.update()
		clock.tick(30)
	gameover = font.render("Game Over",1,(255,255,255))
	reset = font.render("Press q to quit, r to reset!",1,(255,255,255))
	gameDisplay.blit(gameover,(resx/2-30,resy/2))
	gameDisplay.blit(reset,(resx/2-120,resy/2 + 30))
        pygame.display.update()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()  
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					gq = 0
					bx = random.randint(20,resx-20)
					by = resy/2
					chx = 0
					chx1 = 0
					count = 0
				if event.key == pygame.K_q:
					ext = 1
	
	
pygame.quit()
quit()
