import pygame


pygame.init()
pygame.font.init()

size = width, height =int(536),int(819)
orange=(255,135,0)
white=(255,255,255)
black = (0,0,0)

#########
# init to add
self.week = ['Sun','Mon','Tus','Wed','Thr','Fri','Sat']
self.userImg = pygame.image.load('orange.png')
self.instaImg = pygame.image.load('instagram.png')
self.snapImg = pygame.image.load('snapchat1.png')
self.fbImg = pygame.image.load('fb1.png')
self.oImg = pygame.image.load('o.png')
self.friendImg = pygame.image.load('login1.png')
self.messageImg = pygame.image.load('bubble.png')


##############

def sign(self):
    screen.fill(self.grey)
    screen.blit(self.userImg,(80,70))
    loginScreen.blit(self.fbImg,(118,700))
    loginScreen.blit(self.instaImg,(235.3,700))
    loginScreen.blit(self.snapImg,(353,700))


# this gives an animation of our logo
def subpage(self):
    screen.fill(self.grey)
    self.drawShades(self.white,0,0,self.width,60)
        
def drawShades(self,color, a, b, c, d):
        pygame.draw.rect(screen,(160,160,160),(a-7,b-7,c+14,d+14))
        pygame.draw.rect(screen,(170,170,170),(a-6,b-6,c+12,d+12))
        pygame.draw.rect(screen,(190,190,190),(a-5,b-5,c+10,d+10))
        pygame.draw.rect(screen,(210,210,210),(a-4,b-4,c+8,d+8))
        pygame.draw.rect(screen,(230,230,230),(a-3,b-3,c+6,d+6))
        pygame.draw.rect(screen,(240,240,240),(a-2,b-2,c+4,d+4))
        pygame.draw.rect(screen,(250,250,250),(a-1,b-1,c+2,d+2))
        pygame.draw.rect(screen, color, (a,b,c,d))

def drawCalendarButton(self,color, fontColor, a, b, c, d, text, width = 0, font):
        pygame.draw.rect(screen, color, (a,b,c,d), width)
        myFont = font
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/2, b + d/2)
        screen.blit(textSurface, textRect1)

def drawLeftRightButton(self, color, loc):
    pygame.draw.polygon(screen, color, loc)


def calendarMarch(self):
    self.subpage()
    x = -223
    y = 100
    self.drawCalendarButton(grey, orange, 250+x, 10+y, 480, 50, "March, 2018",self.regularFont)
    self.drawLeftRightButton(orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
    self.drawLeftRightButton(orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
    for i in range(7):
        self.drawCalendarButton(grey,white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
        day = 29
        for i in range(5):
            for j in range(7):
                if i == 0 and j < 4: continue
                if i ==0 and j == 4:
                    day = 1
               # if calendarColor[i][j] == 0 :
                        # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                self.drawCalendarButton(grey, orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
               # if calendarColor[i][j] == 1:
                    #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                    #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                day = day + 1

            #if recordMode == 11:
              #  pygame.draw.rect(screen, orange, (250+x, 90+y,480 ,380))
              #  myfont = pygame.font.SysFont('Comic Sans MS', 30)
              #  textSurface = myFont.render("Date: Nov." + str(self.recordMode) + 'th', True, grey)
              #  textRect1 = textSurface.get_rect()
              #  textRect1.midleft = (300+x, 150+y)
              #  screen.blit(textSurface, textRect1)
              #  #Good

              #  myfont = pygame.font.SysFont('Comic Sans MS', 30)
              #  textSurface1 = myFont1.render("Condition : " + "Fair", True, grey)
              #  textRect2 = textSurface1.get_rect()
              #  textRect2.midleft = (300+x, 200+y)
              #  screen.blit(textSurface1, textRect2)
    screen.blit(self.oImg, (80,700))

def calendarApril(self):
    week = ['Sun', 'Mon', 'Tus', 'Wed', 'Thr', 'Fri', 'Sat']
    subpage()
    x = -223
    y = 100
    drawCalendarButton(grey, orange, 250+x, 10+y, 480, 50, "April, 2018",self.regularFont)
    drawLeftRightButton(orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
    drawLeftRightButton(orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
    for i in range(7):
        drawCalendarButton(grey,white,250 + i * 70+x, 90+y, 60, 30, week[i], self.weekFont)

        day = 29
        for i in range(5):
            for j in range(7):
                if i == 4 and j > 2: continue
                if i ==0 and j == 0:
                    day = 1
               # if calendarColor[i][j] == 0 :
                        # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                drawCalendarButton(grey, orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
               # if calendarColor[i][j] == 1:
                    #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                    #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                day = day + 1

            #if recordMode == 11:
              #  pygame.draw.rect(screen, orange, (250+x, 90+y,480 ,380))
              #  myfont = pygame.font.SysFont('Comic Sans MS', 30)
              #  textSurface = myFont.render("Date: Nov." + str(self.recordMode) + 'th', True, grey)
              #  textRect1 = textSurface.get_rect()
              #  textRect1.midleft = (300+x, 150+y)
              #  screen.blit(textSurface, textRect1)
              #  #Good

              #  myfont = pygame.font.SysFont('Comic Sans MS', 30)
              #  textSurface1 = myFont1.render("Condition : " + "Fair", True, grey)
              #  textRect2 = textSurface1.get_rect()
              #  textRect2.midleft = (300+x, 200+y)
              #  screen.blit(textSurface1, textRect2)
    screen.blit(self.oImg, (80,700))

def calendarMay(self):
    self.subpage()
    x = -223
    y = 100
    drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50, "May, 2018", self.regularFont)
    drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
    drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
    for i in range(7):
        drawCalendarButton(self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, week[i], self.weekFont)

        day = 29
        for i in range(5):
            for j in range(7):
                if i == 0 and j < 2 or i == 4 and j > 4: continue
                if i ==0 and j == 2:
                    day = 1
               # if calendarColor[i][j] == 0 :
                        # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                drawCalendarButton(self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
               # if calendarColor[i][j] == 1:
                    #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                    #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                day = day + 1
    screen.blit(self.oImg, (80,700))
    
def communityFriends(self):
    self.subpage()
    screen.blit(self.friendImg,(20,180))
    screen.blit(self.friendImg,(20,380))
    screen.blit(self.friendImg,(20,580))
    screen.blit(self.messageImg, (140,150))
    screen.blit(self.messageImg, (140,350))
    screen.blit(self.messageImg, (140,550))

def calendarYes(self):
    self.subpage()
    x = -223
    y = 150
    yw = 0
    for i in range(7):
        drawCalendarButton(self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
    drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50,"April 6, 2018", self.regularFont)
    drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
    drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
    
def calendarNo(self):
    self.subpage()
    x = -223
    y = 150
    yw = 0
    for i in range(7):
        drawCalendarButton(self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
    drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50,"April 6, 2018", self.regularFont)
    drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
    drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
    screen.blit(self.oImag,(170, 500))
    displayText('"An Orange A Day',20,150,500,500,self.orange)
    displayText('   Keeps Doctors Away"',20,220,500,500,self.black)
    

def displayText(text,a,b,c,d,fontColor):
    myFont = pygame.font.SysFont('Comic Sans MS', self.cuteFont)
    textSurface = myFont.render(text, True, fontColor)
    textRect1 = textSurface.get_rect()
    textRect1.center = (a + c/2, b + d/2)
    screen.blit(textSurface, textRect1)
    

    