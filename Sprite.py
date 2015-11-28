import pygame
class Sprite: 
	def __init__(self,x,y): 
		self.x=x 
		self.y=y
		self.width=50 
  		self.height=50 
 		self.i0 = pygame.image.load("Sprites/m1.bmp")
	      	self.i1 = pygame.image.load("Sprites/m2.bmp")
		self.timeTarget=10
		self.timeNum=0
		self.currentImage=0 
 	def update(self,window): 
		self.timeNum+=1
		if (self.timeNum==self.timeTarget): 
			if (self.currentImage==0):
				self.currentImage=1 
			else: 
				self.currentImage=0
			self.timeNum=0
		self.render(window) 
	def render(self,window):
		 if (self.currentImage==0):
			 window.blit(self.i0, (self.x,self.y))
		 else:
			 window.blit(self.i1, (self.x,self.y))
