#####This is a 2D game based on python programmed by Mal4D. Odima Kokab#####


################# LIBRARIES ##############################
import pygame , os ,sys
from pygame import*
from rocket import menu

########################## WINDOWS ###############################
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
pygame.init()


pygame.display.set_caption('Main Menu')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Bgsound = mixer.Sound("Sounds/menu.ogg")
Bgsound1= mixer.Sound("Sounds/menu2.ogg")
font = pygame.font.Font('fonts/COMIC.TTF', 25)
font2 = pygame.font.Font('freesansbold.ttf', 30)
space = pygame.image.load("places/bg.png")
start_img = pygame.image.load('places/start_btn.png').convert_alpha()
exit_img = pygame.image.load('places/exit_btn.png').convert_alpha()
command=("python3 rocketL.py")
command2= ("python3 rocketM.py")
Bgsound.play(100)
################### COLORS ############################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (102,205,0)
BLUE = (0,0,238)
CYAN = (0,205,205)

##################################################
def levels():
	Med=font.render(" Mode Medium :  "  , True, (YELLOW))
	Low = font.render(" Mode Low : ", True, (GREEN))
	Quit= font.render(" For Quit :  ",True,(RED))
	Med1=font.render("   Press M ",True,(WHITE))
	Low1=font.render(" Press L or START",True,(WHITE))
	Quit1=font.render("  Press Q or Exit",True,(WHITE))
	credits=font.render("By Mal4D",True,(CYAN))

	screen.blit(Med,(0,400))
	screen.blit(Low,(0,360))
	screen.blit(Quit,(0,440))

	screen.blit(Med1,(170,400))
	screen.blit(Low1,(150,360))
	screen.blit(Quit1,(130,440))

	screen.blit(credits,(600,440))

#################load button images##################
start_img = pygame.image.load('places/start_btn.png').convert_alpha()
exit_img = pygame.image.load('places/exit_btn.png').convert_alpha()

################create button instances############
start_button = menu.Button(100, 150, start_img, 0.6)
exit_button = menu.Button(500, 150, exit_img, 0.6)

############### game loop ######################
Bgsound.play()
run = True
while run:
	keys=pygame.key.get_pressed()

	screen.fill(BLACK)
	levels()

	if start_button.draw(screen) or keys[pygame.K_l]:
		print('START')

		Bgsound.stop()
		os.system(command)
		pygame.display.update()
		Bgsound.play()

	if keys[pygame.K_m]:
		Bgsound.stop()
		os.system(command2)
		Bgsound.play()


	if exit_button.draw(screen) or keys[pygame.K_q]:
		sys.exit()
	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()