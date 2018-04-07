
import os
import pygame

class InputBox(object):
    def __init__(self, x, y, w, h,listAddedTo,font):
        self.rect = pygame.Rect(x, y, w, h)
        self.width= w
        self.colorActive=(255,135,0)
        self.colorInactive=(240,190,98)
        self.color = self.colorInactive
        self.text = ""
        self.txtSurface = font.render(self.text, True, self.color)
        self.active = False
        self.listAddedTo=listAddedTo

    def handleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.colorActive if self.active else self.colorInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.listAddedTo+=self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.width, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
            
class InterestBox(object):
    def __init__(self,x,y,w,h,text,screen):
        self.x,self.y,self.w,self.h,self.text=x,y,w,h,text
        self.color=(255,255,255)
        self.orange=(255,135,0)
        self.screen=screen
    
    def draw(self):
        box=(self.x,self.y,self.w,self.h)
        pygame.draw.rect(screen,self.orange,box)
        self.screen.blit(self.font.render(self.text,True,self.color,(x+10,y+5)))
            

class PygameGame(object):
   
    # Helpers
    # Init functions
    def initColor(self):
        self.white = (255,255,255)

        #self.deepBlue= (68,118,192)
        #self.darkBlue  = (51,87,117)
        self.grey=(99,99,112)
        self.orange=(222,141,71)
        
        self.blueGray = self.hex_to_rgb("#343f51")
        self.deepBlueGray = self.hex_to_rgb("#2e3242")
        self.darkBlueGray = self.hex_to_rgb("#1b2331")
        
        self.lightOrange=(240,190,98)
        self.orange = (255,135,0)  #normal
        self.darkOrange = (221,111,15)   #motion
        self.deepOrange = (0,0,0)  #pressed
    
    def within(self,left,down,width,height,x,y):
        return left < x < left+width and down < y < down +height

    def hex_to_rgb(self,value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        
    def loadFont(self):
        self.regularFont = pygame.font.SysFont("Arvo-Bold.ttf",35)
        self.buttonFont = pygame.font.SysFont("Arvo-Bold.ttf",30)
        self.calendarFont=pygame.font.SysFont("Arvo-Bold.ttf",25)
        self.weekFont=pygame.font.SysFont("Arvo-Bold.ttf",20)
        self.cuteFont = pygame.font.SysFont("EastSeaDokdo-Regular.ttf",30)

#############################
#all button
#############################

    def signButtons(self):
        width= 300
        height = 40
        gap = 20
        first_button_y = 475
        first_button_x = 118
        self.signInBtn = [first_button_x,first_button_y,width,height, self.orange]
        self.signUpBtn = [first_button_x,first_button_y+gap+height,width,height,self.orange]

    def interestButtons(self):
        gap=10
        btnHeight=35
        self.interestButtonList=[]
        for i in range(0,len(self.interestList)):
            lenText=len(self.interestList[i])
            self.interestButtonList+=InterestBox(43,30+btnHeight*i+gap*i,\
                                                lenText*10+20,btnHeight,\
                                                self.interestList[i])
                                                
    def mainButtons(self):
        width=150
        gap=20
        self.mainEvent1=[43,140,450,width,self.white]
        self.mainEvent2=[43,140+width+gap,450,width,self.white]
        self.mainEvent3=[43,140+width*2+gap*2,450,width,self.white]
        self.mainCircle=[self.orange,218,779,70]
        self.mainCommunityBtn=[0,739,141,80,self.orange]
        self.mainCalendarBtn=[295,739,241,80,self.orange]
        
        
    def handButtons(self):
        self.titleInput()
        self.dateInput()
        self.beginTimeInput()
        self.endTimeInput()
        self.locationInput()
        self.descriptionInput()
        
   # def finishButtons(self):
   #     self.
        
    
    #def calendarButtons(self):
        #xh
        
    
    def buttons(self):
        self.interestInput()
        self.signButtons()
        self.interestButtons()
        self.mainButtons()
        self.handButtons
        self.importButtons=[self.orange,(268,500),200]
        #self.finishButtons()
        #self.calendarButtons()
        self.friendEventBtn=[118,100,300,200,self.orange]
        self.localEventBtn=[118,350,300,200,self.orange]
        self.preferenceBtn=[118,475,300,40,self.orange]
        self.handCircle=[self.orange,(160,679),40]
        self.libraryInputCircle=[self.orange,(268,639),40]
        self.cameraCircle=[self.orange,(376,679),40]
    
      
##############################
#text input boxes
##############################
    def interestInput(self):
        #text input box at interest input page
        self.interestList=[]
        boxWidth=450
        boxHeight=35
        self.interestInputBox=InputBox(43,70,boxWidth,boxHeight,self.interestList,self.regularFont)
        
    def titleInput(self):
        self.titleText=""
        boxWidth=450
        boxHeight=35
        self.titleInputBox=InputBox(43,70,boxWidth,boxHeight,self.titleText,self.regularFont)
        
    def dateInput(self):
        self.dateText=""
        boxWidth=200
        boxHeight=35
        self.dateInputBox=InputBox(43,125,boxWidth,boxHeight,self.dateText,self.regularFont)
        
    def beginTimeInput(self):
        self.beginTimeText=""
        boxWidth=100
        boxHeight=35
        self.beginTimeInputBox=InputBox(43,180,boxWidth,boxHeight,self.beginTimeText,self.regularFont)
    
    def endTimeInput(self):
        self.endTimeText=""
        boxWidth=100
        boxHeight=35
        self.endTimeInputBox=InputBox(158,180,boxWidth,boxHeight,self.endTimeText,self.regularFont)
    
    def locationInput(self):
        self.locationText=""
        boxWidth=200
        boxHeight=35
        self.locationInputBox=InputBox(43,235,boxWidth,boxHeight,self.locationText,self.regularFont)
        
    def descriptionInput(self):
        self.descriptionText=""
        boxWidth=450
        boxHeight=100
        self.descriptionInputBox=InputBox(43,290,boxWidth,boxHeight,self.descriptionText,self.regularFont)

#########################
### Main Framework ######
#########################
    def init(self):
        self.mode = "sign"
        self.initColor()
        self.signButtons()
        self.loadFont()
        self.initBtnList=[self.signInBtn,self.signUpBtn]
        #14 modes 
        self.modeLst=["sign","interest","main","hand","libraryInput","camera"\
                      "calendar","working","finish","calendarYes","calendarNo",\
                      "calendarMarch","calendarMay","community"\
                      "communityFriends","preference","threeIcon"]
        self.path = None
        self.buttons()
        self.week = ['Sun','Mon','Tus','Wed','Thr','Fri','Sat']
        self.userImg = pygame.image.load('orange.png')
        self.instaImg = pygame.image.load('instagram.png')
        self.snapImg = pygame.image.load('snapchat1.png')
        self.fbImg = pygame.image.load('fb1.png')
        self.oImg = pygame.image.load('o.png')
        self.friendImg = pygame.image.load('login1.png')
        self.messageImg = pygame.image.load('bubble.png')
        self.backImg = pygame.image.load('back4.png')
        self.addImg = pygame.image.load('add3.png')
        self.doneImg = pygame.image.load('done2.png')
        self.mannualImg = pygame.image.load('manual2.png')
        self.searImg = pygame.image.load('search1.png')
        self.setImg = pygame.image.load('set2.png')
        self.calImg = pygame.image.load('calendar1.png')
        self.comImg = pygame.image.load('community1.png')
        
        #self.loadLogo()  xh
        #self.loadShareLogo() xh

#### MousePressed ####
    def mousePressedSign(self,x,y):
        if self.mode=="sign":
            #signInBtn
            surface= self.initBtnList[0]
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
            #signUpBtn
            surface=self.initBtnList[1]
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
                
    def mousePressedMain(self,x,y):
        if self.mode=="main":
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.deepOrange
            
            btn=self.mainCommunityBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.deepOrange
                
            btn=self.mainCalendarBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.deepOrange
                
    def mousePressedThreeIcon(self,x,y):
        if self.mode=="threeIcon":
            if (x-160)**2+(y-679)**2<=1600:
                self.handCircle[0]=self.deepOrange
            
            if (x-268)**2+(y-639)**2<=1600:
                self.libraryInputCircle[0]=self.deepOrange
                
            if (s-376)**2+(y-679)**2<=1600:
                self.cameraCircle[0]=self.deepOrange
                
    def mousePressedLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-268)**2+(y-500)**2<=200**2:
                surface[1]=self.deepOrange
                
    # def mousePressCalendar(self,x,y):
    #     if self.mode=="calendar":
    #         #xh
    #             
    def mousePressedCommunity(self,x,y):
        if self.mode=="community":
            surface=self.friendEventBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
            
            surface=self.localEventBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
            
    def mousePressedPreference(self,x,y):
        if self.mode=="preference":
            surface=self.preferenceBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
                
    def mousePressed(self,x,y):
        self.mousePressedSign(x,y)
        self.mousePressedLibraryInput(x,y)
        #self.mousePressCalendar(x,y)
        self.mousePressedCommunity(x,y)
        self.mousePressedPreference(x,y)
        self.mousePressedThreeIcon(x,y)
        self.mousePressedMain(x,y)
        
