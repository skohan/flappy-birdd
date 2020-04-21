import pygame
import random
from random import randint
import time
#all the prerequisits 
pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("Floppy Bird")
icon = pygame.image.load("imgs/bird1.png")
pygame.display.set_icon(icon)

#loading the images
background = pygame.image.load("imgs/bg.png")
bird1 = pygame.image.load("imgs/bird1.png")
bird2 = pygame.image.load("imgs/bird2.png")
bird3 = pygame.image.load("imgs/bird3.png")
base = pygame.image.load("imgs/base.png")


#all the varibles

#funtinons
i=1
t0 = 0
space_status = "not pressed"
x_bird = 50
y_bird = 250
u = 250
	

running = True
while running:
	#setting up the background which is constantly moving
	screen.blit(background,(0,0))
	screen.blit(base,(0,400))
	

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print("Space")
				t0 = time.clock()
				space_status = "pressed"
				temp = y_bird
	t = time.clock() - t0
	total_time = 0.3
	if space_status == "pressed":
		#print(t , total_time)
		if t< total_time:
			y_bird = temp - ((u*t) - (9.8*t**2)/2 )
			temp1 = y_bird
			t_0 = time.clock()
			if i==1:
				pygame.transform.rotate(bird1, angle)
				i = 2
			elif i == 2:
				pygame.transform.rotate(bird2, angle)
				i = 3
			elif i== 3:
				pygame.transform.rotate(bird3, angle)
				i = 1

		if t>=total_time:
			t1 = time.clock() - t_0
			y_bird = temp1 + ((250*t1**2)/2 )
		#print(temp1, y_bird)
		if i==1:
			screen.blit(bird1,(x_bird,y_bird))
			i = 2
		elif i == 2:
			screen.blit(bird2,(x_bird,y_bird))
			i = 3
		elif i== 3:
			screen.blit(bird3,(x_bird,y_bird))
			i = 1
	if space_status == "not pressed":
		if i==1:
			screen.blit(bird1,(x_bird,y_bird))
			i = 2
		elif i == 2:
			screen.blit(bird2,(x_bird,y_bird))
			i = 3
		elif i== 3:
			screen.blit(bird3,(x_bird,y_bird))
			i = 1

		
	



	pygame.display.update()