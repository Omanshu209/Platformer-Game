import pygame

pygame.init()

win = pygame.display.set_mode((1200,770))

pygame.display.set_caption("Game!")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpeg')
block=pygame.image.load("block.jpeg")
blockM=pygame.transform.scale(block,(50,50))
block2=pygame.image.load("block2.jpeg")
block2M=pygame.transform.scale(block2,(50,50))
bgA=pygame.transform.scale(bg,(1000,700))
char = pygame.image.load('standing.png')
p1=pygame.image.load("portal1.png")
p1A=pygame.transform.scale(p1,(50,100))
p2=pygame.image.load('portal2.png')
p2A=pygame.transform.scale(p2,(50,100))
clock = pygame.time.Clock()
grass=pygame.image.load("grass.png")
grassB=pygame.image.load("grass2.png")
grass2=pygame.transform.scale(grassB,(250,100))
grass1=pygame.transform.scale(grass,(300,80))
grass3=pygame.transform.scale(grassB,(520,210))
stscreenn=pygame.image.load("Starting.jpeg")
stscreen=pygame.transform.scale(stscreenn,(1000,700))
controller=pygame.image.load('Control.png')
controller=pygame.transform.scale(controller,(200,189))
controller2=pygame.image.load('Control2.png')
controller2=pygame.transform.scale(controller2,(200,165))
jumpb=pygame.image.load('jumpb.png')
jumpb=pygame.transform.scale(jumpb,(110,140))
left=False
right=False

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.fall=100
        self.standing = True 
        self.health=10
        self.hitbox=(self.x+20,self.y+10,26,50)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox=(self.x+20,self.y+10,26,50)
        if keys[pygame.K_s]:
            pygame.draw.rect(win,(0,255,0),self.hitbox,2)
        
    def hit(self):
         if level>=3:
         	self.x=10
         	self.health-=2
         	self.walkCount = 0
         	font1 = pygame.font.SysFont('comicsans', 100)
         	text = font1.render('-2', 1, (255,0,255))
         	win.blit(text, (550 - (text.get_width()/2),350))
         	pygame.display.update()
         	i=0
         	while i < 100 :
         	    pygame.time.delay(10)
         	    i += 1
         	    for event in pygame.event.get():
         	             if event.type == pygame.QUIT:
         	             	 i = 301
         	             	 pygame.quit()
         	             	 
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