#### Open File Browser ####
    def open_file_browser(self):
        pygame.mixer.init()  # initializing the mixer
        import tkinter
        from tkinter import filedialog

        root = tkinter.Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        return root.filename

#### MouseReleased ####
    def mouseReleasedSign(self,x,y):
        if self.mode=="sign":
            #signInBtn
            surface= self.initBtnList[0]
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
            #signUpBtn
            surface=self.initBtnList[1]
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
                self.mode="interest"
    
    def mouseReleasedMain(self,x,y):
        if self.mode=="main":
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.orange
                self.mode="threeIcon"
            
            btn=self.mainCommunityBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.orange
                self.mode="community"
                
            btn=self.mainCalendarBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.orange
                self.mode="calendar"
                
    def mouseReleasedThreeIcon(self,x,y):
        if self.mode=="threeIcon":
            if (x-160)**2+(y-679)**2<=1600:
                self.handCircle[0]=self.orange
                data.mode="hand"
            
            if (x-268)**2+(y-639)**2<=1600:
                self.libraryInputCircle[0]=self.orange
                data.mode="libraryInput"
                
            if (s-376)**2+(y-679)**2<=1600:
                self.cameraCircle[0]=self.orange
                data.mode="camera"
            
    # def mouseReleasedCalendar(self,x,y):
    
    def mouseReleasedLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-268)**2+(y-500)**2<=200**2:
                surface[1]=self.orange
                self.path=self.open_file_browser()
                if self.path!="":
                    self.mode="working"
    
    def mouseReleasedBack(self,x,y):
        if self.within(0,0,60,40,x,y):
            if self.mode=="interest":
                self.mode="sign"
            elif self.mode=="libraryInput":
                self.mode="main"
            elif self.mode=="camera":
                self.mode="main"
            elif self.mode=="hand":
                self.mode="main"
            elif self.mode=="community":
                self.mode="main"
            elif self.mode=="calendar":
                self.mode="main"
            elif self.mode=="calendarYes":
                self.mode="calendar"
            elif self.mode=="calendarNo":
                self.mode="calendar"
            elif self.mode=="finish":
                self.mode="libraryInput"
            elif self.mode=="friendEvent":
                self.mode="community"
                
    def mouseReleasedDone(self,x,y):
        if self.within(536-60,0,60,40,x,y):
            if self.mode=="finish":
                self.mode="main"
            elif self.mode=="hand":
                self.mode="main"
            elif self.mode=="interest":
                self.mode="main"
                
    def mouseReleasedPreference(self,x,y):
        if self.mode=="preference":
            surface=self.preferenceBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
                data.mode="communityFriends"
    
   # def mouseReleasedMonthChange(self,x,y):
   
            
    def mouseReleased(self,x,y):
        self.mouseReleasedSign(x,y)
        #self.mouseReleasedCalendar(x,y)
        self.mouseReleasedLibraryInput(x,y)
        self.mouseReleasedBack(x,y)
        self.mouseReleasedDone(x,y)
        self.mouseReleasedPreference(x,y)
        self.mouseReleasedThreeIcon(x,y)
        self.mouseReleasedMain(x,y)
        print(self.mode)
        
