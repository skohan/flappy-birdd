import pygame
import random
from random import randint
import time
from pygame import mixer


#all the prerequisits 
pygame.init()
screen = pygame.display.set_mode((288,512))
pygame.display.set_caption("Floppy Bird")
icon = pygame.image.load("imgs/bird1.png")
pygame.display.set_icon(icon)
scorefont = pygame.font.Font("freesansbold.ttf", 30)
restartfont = pygame.font.Font("freesansbold.ttf", 18)
gameoverfont = scorefont = pygame.font.Font("freesansbold.ttf", 50)

#music
mixer.music.load("sounds/music.mp3")
mixer.music.play(-1)
flying_sound = mixer.Sound("sounds/flying sound.wav")
collsion_sound = mixer.Sound("sounds/collision sound.wav")
point_sound = mixer.Sound("sounds/point sound.wav")

#loading the images
background = pygame.image.load("imgs/bg.png")
base = pygame.image.load("imgs/base.png")
pipe = pygame.image.load("imgs/pipe.png")
bird1 = pygame.image.load("imgs/bird1.png")
bird2 = pygame.image.load("imgs/bird2.png")
bird3 = pygame.image.load("imgs/bird3.png")
inverted_pipe = pygame.image.load("imgs/inverted-pipe .png")

#all the varibles
game_status = "not over"
x_bg = 0
x_bg1 = 288
x_pipe = 0
y_pipe1 = randint(-220,-50)
y_pipe = randint(-220,-50)
x_add = randint(40+288,196+288) 
x_add1 = x_add + 230
speed = 0.5
i=1
t0 = 0
space_status = "not pressed"
x_bird = 50
y_bird = 250
u = 250
score = 0

def collsion1():
	if x_bird> x_add:
		if x_bird< x_add+ 52:
			if y_bird< y_pipe1 + 320:
				collsion_sound.play()
				return True
			elif y_bird > y_pipe1 +320 +120:
				collsion_sound.play()
				return True

def collsion2():
	if x_bird> x_add1:
		if x_bird< x_add1+ 52:
			if y_bird< y_pipe+ 320:
				collsion_sound.play()

				return True
			elif y_bird > y_pipe+320 +120:
				collsion_sound.play()
				return True
def show_score(x,y):
	score_value = scorefont.render(str(score), True, (255,255,255))
	screen.blit(score_value, (x,y))
def show_game_over(x,y):
	game_over_render = gameoverfont.render("Game Over", True, (255,255,255))
	screen.blit(game_over_render, (x,y))
def restarter(x,y,text):
	restart_render = restartfont.render(text, True, (255,255,255))
	screen.blit(restart_render, (x,y))



	

running = True
while running:
	#setting up the background which is constantly moving
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				#print("Space")
				t0 = time.clock()
				space_status = "pressed"
				flying_sound.play()
				temp = y_bird
	if game_status == "not over":
		screen.blit(background, (x_bg,0))
		screen.blit(background,(x_bg1,0))

		screen.blit(inverted_pipe,(x_add,y_pipe1))
		screen.blit(inverted_pipe,(x_add1 ,y_pipe))

		screen.blit(pipe,(x_add,y_pipe1+320+120))
		screen.blit(pipe,(x_add1 ,y_pipe+320+120))

		screen.blit(base, (x_bg,400))
		screen.blit(base, (x_bg1,400))
		
		x_bg -= speed
		x_bg1 -= speed
		x_add -= speed
		x_add1 -= speed

		if x_add < -52:
			x_add = randint(30+288,206+288)
			y_pipe1 = randint(-220,-80)
			score+= 10
			point_sound.play()
		if x_add1 < -52:
			x_add1 = x_add + 230
			y_pipe = randint(-220,-80)
			score+= 10
			point_sound.play()
		


		if x_bg == -288:
			x_bg = 288
		if x_bg1 == -288:
			 x_bg1 = 288
		t = time.clock() - t0
		total_time = 0.3
		if space_status == "pressed":
			#print(t , total_time)
			if t< total_time:
				y_bird = temp - ((u*t) - (9.8*t**2)/2 )
				temp1 = y_bird
				t_0 = time.clock()

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

		show_score(135, 40)
		
		if collsion1() or collsion2():
			game_status = "over"
		if y_bird >376:
			game_status = "over"
			collsion_sound.play()
	elif game_status == "over":

		
		restarter(10,250, "Press Enter To Restart")
		restarter(10,268, "Press Esc To Close")
		show_game_over(10, 200)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_status = "not over"
					x_bg = 0
					x_bg1 = 288
					x_pipe = 0
					y_pipe1 = randint(-220,-50)
					y_pipe = randint(-220,-50)
					x_add = randint(40+288,196+288) 
					x_add1 = x_add + 230
					speed = 0.5
					i=1
					t0 = 0
					space_status = "not pressed"
					x_bird = 50
					y_bird = 250
					u = 250
					score = 0
				if event.key == pygame.K_ESCAPE:
					running = False




		#print(score)
		


	


	pygame.display.update()