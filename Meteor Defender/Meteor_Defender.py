#Phillipe Lothaller[4460820] and Stephan Schmidt[4671724]

#AE1205 Bonus Project
import pygame as pg
import math
import sys
import random
from pygame.locals import *

#Initialize pygame
pg.init()

#Icon
icon = pg.image.load("icon.png")
pg.display.set_caption("Meteor Defender")
pg.display.set_icon(icon)
icon.set_colorkey((255, 255, 255))

Super_Run = True
Super_Start = True
Super_Game = False
Super_Lose = False

SuperSong = pg.mixer.music.load("Undertale-Megalovania.ogg")
pg.mixer.music.play(-1,0)
while Super_Run == True:
    if Super_Start == True:
        #Start screen
        pg.init()
        pg.font.init()

        #Colours
        white = (255,255,255)
        black = (0,0,0)

        #Font

        gtitlefont = pg.font.SysFont('Retro Computer', 60) 
        titlefont = pg.font.SysFont('Retro Computer', 45)
        bodyfont = pg.font.SysFont('Retro Computer', 18)

        #Pygame window
        xmax = 1000
        ymax = 700
        start_scr  =  pg.display.set_mode((xmax,ymax))
        background =  pg.image.load("BackStart.png").convert()

        #defaults

        mpos = (0,0)

        #Game boxes

        start_box = pg.image.load("Start.png")
        startrect = start_box.get_rect()
        startrect1 = pg.Rect.inflate(startrect,0,20)

        hs_box = pg.image.load("HighScore.png")
        hsrect = hs_box.get_rect()
        hsrect1 = pg.Rect.inflate(hsrect,0,20)

        help_box = pg.image.load("Help.png")
        helprect = help_box.get_rect()
        helprect1 = pg.Rect.inflate(helprect,0,20)

        credit_box = pg.image.load("Credits.png")
        creditrect = credit_box.get_rect()
        creditrect1 = pg.Rect.inflate(creditrect,0,20)

        exit_box = pg.image.load("Exit.png")
        exitrect = exit_box.get_rect()
        exitrect1 = pg.Rect.inflate(exitrect,0,20)

        back_box = pg.image.load("Back.png")
        backrect = back_box.get_rect()
        backrect1 = pg.Rect.inflate(backrect,0,20)
        #Help screen boxes

        leftwalk = pg.image.load("L-Walk3.png")
        leftwalkrect = leftwalk.get_rect()

        rightwalk = pg.image.load("R-Walk3.png")
        rightwalkrect = rightwalk.get_rect()

        boost = pg.image.load("R-Boost.png")
        boostrect = boost.get_rect()

        shield = pg.image.load("shield.png")
        shieldrect = shield.get_rect()

        charge = pg.image.load("Recharge.png")
        chargerect = charge.get_rect()

        #Meteorite image, postion and speed
        metpic  = pg.image.load("1-Met-Large.png")
        metrect = metpic.get_rect()
        x       = 100
        y       = 100
        vx      = 400
        vy      = 100

        #Picture
        bobby = pg.image.load("MenuBob.png")
        bobbyrect = bobby.get_rect()
        xb = 0.8*xmax
        yb  = 0.5*ymax
        vyb = 50


        #Time
        t = pg.time.get_ticks()*0.001

        #Loop
        running = True
        while running:

            #Event pump
            pg.event.pump()

            #Timer
            t0 = t
            t  = pg.time.get_ticks()*0.001
            dt = t-t0
            tr = t+dt

            #Speed intergration for meteorite

            x = x + vx*dt
            y = y + vy*dt

            if x>xmax and vx>0:
                x=xmax
                vx=-vx
            if x<0 and vx<0:
                x=0
                vx=-vx

            if y>ymax and vy>0:
                y=ymax
                vy = -vy
            if y<0 and vy<0:
                y=0
                vy=-vy

            #Speed integration for bobby

            yb = yb + vyb*dt

            if yb<0.3*ymax and vyb<0:
                yb = 0.3*ymax
                vyb = -vyb
            if yb>0.7*ymax and vyb>0:
                yb=0.7*ymax
                vyb = -vyb

            #Mouse click

            mclick = pg.mouse.get_pressed()
            
            if mclick[0] == True:
                mpos = pg.mouse.get_pos()

                if startrect.collidepoint(mpos) == True:
                    running = False
                    break

                #Highscore screen
                
                if hsrect.collidepoint(mpos) == True:
                    running = False
                    hsrunning = True

                    f = open('HIgh_Scores.txt','r')
                    lines = f.readlines()
                    f.close()

                    Scores = []
                    List = []
                    for s in lines:
                        List.append(s)
                        Scores.append(float(s[s.find('\t')+1:-1]))
                        
                    for count in range(len(Scores)-1,0,-1):
                        for count2 in range(count):
                            if Scores[count2]>Scores[count2 + 1]:
                                temp = Scores[count2]
                                Scores[count2] = Scores[count2+1]
                                Scores[count2+1] = temp
                                temp2 = List[count2]
                                List[count2] = List[count2+1]
                                List[count2+1] = temp2
                    

                    while hsrunning:

                        keys = pg.key.get_pressed()

                        start_scr.fill(black)
                        start_scr.blit(background,(0,0))
                        
                        textsurface = titlefont.render('High scores', False, white)
                        textsurface_rect = textsurface.get_rect()
                        textsurface_rect.center = (xmax/2,100)
                        start_scr.blit(textsurface,textsurface_rect)



                        for i in range(10):

                            textsurface1 = bodyfont.render(List[-i-1], False, white)
                            textsurface_rect1 = textsurface1.get_rect()
                            textsurface_rect1.center = (xmax/2,250 + i*30)
                            start_scr.blit(textsurface1,textsurface_rect1)


                        mclick = pg.mouse.get_pressed()
                        cursorpos = pg.mouse.get_pos()
                        
                        if mclick[0] == True:
                            mpos = pg.mouse.get_pos()    

                        backrect.center = (70,70)
                        backrect1.center = (70,70)

                        if backrect.collidepoint(cursorpos) == True:
                            start_scr.blit(back_box,backrect1)
                        else:
                            start_scr.blit(back_box,backrect)

            
                        pg.display.flip()
                        if backrect.collidepoint(mpos) == True:
                            hsrunning = False
                            running = True



                        if keys[pg.K_ESCAPE]:
                            hsrunning = False
                            running = True

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                hsrunning = False
                                running = True

                #Help screen
                                
                if helprect.collidepoint(mpos) == True:
                    running = False
                    helprunning = True
                    while helprunning:
                        keys = pg.key.get_pressed()
                        start_scr.fill(black)
                        start_scr.blit(background,(0,0))
                        
                        textsurface = titlefont.render('Help', False, white)
                        textsurface_rect = textsurface.get_rect()
                        textsurface_rect.center = (xmax/2,50)
                        start_scr.blit(textsurface,textsurface_rect)
                        

                        leftwalkrect.center = (xmax/4,150)
                        start_scr.blit(leftwalk,leftwalkrect)

                        btextsurface = bodyfont.render("[A] Moves left", False, white)
                        btextsurface_rect = btextsurface.get_rect()
                        btextsurface_rect = (310,150-15)
                        start_scr.blit(btextsurface,btextsurface_rect)

                        rightwalkrect.center = (xmax/4,250)
                        start_scr.blit(rightwalk,rightwalkrect)

                        btextsurface1 = bodyfont.render("[D] Moves right", False, white)
                        btextsurface1_rect = btextsurface1.get_rect()
                        btextsurface1_rect = (310,250-15)
                        start_scr.blit(btextsurface1,btextsurface1_rect)               

                        boostrect.center = (xmax/4,350)
                        start_scr.blit(boost,boostrect)

                        btextsurface2 = bodyfont.render("[W] Boost, helps to jump between platforms", False, white)
                        btextsurface2_rect = btextsurface2.get_rect()
                        btextsurface2_rect = (310,350-15)
                        start_scr.blit(btextsurface2,btextsurface2_rect)                

                        shieldrect.center = (xmax/4,450)
                        start_scr.blit(shield,shieldrect)

                        btextsurface3 = bodyfont.render("[Space Bar] Shield, protects you from Meteorites", False, white)
                        btextsurface3_rect = btextsurface3.get_rect()
                        btextsurface3_rect = (310,450-15)
                        start_scr.blit(btextsurface3,btextsurface3_rect)                

                        chargerect.center = (xmax/4,550)
                        start_scr.blit(charge,chargerect)

                        btextsurface4 = bodyfont.render("Collect to recharge shield power", False, white)
                        btextsurface4_rect = btextsurface4.get_rect()
                        btextsurface4_rect= (310,550-15)
                        start_scr.blit(btextsurface4,btextsurface4_rect)

                        btextsurface6 = bodyfont.render("You only start with 3 shield chrages, and each shield lasts 3 seconds", False, white)
                        btextsurface6_rect = btextsurface6.get_rect()
                        btextsurface6_rect.center= (xmax/2,610)
                        start_scr.blit(btextsurface6,btextsurface6_rect) 

                        btextsurface5 = bodyfont.render("Dont let the meteors touch you! Or else its game over.", False, white)
                        btextsurface5_rect = btextsurface5.get_rect()
                        btextsurface5_rect.center= (xmax/2,645)
                        start_scr.blit(btextsurface5,btextsurface5_rect) 

                        mclick = pg.mouse.get_pressed()
                        cursorpos = pg.mouse.get_pos()
                        
                        if mclick[0] == True:
                            mpos = pg.mouse.get_pos()    

                        backrect.center = (70,70)
                        backrect1.center = (70,70)

                        if backrect.collidepoint(cursorpos) == True:
                            start_scr.blit(back_box,backrect1)
                        else:
                            start_scr.blit(back_box,backrect)

            
                        pg.display.flip()
                        if backrect.collidepoint(mpos) == True:
                            helprunning = False
                            running = True



                        if keys[pg.K_ESCAPE]:
                            helprunning = False
                            running = True


                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                helprunning = False
                                running = True        

                #Credit screen
                                
                if creditrect.collidepoint(mpos) == True:
                    running = False
                    creditrunning = True
                    while creditrunning:
                        keys = pg.key.get_pressed()
                        start_scr.fill(black)
                        start_scr.blit(background,(0,0))

                        textsurface = titlefont.render('Credits', False, white)
                        textsurface_rect = textsurface.get_rect()
                        textsurface_rect.center = (xmax/2,100)
                        start_scr.blit(textsurface,textsurface_rect)

                        lst = ['Meteor defender was developed by Stephan Schmidt and ','Phillipe Lothaller in the scope of the AE1205 - Python bonus project.',
                               'All sprites were made by Stephan Schmidt.','Music was sourced from Toby Fox - MEGLAVONIA']


                        for i in range(len(lst)):

                            btextsurfacei = bodyfont.render(lst[i], False, white)
                            btextsurfacei_rect = btextsurfacei.get_rect()
                            btextsurfacei_rect.center = (xmax/2,250 + i*30)
                            start_scr.blit(btextsurfacei,btextsurfacei_rect)

                        lst2 = ['The developers would like thank Professor Hoekstra,','Professor Van Paassen and the AE1205 tutors for the continued support.']

                        for j in range(len(lst2)):

                            btextsurfacej = bodyfont.render(lst2[j], False, white)
                            btextsurfacej_rect = btextsurfacej.get_rect()
                            btextsurfacej_rect.center = (xmax/2,400 + j*30)
                            start_scr.blit(btextsurfacej,btextsurfacej_rect)

                        mclick = pg.mouse.get_pressed()
                        cursorpos = pg.mouse.get_pos()
                        
                        if mclick[0] == True:
                            mpos = pg.mouse.get_pos()    

                        backrect.center = (70,70)
                        backrect1.center = (70,70)

                        if backrect.collidepoint(cursorpos) == True:
                            start_scr.blit(back_box,backrect1)
                        else:
                            start_scr.blit(back_box,backrect)

            
                        pg.display.flip()
                        if backrect.collidepoint(mpos) == True:
                            creditrunning = False
                            running = True

        
                        if keys[pg.K_ESCAPE]:
                            creditrunning = False
                            running = True

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                creditrunning = False
                                running = True

                #Exit Button
                                
                if exitrect.collidepoint(mpos) == True:
                    running = False
                    Super_Run = False
                    break
                    pg.quit()
                
            #Mouse postion

            cursorpos = pg.mouse.get_pos()
                
            #Clear screen
            start_scr.fill(black)

            #Draw background
            start_scr.blit(background,(0,0))

            #Draw meteroite
            metpicr = pg.transform.rotate(metpic,tr*100)
            metrect = metpicr.get_rect()
            metrect.center = (x,y)
            start_scr.blit(metpicr,metrect)

            #Draw game boxes
            
            startrect.center = ((xmax/2), (ymax/2 - 3*startrect[3]+50))
            startrect1.center = ((xmax/2), (ymax/2 - 3*startrect[3]+50))

            if startrect.collidepoint(cursorpos) == True:
                start_scr.blit(start_box,startrect1)
            else:
                start_scr.blit(start_box,startrect)

            hsrect.center = ((xmax/2), (ymax/2 - 1.5*hsrect[3]+50))
            hsrect1.center = ((xmax/2), (ymax/2 - 1.5*hsrect[3]+50))

            if hsrect.collidepoint(cursorpos) == True:
                start_scr.blit(hs_box,hsrect1)
            else:
                start_scr.blit(hs_box,hsrect)
               
            helprect.center = (xmax/2,ymax/2+50)
            helprect1.center = ((xmax/2), (ymax/2)+50)

            if helprect.collidepoint(cursorpos) == True:
                start_scr.blit(help_box,helprect1)
            else:
                start_scr.blit(help_box,helprect)

            creditrect.center = ((xmax/2), (ymax/2 + 1.5*creditrect[3]+50))
            creditrect1.center = ((xmax/2), (ymax/2 + 1.5*creditrect[3]+50))

            if creditrect.collidepoint(cursorpos) == True:
                start_scr.blit(credit_box,creditrect1)
            else:
                start_scr.blit(credit_box,creditrect)

            exitrect.center = ((xmax/2), (ymax/2 + 3*exitrect[3]+50))
            exitrect1.center = ((xmax/2), (ymax/2 + 3*exitrect[3]+50))

            if exitrect.collidepoint(cursorpos) == True:
                start_scr.blit(exit_box,exitrect1)
            else:
                start_scr.blit(exit_box,exitrect)
         
            #Draw Bobby
            bobbyrect.center = (xb,yb)
            start_scr.blit(bobby,bobbyrect)

            #Draw Title
            textsurface = gtitlefont.render('Meteor Defender', False, white)
            textsurface_rect = textsurface.get_rect()
            textsurface_rect.center = (xmax/2,100)
            start_scr.blit(textsurface,textsurface_rect)
            
            
            #Update screen
            pg.display.flip()

            #catch quite event
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    Super_Start = False
                    Super_Run = False

        if startrect.collidepoint(mpos) == True:
            running = False
            Super_Start = False
            Super_Game = True
            