#### MouseMotion ####
    def mouseMotionSign(self,x,y):
        if self.mode=="sign":
            for btn in self.initBtnList:
                if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                    btn[4]=self.darkOrange
                else:
                    btn[4]=self.orange 

    def mouseMotionInterest(self,x,y):
        if self.mode=="interest":
            if len(self.interestButtonList)!=0:
                for btn in self.interestButtonList:
                    if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                        btn[4]=self.darkOrange
                    else:
                        btn[4]=self.orange 
                
    def mouseMotionMain(self,x,y):
        if self.mode=="main":
            for btn in [self.mainEvent1,self.mainEvent2,self.mainEvent3]:
                if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                    btn[4]=self.darkOrange
                else:
                    btn[4]=self.orange 
        
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.darkOrange
            else:
                self.mainCircle[0]=self.orange
            
            btn=self.mainCommunityBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange
            
            btn=self.mainCalendarBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange
            
    def mouseMotionThreeIcon(self,x,y):
        if self.mode=="threeIcon":
            if (x-160)**2+(y-679)**2<=1600:
                self.handCircle[0]=self.darkOrange
            else:
                self.handCircle[0]=self.orange
            
            if (x-268)**2+(y-639)**2<=1600:
                self.libraryInputCircle[0]=self.darkOrange
            else:
                self.libraryInputCircle[0]=self.orange
                
            if (x-376)**2+(y-679)**2<=1600:
                self.cameraCircle[0]=self.darkOrange
            else:
                self.cameraCircle[0]=self.orange
                
    def mouseMotionLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x_218)**2+(y-500)**2<=200**2:
                surface[1]=self.darkOrange
            else:
                surface[1]=self.orange
    
    # def mouseMotionFinish(self,x,y):
    #     if self.mode=="finish":
            
    def mouseMotionCommunity(self,x,y):
        if self.mode=="community":
            btn=self.friendEventBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
                
            btn=self.localEventBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
        
    # def mouseMotionCalendar(self,x,y):
    #     if self.mode=="calendar":
    #         #xh
            
    def mouseMotionPreference(self,x,y):
        if self.mode=="preference":
            btn=self.preferenceBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 

    def mouseMotion(self, x, y):
        self.mouseMotionSign(x,y)
        self.mouseMotionInterest(x,y)
        self.mouseMotionMain(x,y)
        self.mouseMotionLibraryInput(x,y)
        self.mouseMotionCommunity(x,y)
        #self.mouseMotionCalendar(x,y)
        self.mouseMotionPreference(x,y)
        self.mouseMotionThreeIcon(x,y)

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass
        
        


