#####This is a 2D game based on python programmed by Mal4D. Odima Kokab#####


############# LIBRARIES ####################
import pygame, sys, random, time
import math
from pygame.constants import SYSTEM_CURSOR_WAITARROW 
from pygame import mixer


pygame.init()

############ WINDOW OPTIONS ################
Swidth = 800 
Sheight = 600
screen = pygame.display.set_mode((Swidth, Sheight))
pygame.display.set_caption("Space Invader By Mal4D")
icon = pygame.image.load('places/favicon.png')
pygame.display.set_icon(icon)


############# COLORS #######################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (102,205,0)
CYAN = (0,205,205)

###########  VARIANTS ######################
isJumping = False

LevelJump = 0.25

rocket = pygame.image.load("rocket/rocket.png")

space = pygame.image.load("places/bg.png")

bullet = pygame.image.load("rocket/bullet.png")

Sound = pygame.mixer.music.load("Sounds/laser.mp3")

Bgsound = mixer.Sound("Sounds/bg.mp3")

enemy = pygame.image.load("Enemy/enemy.png")

bulletObjectSound = mixer.Sound("Sounds/laser.mp3")

score_value=0

font = pygame.font.Font('freesansbold.ttf', 25)

font2= pygame.font.Font("fonts/COMIC.TTF",55)

xscore = 10

yscore = 10 

so=-5

si=5

sm=0

MODE='low'

Endsound= mixer.Sound("Sounds/won.ogg")
############## Class Players ##########################
class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.step = 10
        self.speed = 10
        self.isJumping = False
        

    def drawplayer (self, screen):
        screen.blit(rocket, (rocketObject.x, rocketObject.y))

    def drawscreen (self, screen):
        screen.blit(space, (0, 0))
    

rocketObject = Player(350, 500, 50, 50)


########### Bullet #####################
class Bullet():
    def __init__(self, x, y, y_change, x_change, state):
        self.x = x
        self.y = y
        self.y_change = y_change
        self.x_change = x_change
        self.state = state


    def fire(self):
        self.state = "fire"
        screen.blit(bullet, (self.x + 16, self.y + 10))


bulletObject = Bullet(350, 500, 20, 0, "ready")


######################### Collision Condition ##########################
def isc (enemy, bullet):
    distance = math.sqrt(math.pow(enemyObject.x - bulletObject.x, 2) + (math.pow(enemyObject.y- bulletObject.y, 2)))

    if distance <27:
        return True
    else:
        return False
    
################## Enemy ########################
class Enemy():
    def __init__(self, x, y, stepx, stepy):
        self.x = x
        self.y = y
        self.stepx = stepx
        self.stepy = stepy

    def drawenemy(self, screen):
        screen.blit(enemy, (self.x, self.y))


enemyObject = Enemy(450, 25 , 3, 35)

####################### Score, win, game over ###################

def show_score(x, y):
    score = font.render("Score : " + str(score_value) , True, (255, 255, 255))
    Mode = font.render('Mode : '+str(MODE), True,GREEN)
    screen.blit(score, (x, y))
    screen.blit(Mode,(x,y+25))
()

def gm2():
    time.sleep(5)
    pygame.quit()
    sys.exit()
def gm3():
    time.sleep(30)
    pygame.quit()
    sys.exit()

################### Game Loop #####################################
Bgsound.play(180)
while 1:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()

    keys = pygame.key.get_pressed()
    rocketObject.drawscreen(screen)
    enemyObject.drawenemy(screen)



    if keys[pygame.K_SPACE]:
        if bulletObject.state == "ready":
            bulletObjectSound.play()

            bulletObject.x = rocketObject.x
            bulletObject.y = rocketObject.y
            bulletObject.fire()



    if keys[pygame.K_LEFT] and rocketObject.x - rocketObject.step >= 0:
        rocketObject.x = rocketObject.x - rocketObject.step
    
    if keys[pygame.K_RIGHT] and rocketObject.x + rocketObject.width + rocketObject.step <= Swidth:
        rocketObject.x = rocketObject.x + rocketObject.step

    if bulletObject.y <= 0:
        bulletObject.y = 500
        bulletObject.state = "ready"


    if bulletObject.state == "fire":
        bulletObject.fire()
        bulletObject.y -= bulletObject.y_change



########### Enemy Movement #########################################
  
    enemyObject.x += enemyObject.stepx
    if enemyObject.x <= 0:
        enemyObject.stepx = 5
        enemyObject.y += enemyObject.stepy

    elif enemyObject.x >= 750:
        enemyObject.stepx = -5
        enemyObject.y += enemyObject.stepy

    if enemyObject.y <=0:
        enemyObject.x = 450
        enemyObject.y = random.randint(125, 450)

    if enemyObject.y >=500:
        enemyObject.y=random.randint(125, 450)

    ########## Colllision ##########################################
   
    collision = isc(enemy, bullet)
    if collision:
        bulletObject.y = 500
        bulletObject.state = "ready"
        
        enemyObject.stepx=random.choice([so,si,sm])
        enemyObject.stepy=7
        enemyObject.x= random.randint(100,500)
        enemyObject.y = random.randint(20,450)

        score_value += 1




        


################## Collision ######################


    if score_value == 50:
        pygame.display.update()
        winner = font2.render("YOU WON :)", True, (CYAN))
        screen.fill(BLACK)
        screen.blit(winner, (250, 250))
        pygame.display.update()

        Bgsound.stop()
        enemyObject.y=-30000
        Endsound.play(10)
        gm3()






################## OUTRO #######################################
    rocketObject.drawplayer(screen)
    show_score(x=10,y=10)
    pygame.display.update()