##
##==================================================================================================================================================================
##==================================================================================================================================================================
##==================================================================================================================================================================

    if Super_Game == True:
        
        def walk(drc,idx,flg):
            sidx = idx
            if idx == 0:
                sidx = 2
            if flg == True:
                idx += 1
                if idx > 3:
                    idx = 0

            pcls  =  drc+"-walk"+str(sidx)+".png"
            return idx,pcls


        #Colours
        white = (255,255,255)
        black = (60,70,70)

        #constants
        VR1 = 50
        VR2 = 200
        g0 = 9.80665 * 80
        cax = 800
        vmax = 300
        acax = 0

        ttot = 0

        wtime = 0

        jtime = 0
        jump = False
        drc = "R"
        pcls = "R-walk2.png"
        fall = True
        PlatNum = 4
        MetNum = 1

        Shields = 3
        shldflg = False
        stime = 0
        sa,sb = 42.5,28.5
        Contactlst = []
        tlst = []

        rtime = 0
        rlim = 3
        rinc = 2
        netcharge = 0
        chrgstep = 1

        mtime = 0
        mlim = 5
        mdec = -1
        mmax = 1

        #Pygame window
        xmax = 1000
        ymax = 700
        scr  = pg.display.set_mode((xmax,ymax))
        bg = pg.image.load("Backup.png").convert()

        #Simulation loop
        t = pg.time.get_ticks()*0.001

        #Paddle initialization
        paddlelst = []
        xlst = []
        ylst = []
        paddleV = []
        dxpaddle = xmax/8
        dypaddle = 3
        countlst = [random.randint(1,8)]
        '''Randomises the locations of the paddles in the list so that the random process truly is random
        eg paddle 1 would always have 100% in the loop below, so random it ''' 
        for count in list(range(7)):        
            cflag = True                    
            while cflag == True:
                cflag = False
                testval = random.randint(1,8)
                for val in countlst:
                    if testval == val:
                        cflag = True
            countlst.append(testval)

        probability = 0                     
        '''This is where the magic happens, randomises where the platforms should be. they are alwasy evenly divided.
        with a max number of panels of 8'''
        for count in list(range(8)):        
            bplat = random.randint(0,100)   
            if bplat >= probability:
                xlst.append((countlst[count] - 0.5)*dxpaddle)
                ylst.append(random.randint(10, ymax))
                paddleV.append(random.randint(VR1,VR2))
                paddlelst.append(pg.Rect(0,0,dxpaddle,dypaddle))
                probability += 10           
        '''Every time a panel is added the likely hood decreases by 10% (i think...im not actually good at stats)'''        

        #Sprite Platform instansisation
        '''create a list with all the pngs, then a lists from 1=>PlatNum for every plat so we only have 4 sprites instead of 8 or whatever'''
        paddlesprites = []
        spriterect = []
        for count in list(range(len(paddlelst))):                          
            paddlesprites.append(pg.image.load("Plat"+str(random.randint(1,PlatNum))+".png"))
            spriterect.append(paddlesprites[count].get_rect())
        sw,sh = paddlesprites[0].get_size()
        sh = sh/2
        sw = sw/2

        #Char Instantiazation
        idx     =   2
        xc      =   xlst[0]
        yc      =   0
        vxc     =   0 #acc 50px/s^2 maybe
        vyc     =   0
        pc      =   pg.image.load("R-walk2.png")
        cHB     =   pc.get_rect()
        cw,ch   =   pc.get_size()
        ch      =   ch/2
        cw      =   cw/2

        #Shield Instantiazation
        '''Spawn the meteors first'''
        xs = xc
        ys = yc
        shld = pg.image.load("shield.png")
        shldHB = shld.get_rect()

        #Meteor
        MetRad = 17
        Spawnwait = 5000
        Metdt = 0
        MetVX,MetVY,MetX,MetY,MetSpritelst,MetLst,MetHB,MetLstUp = [],[],[],[],[],[],[],[]
        for count in list(range(MetNum)):                          
            MetSpritelst.append(pg.image.load(str(random.randint(1,MetNum))+"-Met.png"))

        #Recharge
        Recharge = pg.image.load("Recharge.png")
        chrgX,chrgY,chrges,chrgHB = [],[],[],[]

        #Frame Rate Counter
        myfont = pg.font.SysFont("monospace", 30)

        #==========================================================================================================
        #Loop
        running = True
        while running:
          
            #Clock
            t0 = t
            t  = pg.time.get_ticks()*0.001
            dt = t-t0
            Metdt += dt
            tr = t+dt

            #Time updates
            for count in list(range(len(tlst))):
                tlst[count] += dt
                
            #Event pump
            pg.event.pump()

            #Clear screen
            scr.fill(black)

            #Charge creation
            rtime += dt
            if rtime > rlim:
                rtime = 0
                rlim += rinc
                chrges.append(Recharge)
                chrgHB.append(chrges[-1].get_rect())
                chrgX.append(random.randint(int(0.5*dxpaddle),int(7.5*dxpaddle)))
                chrgY.append(random.randint(ch*2,ymax-ch*2))

            #Meteor creation
            mtime += dt
            if mtime > mlim and len(MetX)<=7:
                mtime = 0
                if mlim > mmax:
                    mlim += mdec
                MetLst.append(MetSpritelst[random.randint(0,len(MetSpritelst)-1)])
                MetLstUp.append(MetLst[-1])
                MetHB.append(MetLst[-1].get_rect())
                MetVX.append(random.randint(-212,212))
                MetVY.append(random.randint(106,212))
                MetX.append(random.randint(10,xmax-10))
                if MetX[-1] <= xc+20 and MetX[-1] >= xc-20:
                    MetX[-1] = MetX[-1] - 50
                MetY.append(0)
                
            
        #Affects
            #Gravity change for char
            g = 0.5*g0/ymax*yc + 0.5*g0 #gravity changes with altitude

            #Contact check
            Contact = cHB.collidelist(paddlelst)

            #Charge Contact
            ChrgContact = cHB.collidelist(chrgHB)

            #Met Contact
            MetContact = cHB.collidelist(MetHB)

            #Shield/Met Contact
            ShldContact = shldHB.collidelist(MetHB)


        #ANIMATIONS    
            #Walk timer
            wflg = False
            wtime += dt
            if wtime > 0.15:
                wflg = True
                wtime = 0

            #jump animation
            if jump == True and Contact == -1:
                pc = pg.image.load(drc+"-Boost.png")
            
            #jump timer
            if jump == True and Contact != -1 and yc-8<ylst[Contact] and vyc >= paddleV[Contact]:
                jump = False
                pc = pg.image.load(pcls)

            #Fall stopper
            if fall == True and Contact != -1:
                fall = False
                pc = pg.image.load(pcls)
                    
            #Fall Animation
            if fall == True and Contact == -1:
                pc = pg.image.load(drc+"-Fall.png")

            #SHIELD TIMER
            if shldflg == True:
                shldHB.center = (xc,yc-ch)
                stime += dt
                if stime > 3:
                    shldflg = False
                    stime = 0

            #SHIELD CONTACT
            if ChrgContact > -1:
                chrgHB.remove(chrgHB[ChrgContact])
                chrgX.remove(chrgX[ChrgContact])
                chrgY.remove(chrgY[ChrgContact])
                Shields += 1

            #MET/SHIELD CONTACT
            for count in Contactlst:
                if ShldContact == count or MetContact == count:
                    ShldContact = -1
                    MetContact = -1

            if shldflg == True and ShldContact > -1:
                MetLst[ShldContact] = pg.image.load("Met-Debris.png")
                MetLstUp[ShldContact] = pg.image.load("Met-Debris.png")
                Contactlst.append(ShldContact)
                tlst.append(dt) 

            for count in Contactlst:
                if ShldContact == count or MetContact == count:
                    ShldContact = -1
                    MetContact = -1
                    
            track = 0
            for count in list(range(len(tlst))):
                if tlst[count - track] > 2:
                    del MetLst[Contactlst[count - track]]
                    del MetLstUp[Contactlst[count - track]]
                    del MetHB[Contactlst[count - track]]
                    del MetVX[Contactlst[count - track]]
                    del MetVY[Contactlst[count - track]]
                    del MetX[Contactlst[count - track]]
                    del MetY[Contactlst[count - track]]
                    del tlst[count - track]
                    mem = Contactlst[count - track]
                    del Contactlst[count - track]
                    track += 1
                    for count2 in list(range(len(Contactlst))):
                        if Contactlst[count2] > mem:
                           Contactlst[count2] = Contactlst[count2]-1 
                            
                    
        #KEY INPUTS
            WalkFlag = False
            keys = pg.key.get_pressed()
            #LEFT
            if keys[pg.K_a]:
                drc = "L"
                WalkFlag = True
                if vxc > 0:
                    vxc = 0
                acax = -cax
                if vxc >= -vmax:
                    vxc = vxc + acax*dt
                else:
                    vxc = -vmax
            #RIGHT
            if keys[pg.K_d]:
                drc = "R"
                WalkFlag = True
                if vxc < 0:
                    vxc = 0
                acax = cax
                if vxc <= vmax:
                    vxc = vxc + acax*dt
                else:
                    vxc = vmax
            #JUMP
            if keys[pg.K_w]:
                if jump == False:
                    fall = False
                    vyc = -500
                    jump = True

            #SHIELD
            if keys[pg.K_SPACE] and shldflg==False and Shields > 0:
                shldflg = True
                Shields += -1
                
        #POSITION UPDATES
            
            #y-position of char
            if Contact != -1 and jump == False and yc-8<ylst[Contact] and vyc >= paddleV[Contact]:
                fall = False
                vyc = paddleV[Contact]
                ax = 300
            else:
                if jump == False:
                    fall = True
                vyc = vyc + g*dt
                ax = 80
                
            yc = yc + vyc*dt

            if yc >= ymax+ch:
                yc = -ch

            if yc <= -50 and vyc < 0:
                vyc = 0

            #x-position of char
            if WalkFlag == False and abs(vxc*dt) <= 0.005:
                vxc = 0

            if vxc > 0:
                vxc = vxc - ax*dt
            if vxc < 0:
                vxc = vxc + ax*dt
            xc = xc + vxc*dt 

            if jump == False and fall ==False and vxc != 0 :
                idx,pcls = walk(drc,idx,wflg)
                pc = pg.image.load(pcls)
            
            if vxc == 0 and fall == False and jump == False:
                pc = pg.image.load(drc+"-walk2.png")

            if xc >= xmax+2*cw:
                xc = -cw
            if xc <= -cw*2:
                xc = xmax+cw

        #WORLD DESIGN
            #background
            '''WHY IS THIS CAUSING SUCH FRAME LOSS!'''
            '''Fixed it :D'''
            scr.blit(bg,(0,0)) 

            #Position of paddle
            for count in list(range(len(ylst))):
                ylst[count] = ylst[count] + paddleV[count]*dt
                if ylst[count]<=ch*2 or ylst[count]>=ymax:
                    if ylst[count] <= ch*2 and paddleV[count] < 0:
                        paddleV[count] = -paddleV[count]
                    elif ylst[count] >= ymax and paddleV[count] > 0:
                        paddleV[count] = -paddleV[count]

                    #HERE LIES PHILS CODE. MAY IT RIP
                        
            #Draw paddle
            for count in list(range(len(ylst))):
                paddlelst[count].center = (xlst[count],ylst[count])
        ##        pg.draw.rect(scr,white,paddlelst[count])
                spriterect[count].center = (xlst[count],ylst[count]+sh)
                scr.blit(paddlesprites[count],spriterect[count])
                    #HERE LIES MORE OF PHILS SHITTY CODE RIP
         
            #Spawn Char
            cHB.center = (xc,yc-ch) 
            scr.blit(pc,cHB)
            if shldflg == True:
                scr.blit(shld,shldHB)

            #Draw charges
            netcharge += chrgstep
            if abs(netcharge) == 50:
                chrgstep = chrgstep * -1
                netcharge = 0
            for count in list(range(len(chrgX))):
                chrgY[count] += 0.12*chrgstep
                chrgHB[count].center = (chrgX[count],chrgY[count])
                scr.blit(chrges[count],chrgHB[count])

            #Meteor flying
            for count in list(range(len(MetX))):
                MetX[count] = MetX[count] + MetVX[count]*dt
                MetY[count] = MetY[count] + MetVY[count]*dt

                if MetX[count]>xmax and MetVX[count]>0:
                    MetX[count]=xmax
                    MetVX[count]=-MetVX[count]
                if MetX[count]<0:
                    MetVX[count]=-MetVX[count]

                if MetY[count]>ymax and MetVY[count]>0:
                    MetY[count]=ymax
                    MetVY[count]=-MetVY[count]
                if MetY[count]<0:
                    MetVY[count]=-MetVY[count]


                MetLstUp[count] = pg.transform.rotate(MetLst[count],tr*50)
                MetHB[count] = MetLst[count].get_rect()
                MetHB[count].center = (MetX[count],MetY[count])
                scr.blit(MetLstUp[count],MetHB[count])

            #Framerate
            scr.blit(myfont.render( 'Charges: ' + str(Shields)+ ' Time: ' + str(round(ttot,3)), 1, (255,255,0)), (50, 50)) 
            scr.blit(myfont.render( 'Charge time: ' + str(int(3-stime)), 1, (255,255,0)), (50, ymax-50))
            #str(round(1/dt if dt > 0 else 60))

            #Update screen
            pg.display.update()

            #catch quite event
            for event in pg.event.get():
                if event.type == QUIT:
                    Super_Game = False
                    Super_Lose = True
                    running = False

            #EXIT
            if keys[pg.K_ESCAPE]:
                running = False
                Super_Game = False
                Super_Lose = True

            #SCORE
            if MetContact > -1:
                running = False
                Super_Game = False
                Super_Lose = True
            else:
                ttot += dt

    if Super_Lose == True:
        #Start screen
        pg.init()
        pg.font.init()

        #Colours
        white = (255,255,255)
        black = (0,0,0)

        #Font
        gtitlefont = pg.font.SysFont('Retro Computer', 60) 
        titlefont = pg.font.SysFont('Retro Computer', 45)
        bodyfont = pg.font.SysFont('Retro Computer', 33)

        #Pygame window
        xmax = 1000
        ymax = 700
        scr  =  pg.display.set_mode((xmax,ymax))
        background =  pg.image.load("BackStart.png").convert()    

        #Time
        t = pg.time.get_ticks()*0.001

        Name = '' #We're engineers not literature students, please dont judge the spelling
        ttot = round(ttot,3)
        running = True
        CursTime = 0
        Curs = '_'
        jumpvar = 12
        cursjump = jumpvar
        t  = pg.time.get_ticks()*0.001
        kt = 0
        kflag = False
        while running == True:

            #Clock
            t0 = t
            t  = pg.time.get_ticks()*0.001
            dt = t-t0


            
            #Event pump
            pg.event.pump()

            #Clear screen
            scr.fill(black)
            
            scr.blit(background,(0,0))

            #Timer for cursor
            CursTime += dt
            if CursTime > 0.8:
                CursTime = 0
                if Curs == '_':
                    Curs = ' '
                    cursjump = 0
                else:
                    Curs = '_'
                    cursjump = jumpvar
            
            keys = pg.key.get_pressed()
            if kflag == True:
                kt += dt
                if kt > 0.15:
                    kflag = False
                    kt = 0
            if sum(keys) > 0 and kflag == False:
                    if keys.index(1) == 8:
                        Name = Name[:-1]
                    elif len(Name) <= 8 and keys.index(1) >= 97 and keys.index(1) <= 122 :
                        Name = Name + chr(keys.index(1))
                    kflag = True

                    

                    
            textsurface = gtitlefont.render('Game Over', False, white)
            textsurface_rect = textsurface.get_rect()
            textsurface_rect.center = (xmax/2,100)
            scr.blit(textsurface,textsurface_rect)
            
            textsurface1 = bodyfont.render('You survived for ' + str(ttot) + ' seconds', False, white)
            textsurface_rect1 = textsurface1.get_rect()
            textsurface_rect1.center = (xmax/2,250)
            scr.blit(textsurface1,textsurface_rect1)

            textsurface2 = titlefont.render('Your Name: ' + Name + Curs, False, white)
            textsurface_rect2 = textsurface2.get_rect()
            textsurface_rect2.center = (xmax/2 + cursjump,350)
            scr.blit(textsurface2,textsurface_rect2)
            for event in pg.event.get():
                if event.type == QUIT:
                    running = False
                    Super_Lose = False
                    Super_Start = True

            #EXIT
            if keys[pg.K_ESCAPE] or keys[pg.K_RETURN]:
                running = False
                Super_Lose = False
                Super_Start = True

            #Update screen
            pg.display.flip()


        #File Update
        if Name == '':
            Name = 'Anonymus'
        f = open("HIgh_Scores.txt","a")
        f.write(Name + '\t' + str(ttot)+ '\n')
        f.close()
#Close window
pg.quit()
        