#### timerFried ####

    def timerFired(self, dt):
        pass
        
###########################
#draw
###########################
    def drawSignButtons(self,screen):
        pygame.draw.rect(screen, self.signInBtn[4], self.signInBtn[:4])
        pygame.draw.rect(screen, self.signUpBtn[4], self.signUpBtn[:4])
        
    def drawSign(self,screen):
        screen.fill(self.grey)
        screen.blit(self.userImg,(80,70))
        screen.blit(self.fbImg,(118,700))
        screen.blit(self.instaImg,(235.3,700))
        screen.blit(self.snapImg,(353,700))

    def drawBackBtn(self,screen):
        screen.blit(self.backImg,(0,0))
        
    def drawAddBtn(self,screen):
        screen.blit(self.addImg, (546,0))
        
    def drawDoneBtn(self,screen):
        screen.blit(self.doneImg, (546,0))
        
    # remember to input
    def drawMannualBtn(self,screen):
        screen.blit(self.mannualImg, ())
        
    # remember to input
    def drawSearchBtn(self,screen):
        screen.blit(self.searImg, ())
        
    # remember to input
    def drawSettingBtn(self,screen):
        screen.blit(self.setImg, (546,0))
        
    # remember to input
    def drawCalBtn(self,screen):
        screen.blit(self.calImg, ())
        
    # remember to input    
    def drawComBtn(self,screen):
        screen.blit(self.comImg, ())
    # add
    def drawEventBtn(self,screen,color,loc):
        pygame.draw.rect(screen,color,loc)
        
    
        
    def drawMainBtn(self,screen):
        pygame.draw.rect(screen,self.orange,(0,739,536,80))
        pygame.draw.circle(screen,self.mainCircle[0],(268,779),80)

        

        
    def drawSubpage(self,screen):
        screen.fill(self.grey)
        self.drawShades(screen,self.white,0,0,self.width,50)
        
    def drawShades(self, screen, color, a, b, c, d):
            pygame.draw.rect(screen,(160,160,160),(a-7,b-7,c+14,d+14))
            pygame.draw.rect(screen,(170,170,170),(a-6,b-6,c+12,d+12))
            pygame.draw.rect(screen,(190,190,190),(a-5,b-5,c+10,d+10))
            pygame.draw.rect(screen,(210,210,210),(a-4,b-4,c+8,d+8))
            pygame.draw.rect(screen,(230,230,230),(a-3,b-3,c+6,d+6))
            pygame.draw.rect(screen,(240,240,240),(a-2,b-2,c+4,d+4))
            pygame.draw.rect(screen,(250,250,250),(a-1,b-1,c+2,d+2))
            pygame.draw.rect(screen, color, (a,b,c,d))
            
    def drawCalendarButton(self,screen,color, fontColor, a, b, c, d, text,font, width = 0):
            pygame.draw.rect(screen, color, (a,b,c,d), width)
            myFont = font
            textSurface = myFont.render(text, True, fontColor)
            textRect1 = textSurface.get_rect()
            textRect1.center = (a + c/2, b + d/2)
            screen.blit(textSurface, textRect1)
                
    def drawLeftRightButton(self,screen, color, loc):
        pygame.draw.polygon(screen, color, loc)
    
    def calendarMarch(self,screen):
        self.drawSubpage()
        x = -223
        y = 100
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50, "March, 2018",self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 0 and j < 4: continue
                    if i ==0 and j == 4:
                        day = 1
                # if calendarColor[i][j] == 0 :
                            # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                    self.drawCalendarButton(screen,self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                # if calendarColor[i][j] == 1:
                        #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                        #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    day = day + 1
        screen.blit(self.oImg, (80,700))
    
    def calendarApril(self,screen):
        
        self.drawSubpage(screen)
        x = -223
        y = 100
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50, "April, 2018",self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.white,250 + i * 70+x, 90+y, 60, 30,self.week[i], self.weekFont)
    
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 4 and j > 2: continue
                    if i ==0 and j == 0:
                        day = 1
                # if calendarColor[i][j] == 0 :
                            # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                    self.drawCalendarButton(screen,self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
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
    
    def calendarMay(self,screen):
        self.drawSubpage()
        x = -223
        y = 100
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50, "May, 2018", self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
    
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 0 and j < 2 or i == 4 and j > 4: continue
                    if i ==0 and j == 2:
                        day = 1
                # if calendarColor[i][j] == 0 :
                            # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                    self.drawCalendarButton(screen,self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                # if calendarColor[i][j] == 1:
                        #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                        #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    day = day + 1
        screen.blit(self.oImg, (80,700))
        
    def drawCommunityFriends(self):
        self.drawSubpage()
        screen.blit(self.friendImg,(20,180))
        screen.blit(self.friendImg,(20,380))
        screen.blit(self.friendImg,(20,580))
        screen.blit(self.messageImg, (140,150))
        screen.blit(self.messageImg, (140,350))
        screen.blit(self.messageImg, (140,550))
        
    def calendarYes(self):
        self.drawSubpage()
        x = -223
        y = 150
        yw = 0
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50,"April 6, 2018", self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        
    def calendarNo(self):
        self.drawSubpage()
        x = -223
        y = 150
        yw = 0
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50,"April 6, 2018", self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        screen.blit(self.oImag,(170, 500))
        self.displayText(screen,'"An Orange A Day',20,150,500,500,self.orange,self.cuteFont)
        self.displayText(screen,'   Keeps Doctors Away"',20,220,500,500,self.black,self.cuteFont)
        
    def displayText(self,screen,text,a,b,c,d,fontColor,font):
        myFont = font
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/2, b + d/2)
        screen.blit(textSurface, textRect1)
        
                
