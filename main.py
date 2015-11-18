import pygame
from Brick import *

pygame.init()
white = (255,255,255)
black = (0,0,0)

cur_x_1 = 400
cur_y_1 = 550

cur_x_2 = 20
cur_y_2 = 20

x_change_1=0
y_change_1=0


x_change_2=0
y_change_2=0

fps = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('CraZY Ball')
gameExit = False
slider = pygame.image.load('Sprites/slider.bmp')
slider2 = pygame.transform.rotate(slider, -90)

level = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
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
            brickList.append(Brick(x*32, y*32))


ball_x=400
ball_y=300
dx=10
dy=10
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change_1=-10
				y_change_1=0
			elif event.key == pygame.K_RIGHT:
				x_change_1=10
				y_change_1=0
			
			elif event.key == pygame.K_w:
				x_change_2=0
				y_change_2=-10
			elif event.key == pygame.K_s:
				x_change_2=0
				y_change_2=10

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change_1 = 0
				y_change_1 = 0
       			if event.key == pygame.K_w or event.key == pygame.K_s:
              			x_change_2 = 0
               			y_change_2 = 0
	
	
	cur_x_1+=x_change_1
	cur_y_1+=y_change_1
   	cur_x_2+=x_change_2
	cur_y_2+=y_change_2
	
	ball_x+=dx
	ball_y+=dy

    def detectCollisions(self, x1,y1,w1,h1,x2,y2,w2,h2):
            if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
                return True
        
            elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
                return True
        
            elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
                return True

            elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
                return True
        
            else:
                return False


	if dx>=0 and ball_x>=cur_x_1 and ball_x<=cur_x_1+40 and ball_y==cur_y_1:
		dx*=1
		dy*=-1
	elif dx<=0 and ball_x<=cur_x_1+80 and ball_x>=cur_x_1+40 and ball_y==cur_y_1:
		dx*=1
		dy*=-1
	elif dx>=0 and ball_x<=cur_x_1+80 and ball_x>=cur_x_1+40 and ball_y==cur_y_1:
		dx*=1
		dy*=-1
	elif dx<=0 and ball_x<=cur_x_1+40 and ball_x>=cur_x_1 and ball_y==cur_y_1:
		dx*=1
		dy*=-1

	if ball_x==50 and ball_y<=cur_y_2+80 and ball_y>=cur_y_2:
		dx*=-1
		dy*=1

	if ball_x<=0: 
		gameExit = True
		print "You lose"
	elif ball_x>=790:
		dx*=-1
	if ball_y>=590:
		gameExit = True
		print "You lose"
	elif ball_y<0:
		dy*=-1



	gameDisplay.fill(white)

    gameDisplay.blit(slider, (cur_x_1, cur_y_1))
    gameDisplay.blit(slider2, (cur_x_2, cur_y_2))
    pygame.draw.circle(gameDisplay, (100,90,90),(ball_x,ball_y),10,0)
    for brick in brickList:
        if detectCollisions(ball_x, ball_y, 10,10,brick.x, brick.y, brick.width, brick.height):
            blockList.pop(brick)
    
    for brick in brickList:
        brick.render(gameDisplay)

	pygame.display.update()
	fps.tick(60)
pygame.quit()
quit()