class dog:
	DogLeft=[pygame.transform.scale(pygame.image.load('dogl1.png'),(40,35)),pygame.transform.scale(pygame.image.load('dogl2.png'),(40,35)),pygame.transform.scale(pygame.image.load('dogl3.png'),(40,35))]
	DogRight=[pygame.transform.scale(pygame.image.load('dogr1.png'),(40,35)),pygame.transform.scale(pygame.image.load('dogr2.png'),(40,35)),pygame.transform.scale(pygame.image.load('dogr3.png'),(40,35))]
	DogSit=pygame.transform.scale(pygame.image.load('dogsit.png'),(40,35))
	def __init__(self,active, x, y, width, height,plocx,plocy,end):
	    if active:
	       self.x=plocx-50 
	       self.y=plocy 
	    else:
	       self.x = x
	       self.y = y 
	    self.plocx=plocx 
	    self.plocy=plocy
	    self.width = width
	    self.height = height 
	    self.end=end
	    self.path = [self.x, self.end]
	    self.walkCount = 0
	    self.vel = 3
	    self.hitbox = (self.x + 17, self.y + 2, 31, 57)
	    self.health = 10
	    self.visible = True 
	    self.active=active
	    self.dir=0
	def draw(self,win,active,plocx2,plocy2,left,right,x,y):
	    self.active=active
	    if self.active:
	        if self.walkCount + 1 >= 33:
	        	self.walkCount = 0
	        if left:
	            win.blit(self.DogLeft[self.walkCount //11], (plocx2+50,plocy2+30))
	            self.walkCount += 1
	            self.dir=1
	        elif right:
	            win.blit(self.DogRight[self.walkCount //11], (plocx2-30, plocy2+30))
	            self.walkCount += 1
	            self.dir=2
	        else:
	        	if self.dir==1:
	        		win.blit(self.DogSit,(plocx2+50,plocy2+30))
	        	elif self.dir==2:
	        		win.blit(self.DogSit,(plocx2-30,plocy2+30))
	    else:
	        win.blit(self.DogSit,(x,y))

#    def move(self):
#        if self.active:
#	        if self.vel > 0:
#	            if self.x + self.vel < self.path[1]:
#	                self.x =plocx-50
#	            else:
#	                self.vel = self.vel * -1
#	                self.walkCount = 0
#	        else:
#	            if self.x - self.vel > self.path[0]:
#	                self.x =plocx-50
#	            else:
#	                self.vel = self.vel * -1
#	                self.walkCount = 0
#	    else:
#	    	win.blit(DogSit,(self.x,self.y))
class text:
	def __init__(self,nameA,size,nameB,word,colour,posX,posY):
		self.nameA=pygame.font.SysFont("comicsans",size,True)
		self.nameB=self.nameA.render(word,1,colour)
		win.blit(self.nameB,(posX,posY))

level=0
score=0
dogx=150
dogy=200
fall=False
pets=False
def DrawGameWindow():
	global level,fall,left,right,pets
	win.fill((255,255,255))
	pygame.draw.rect(win,(0,255,0),(5,0,1257,720),3)
	pygame.draw.rect(win,(0,0,255),(1005,0,250,700),10)
	pygame.draw.rect(win,(255,0,0),(1015,10,230,50))
	pygame.draw.rect(win,(255,0,0),(1015,594,230,100))
	pygame.draw.rect(win,(255,0,0),(8,705,1249,12))
	win.blit(controller,(1030,180))
	win.blit(controller2,(1040,70))
	win.blit(jumpb,(1080,330))
	text("ControlsA",68,"ControlsB","Controls",(0,255,0),1012,18)
	pygame.draw.rect(win,(255,0,0),(1025,495,220,75))
	text("LeftPA",35,"LeftPB",f"MoveLeft: {left}",(0,136,64),1027,500)
	text("RightPA",33,"RightPB",f"MoveRight: {right}",(0,136,64),1027,530)
	text("LevelA",60,"LevelB",f"Level: {level}",(255,100,0),1020,650)
	text("ScoreA",50,"ScoreB",f"Score: {score}",(255,100,130),1020,600)
	text('dev',22,'devlop','D   E   V   L   O   P   E   D        B   Y       O   M   A   N   S   H   U',(0,0,255),210,705)
	if man.health<=0:
		level=0
		man.health=10
	if level==0:
		win.blit(stscreen,(0,0))
		text("stt",75,"sttt","START",(0,255,0),420,300)
		pygame.draw.rect(win,(255,0,0),(405,290,220,70),10)
	elif level==1:
		win.blit(bgA,(0,0))
		win.blit(p1A,(840,450))
		win.blit(blockM,(0,650))
		win.blit(blockM,(50,650))
		win.blit(blockM,(100,650))
		win.blit(blockM,(150,650))
		win.blit(blockM,(200,650))
		win.blit(blockM,(0,600))
		win.blit(blockM,(0,550))
		win.blit(blockM,(50,600))
		win.blit(blockM,(50,550))
		win.blit(blockM,(100,600))
		win.blit(blockM,(100,550))
		win.blit(blockM,(150,600))
		win.blit(blockM,(150,550))
		win.blit(blockM,(200,600))
		win.blit(blockM,(200,550))
		win.blit(blockM,(345,650))
		win.blit(blockM,(395,650))
		win.blit(blockM,(345,600))
		win.blit(blockM,(345,550))
		win.blit(blockM,(395,600))
		win.blit(blockM,(395,550))
		win.blit(blockM,(540,650))
		win.blit(blockM,(540,600))
		win.blit(blockM,(540,550))
		win.blit(blockM,(685,650))
		win.blit(blockM,(685,600))
		win.blit(blockM,(685,550))
		win.blit(blockM,(735,650))
		win.blit(blockM,(735,600))
		win.blit(blockM,(735,550))
		win.blit(blockM,(785,650))
		win.blit(blockM,(785,600))
		win.blit(blockM,(785,550))
		win.blit(blockM,(835,650))
		win.blit(blockM,(835,600))
		win.blit(block2M,(835,550))
		
		man.draw(win)
		if man.x>220 and man.y<700 and man.y>489 and man.x<310:
			fall=True
		elif man.x>425 and man.y<700 and man.y>489 and man.x<505:
			fall=True
		elif man.x>570 and man.y<700 and man.y>489 and man.x<650:
			fall=True
		elif man.x>860 and man.y<700 and man.y>489 and man.x<1000:
			fall=True
		else:
			fall=False
			if man.isJump==False:
				man.y=490
		if man.x>800 and man.y<600 and man.y>489 and man.x<860:
			level=2
			man.x=10
			left=False 
			right=False
		for bullet in bullets:
			if level==1:
			    bullet.draw(win)
	elif level==2:
		win.blit(bgA,(0,0))
		man.draw(win)
		win.blit(blockM,(0,650))
		win.blit(blockM,(50,650))
		win.blit(blockM,(0,600))
		win.blit(blockM,(0,550))
		win.blit(blockM,(50,600))
		win.blit(blockM,(50,550))
		win.blit(grass1,(170,460))
		win.blit(grass1,(540,390))
		win.blit(p1A,(935,410))
		win.blit(block2M,(940,510))
		if man.x>70 and man.y<700 and man.y>470 and man.x<=132:
			fall=True
		elif man.x>440 and man.y<700 and man.y>400 and man.x<=502:
			fall=True
		elif man.x>817 and man.y<700 and man.y>330 and man.x<=910:
			fall=True
		else:
			fall=False
			if man.x<=132 and man.isJump==False:
				man.y=490
			elif man.x>132 and man.x<=502 and man.isJump==False:
				man.y=430
			elif man.x>502 and man.x<817 and man.isJump==False:
				man.y=360
			elif man.x>910 and man.x<1000 and man.isJump==False:
				man.y=420
			if man.x>910 and man.y==420:
				level=3
				man.x=10
				man.y=60
				left=False 
				right=False
		for bullet in bullets:
			if level==2:
			    bullet.draw(win)
	elif level==3:
		win.blit(bgA,(0,0))
		if level==3:
			goblin.draw(win)
		man.draw(win)
		win.blit(blockM,(0,120))
		win.blit(blockM,(50,120))
		win.blit(grass2,(170,200))
		win.blit(grass3,(485,300))
		win.blit(p1A,(940,245))
		if man.x>910 and man.y==277:
			level=4
			man.x=50
			man.y=210
			left=False 
			right=False
		if man.x<=70 and man.isJump==False and level==3:
			man.y=60
		elif man.x>=155 and man.x<395 and man.y<300 and man.isJump==False and level==3:
			man.y=157
		elif man.x>=475 and man.x<1000 and man.isJump==False and level==3:
			man.y=277	
		if man.x>70 and man.y<250 and man.x<155 and man.y>50:
			fall=True
		elif man.x>=395 and man.y<500 and man.x<475 and man.y>=150:
			fall=True 
		elif man.x<71 and man.y>250:
			fall=True
		for bullet in bullets:
			if level==3:
			    bullet.draw(win)
	elif level==4:
		win.blit(bgA,(0,0))
		win.blit(blockM,(50,270))
		man.draw(win)
		win.blit(p1A,(0,180))
		win.blit(block2M,(0,270))
		win.blit(grass3,(170,220))
		win.blit(p2A,(640,165))
		for bullet in bullets:
			if level==4:
			    bullet.draw(win)
		if man.x<20 and man.y==210:
			level=5
		elif man.x>625 and man.x<=640 and man.y==210:
			level=1
			man.x=10 
			man.y=490
			left=False 
			right=False
		elif man.x>90 and man.x<163 and man.y>205:
			fall=True 
		elif man.x>640 and man.y>205:
			fall=True
		if man.x<=90 and man.y>210: 
		    man.y=210
		    man.x=50
			
	elif level==5:
		win.blit(bgA,(0,0))
		win.blit(p1A,(840,450))
		win.blit(blockM,(0,650))
		win.blit(blockM,(50,650))
		win.blit(blockM,(100,650))
		win.blit(blockM,(150,650))
		win.blit(blockM,(200,650))
		win.blit(blockM,(0,450))
		win.blit(blockM,(50,450))
		win.blit(blockM,(100,450))
		win.blit(blockM,(150,450))
		win.blit(blockM,(200,450))
		win.blit(blockM,(0,500))
		win.blit(blockM,(50,500))
		win.blit(blockM,(100,500))
		win.blit(blockM,(150,500))
		win.blit(blockM,(200,500))
		win.blit(blockM,(0,450))
		win.blit(blockM,(50,450))
		win.blit(blockM,(100,450))
		win.blit(blockM,(150,450))
		win.blit(blockM,(200,450))
		win.blit(blockM,(0,400))
		win.blit(blockM,(50,400))
		win.blit(blockM,(100,400))
		win.blit(blockM,(150,400))
		win.blit(blockM,(200,400))
		win.blit(blockM,(0,800))
		win.blit(blockM,(50,800))
		win.blit(blockM,(100,800))
		win.blit(blockM,(150,800))
		win.blit(blockM,(200,800))
		win.blit(blockM,(0,350))
		win.blit(blockM,(50,350))
		win.blit(blockM,(100,350))
		win.blit(blockM,(150,350))
		win.blit(blockM,(200,350))
		win.blit(blockM,(0,300))
		win.blit(blockM,(50,300))
		win.blit(blockM,(100,300))
		win.blit(blockM,(150,300))
		win.blit(blockM,(200,300))
		win.blit(blockM,(0,600))
		win.blit(blockM,(0,550))
		win.blit(blockM,(50,600))
		win.blit(blockM,(50,550))
		win.blit(blockM,(100,600))
		win.blit(blockM,(100,550))
		win.blit(blockM,(150,600))
		win.blit(blockM,(150,550))
		win.blit(blockM,(200,600))
		win.blit(blockM,(200,550))
		win.blit(blockM,(345,650))
		win.blit(blockM,(395,650))
		win.blit(blockM,(345,600))
		win.blit(blockM,(345,550))
		win.blit(blockM,(395,600))
		win.blit(blockM,(395,550))
		win.blit(blockM,(540,650))
		win.blit(blockM,(540,600))
		win.blit(blockM,(540,550))
		win.blit(blockM,(685,650))
		win.blit(blockM,(685,600))
		win.blit(blockM,(685,550))
		win.blit(blockM,(735,650))
		win.blit(blockM,(735,600))
		win.blit(blockM,(735,550))
		win.blit(blockM,(785,650))
		win.blit(blockM,(785,600))
		win.blit(blockM,(785,550))
		win.blit(blockM,(835,650))
		win.blit(blockM,(835,600))
		win.blit(block2M,(835,550))
		man.draw(win)
		if man.x>220 and man.y<241 and man.y>219 and man.x<310:
			fall=True
		elif man.x>425 and man.y<700 and man.y>489 and man.x<505:
			fall=True
		elif man.x>570 and man.y<700 and man.y>489 and man.x<650:
			fall=True
		elif man.x>860 and man.y<700 and man.y>489 and man.x<1000:
			fall=True 
		else:
			fall=False
			if man.isJump==False and man.x<=220:
				man.y=240
			elif man.isJump==False and man.x>=310 and man.x<=425:
				man.y=490
		if man.x>800 and man.y<600 and man.y>489 and man.x<860:
			pygame.quit()
			man.x=10
			left=False 
			right=False
		for bullet in bullets:
			if level==5:
			    bullet.draw(win)
		pet.draw(win,pets,man.x,man.y,man.left,man.right,400,520)
		if man.x>360 and man.y==490 and man.isJump==False:
			pets=True 
	pygame.display.update()

man = player(5, 490, 64,64)
pet=dog(True,300,490,80,70,man.x,man.y,1000)
goblin = enemy(460, 285, 64, 64, 925)
shootLoop=0
bullets = []

def first_mouse_button_is_down():
    pygame.event.get()
    return pygame.mouse.get_pressed()[0]

def check_release():
    if not first_mouse_button_is_down():
        return False
    while first_mouse_button_is_down():
        pass
    return True

run=True
while run:
	clock.tick(27)
	if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and goblin.visible==True and level==3:
	    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
	       man.hit()
	       score -= 10
	       goblin.health=10

	if shootLoop>0:
	   shootLoop+=1
	if shootLoop>3:
		shootLoop=0
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			mx,my=pygame.mouse.get_pos()
			if mx>=405 and mx<=625 and my>=290 and my<=360 and level==0:
				level=1
			if mx>1035 and mx<1140 and my>190 and my<335 and level>0:
				if left==True:
					left=False 
				elif left==False:
					left=True 
					right=False
			elif mx>1150 and mx<1225 and my>190 and my<335 and level>0 :
				if right==True:
					right=False 
				elif right==False:
					right=True 
					left=False
			if mx>1085 and mx<1180 and my>330 and my<500 and level>0:
				man.isJump=True 
			if mx>1085 and mx<1187 and my>130 and my<180:
				if man.left:
					facing = -1
				else:
					facing = 1
				if len(bullets) < 5:
				    bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (255,255,100), facing))
				    shootLoop=1

	#if left==True and man.x>5:
#		man.x -= man.vel
#		man.left = True
#		man.right = False
#		man.standing = False 
#	elif right==True and man.x < 1000 - man.width - man.vel:
#		man.x += man.vel
#		man.right = True
#		man.left = False
#		man.standing = False 
#	else:
#	   man.standing = True
#	   man.walkCount = 0
		
	for bullet in bullets:
         try:
         	if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1] and level==3:
         		if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
         			goblin.hit()
         			bullets.pop(bullets.index(bullet))
         			score+=1
         	'''
         	if bullet.y-bullet.radius<goblin2.hitbox[1]+goblin2.hitbox[3] and bullet.y+bullet.radius>goblin2.hitbox[1]:
         	    if bullet.x+bullet.radius>goblin2.hitbox[0] and bullet.x-bullet.radius<goblin2.hitbox[0]+goblin2.hitbox[2]:
         	    	h_sound.play()
         	    	goblin2.hit()
         	    	score+=1
         	    	bullets.pop(bullets.index(bullet))
         	if bullet.y-bullet.radius<goblin3.hitbox[1]+goblin3.hitbox[3] and bullet.y+bullet.radius>goblin3.hitbox[1]:
         		if bullet.x+bullet.radius>goblin3.hitbox[0] and bullet.x-bullet.radius<goblin3.hitbox[0]+goblin3.hitbox[2]:
         			h_sound.play()
         			goblin3.hit()
         			score+=1
         			bullets.pop(bullets.index(bullet))
         	'''
         except:
         	f=1
         if bullet.x < 990 and bullet.x > 5:
         	bullet.x += bullet.vel
         else:
         	bullets.pop(bullets.index(bullet))
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_b] and shootLoop==0) :
	   if man.left:
	       facing = -1
	   else:
	       facing = 1
	   if len(bullets) < 5:
	       bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (255,255,100), facing))
	       shootLoop=1
	if (keys[pygame.K_d] and man.x > man.vel) or (left==True and man.x>5):
	   man.x -= man.vel
	   man.left = True
	   man.right = False
	   man.standing = False
	elif (keys[pygame.K_f] and man.x < 1000 - man.width - man.vel) or (right==True and man.x < 1000 - man.width - man.vel):
	    man.x += man.vel
	    man.right = True
	    man.left = False
	    man.standing = False
	else:
	   man.standing = True
	   man.walkCount = 0
	if not(man.isJump):
	   if keys[pygame.K_r]:
	       man.isJump = True
	       man.right = False
	       man.left = False
	       man.walkCount = 0
	else:
	    if man.jumpCount >= -10:
	        neg = 1
	        if man.jumpCount < 0:
	           neg = -1
	        man.y -= (man.jumpCount ** 2) * 0.5 * neg
	        man.jumpCount -= 1
	    else:
	        man.isJump = False
	        man.jumpCount = 10
	if fall==True:
		if level==3:
			goblin.health=10
		man.isJump=False 
		left=False 
		right=False
		man.jumpCount=10
		man.walkCount=0
		man.y -= (man.fall ** 1) * 0.39 * -1
		man.fall-=1
		if man.fall<=0:
			fall=False
			man.fall=100
	if man.y>640:
		man.x=10
		man.y=490
		man.health-=1
		score-=1
		left=False 
		right=False
		fall=False
	DrawGameWindow()
	
pygame.quit()