############### redraw ####
    def redrawSign(self, screen):
        self.drawSign(screen)
        self.drawSignButtons(screen)
    
    def redrawInterest(self, screen):
        self.drawSubpage(screen)
    
    def redrawMain(self, screen):
        screen.fill(self.grey)
        self.displayText(screen,"Latest Events", 43,60,100,100,self.white,self.regularFont)
        self.drawMainBtn(screen)
        self.drawEventBtn(screen,self.mainEvent1[4],self.mainEvent1[:4])
        self.drawEventBtn(screen,self.mainEvent2[4],self.mainEvent2[:4])
        self.drawEventBtn(screen,self.mainEvent3[4],self.mainEvent3[:4])
    
    def redrawHand(self,screen):
        self.drawSubpage(screen)

    def redrawLibraryInput(self,screen):
        self.drawSubpage(screen)
        pygame.draw.circle(screen,self.importButtons[0],self.importButtons[1],self.importButtons[2])
        self.displayText(screen,"Input",self.importButtons[1][0],self.importButtons[1][0],500,500,self.white,self.regularFont)
    
    #def redrawCamera(self,screen):
        # use open cv
    
    def redrawCalendar(self,screen):
        self.calendarApril(screen)
    
    def redrawCalendarMarch(self,screen):
        self.calendarMarch(screen)
        
    def redrawCalendarMay(self,screen):
        self.calendarMay(screen)
    
    def redrawWorking(self,screen):
        pass
    
    def redrawFinish(self,screen):
        pass
        
    def redrawCalendarYes(self,screen):
        self.calendarYes(screen)
    
    def redrawCalendarNo(self,screen):
        self.canlendarNo(screen)
        
    def redrawCommunity(self,screen):
        pass
        
    def redrawCommunityFriends(self,screen):
        self.drawCommunityFriends(screen)
        
    def redrawPreference(self,screen):
        pass
        
    def redrawAll(self, screen):
        if self.mode=="sign":
            self.redrawSign(screen)
        elif self.mode=="interest":
            self.redrawInterest(screen)
        elif self.mode=="main":
            self.redrawMain(screen)
        elif self.mode=="libraryInput":
            self.redrawLibraryInput(screen)
        elif self.mode=="camera":
            self.redrawCamera(screen)
        elif self.mode=="hand":
            self.redrawHand(screen)
        elif self.mode=="community":
            self.redrawCommunity(screen)
        elif self.mode=="calendar":
            print('ere')
            self.redrawCalendar(screen)
        elif self.mode=="calendarYes":
            self.redrawCalendarYes(screen)
        elif self.mode=="calendarNo":
            self.redrawCalendarNo(screen)
        elif self.mode=="finish":
            self.redrawFinish(screen)
        elif self.mode=="communityFriends":
            self.redrawCommunityFriends(screen)
        

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=536, height=819, fps=50, title="BlackOrange"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (99,99,112)

        pygame.init()
        

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print("yes")
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons[0] == 1):
                #     self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()



def main():
    game = PygameGame(536,819)
    game.run()

if __name__ == '__main__':
    main()