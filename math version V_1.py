#Math Challenge Defense of the Mathematics Castle Game
#Based on model created by callaboration of Thien Trandinh and Serjan Kairosh
#Copyright of Thien Trandinh
#Date created: May 20th, 2013
#Date last modified: June 17th, 2013

grid = "gamesBackground.jpg"
archer = "Archer.png"
goblin = "Goblin.png"
arrow = "arrow.png"
explosion = "explosion.png"

import pygame, sys, time, random
from random import randint
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500,600), 0, 32);

#Loading images
background = pygame.image.load(grid).convert()
hero = pygame.image.load(archer).convert_alpha()
monster = pygame.image.load(goblin).convert_alpha()
charArrow = pygame.image.load(arrow).convert_alpha()
impact = pygame.image.load(explosion).convert_alpha()
#_______________________________________________________________________________

#Declaring variables variables
x,y = 10,10
movex, movey, arrowx, arrowy = 0,0,0,0
delayBoolean = 0
arrowShootBoolean=0
health = 400
monsterHealth = 150
arrowX, arrowY=11,12
arrowCounter=0
score = 0
levelCounter =1
add1,add2,add3 = 0,0,0
addCounter=0
subtract1,subtract2,subtract3=0,0,0
subtractCounter=0
multiplication1,multiplication2,multiplication3=0,0,0
multiplicationCounter=0
division1,division2,division3=0,0,0
divisionCounter=0
monsterX = 0
monsterY = 0
randDirection = 0
randDirection = 0
count = 3
#_______________________________________________________________________________

#Introduce program:
print "Welcome to Defense of the Mathematics Castle"
print "Solve math questions to attack and slay the invading monsters"
print "in the name of math!"
print "Hit the monsters with your arrows to damage and eventually kill it"
print "A new one will then respawn"
print "But be careful, the monsters will grow increasingly stronger with each death"
print "When a monster hits you, you will lose healthand eventually lose. Run fast!"
print "Take turns with your friends and compete for the best high scores!"
print " "
print "Controls:"
print "Click A,D,W,S to move left, right, up and down respectively"
print "To attack, you must solve the math question and press the corresponding keys"
print "to attack in a certain direction"
print "O and P for right, T and Y for left, U and I for up, and J and K for down"
print " "
print "*TIP: Is there a hard question that you need time to think about?"
print "Run as far away from a monster cas you can: They'll only chase you "
print "within a certain range"

#Addition method - finds 2 random int, returns the 2 int and their sum
def add():
    add1 = randint(1,20)
    add2 = randint(1,20)
    add3 = add1+add2
    
    return add1,add2,add3
#Addition method - finds 2 random int, returns the 2 int and difference sum
def subtract():
    subtract2 = randint(1,10)
    subtract1 = subtract2+(randint(1,10)) #Makes sure first number is larger then second number which results in positive difference
    subtract3 = subtract1-subtract2
    
    return subtract1,subtract2,subtract3
#Addition method - finds 2 random int, multiplies the 2 and returns them
def multiplication():
    multiplication1 = randint(1,10)
    multiplication2 = randint(1,10)
    multiplication3 = multiplication1*multiplication2
    
    return multiplication1,multiplication2,multiplication3
#Division method - finds 2 random int, multiplies the 2 and returns them in this order ( x / y = z   ->  divide1 / divide2 = divide3)
def division():
    divide2 = randint(1,10)
    divide3 = randint(1,10)
    divide1 = divide2*divide3
    
    return divide1,divide2,divide3


                   

#printing initial label for health and score
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render(str(health), 1, (255,0,0))
label2 = myfont.render(str(monsterHealth),1,(255,0,0))
labelScore = myfont.render(str(score), 1, (255,0,0))
labelLevel = myfont.render(str(levelCounter), 1, (255,0,0))
ScoreLabel = myfont.render(str("Score"), 1, (255,0,0))
LevelLabel = myfont.render(str("Level"), 1, (255,0,0))

#_______________________________________________________________________________


#4 possible random location for monster spawn
monsterLo = randint(1,4)
if monsterLo==1:
    monsterX=10
    monsterY=0
if monsterLo==2:
    monsterX=20
    monsterY=10
if monsterLo==3:
    monsterX=0
    monsterY=10
if monsterLo==4:
    monsterX=10
    monsterY=20
#_______________________________________________________________________________


while True:
    #checking events
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        time.sleep(0.05)
        #checks if key down
        if event.type == KEYDOWN:
            #character movement (left,right,up,down in respective order)
            if event.key == K_a:
                movex = -2
            elif event.key == K_d:
                movex = 2
            elif event.key == K_w:
                movey = -2
            elif event.key == K_s:
                movey = 2
            #arrow movement (2 possible keys for each direction [left,right,up,down])
            elif event.key == K_t:
                time.sleep(0.05)
                if tKey==Subtract3:
                    arrowx = -2
                    subtractCounter-=1
                arrowShootBoolean=1
            elif event.key == K_y:
                time.sleep(0.05)
                if yKey==Subtract3:
                    arrowx = -2
                    subtractCounter-=1
                arrowShootBoolean=1
            elif event.key == K_o:
                time.sleep(0.05)
                if oKey==Add3:
                    arrowx = 2
                    addCounter-=1
                arrowShootBoolean=1
            elif event.key == K_p:
                time.sleep(0.05)
                if pKey==Add3:
                    arrowx = 2
                    addCounter-=1
                arrowShootBoolean=1
            elif event.key == K_u:
                time.sleep(0.05)
                if uKey==Multiplication3:
                    arrowy =-2
                    multiplicationCounter-=1
                arrowShootBoolean=1
            elif event.key == K_i:
                time.sleep(0.05)
                if iKey==Multiplication3:
                    arrowy =-2
                    multiplicationCounter-=1
                arrowShootBoolean=1
            elif event.key == K_j:                               
                time.sleep(0.05)
                if jKey==Division3:
                    arrowy = 2
                    divisionCounter-=1
                arrowShootBoolean=1
            elif event.key == K_k:                               
                time.sleep(0.05)
                if kKey==Division3:
                    arrowy = 2
                    divisionCounter-=1
                arrowShootBoolean=1
                    
            #delays - prevent smashing of keys to gain insane movement and attack speed
            delayBoolean = 1
            time.sleep(0.05);
        #checks if key is not held down
        if event.type == KEYUP:
            if event.key == K_a:
                movex = 0
            elif event.key == K_d:
                movex = 0
            elif event.key == K_w:
                movey = 0
            elif event.key == K_s:
                movey = 0
            elif event.key == K_t:
                arrowx=0
            elif event.key == K_y:
                arrowx=0
            elif event.key == K_o:
                arrowx=0
            elif event.key == K_p:
                arrowx=0
            elif event.key == K_u:
                arrowy=0
            elif event.key == K_i:
                arrowy=0
            elif event.key == K_j:
                arrowy=0
            elif event.key == K_k:
                arrowy=0
                

        
        
#_______________________________________________________________________________


    if count == 3:
        #random direction for monster
        randDirection = randint(1,2)
        randDirection2 = randint(1,4)
        count = 0
    
    #if monster is within 160 pixels horizontally and vertically
    #it will chase after character
    if monsterX < x+8 and monsterX > x-8 and monsterY<y+8 and monsterY>y-8: 
        if randDirection == 1:
            #AI pathing for X
            if monsterX < x-1:
                monsterX +=0.2
                time.sleep(0.05)
            elif monsterX > x+1:
                monsterX -=0.2
                time.sleep(0.05)
            #AI pathing for Y
            elif monsterY < y-1:
                monsterY +=0.2
                time.sleep(0.05)
            elif monsterY > y+1:
                monsterY -=0.2
                time.sleep(0.05)
        elif randDirection == 2:
            #AI pathing for X
            if monsterY < y-1:
                monsterY +=0.2
                time.sleep(0.05)
            elif monsterY > y+1:
                monsterY -=0.2
                time.sleep(0.05)
            #AI pathing for Y
            elif monsterX < x-1:
                monsterX +=0.2
                time.sleep(0.05)
            elif monsterX > x+1:
                monsterX -=0.2
                time.sleep(0.05)
            
    #else, monster will move in random direction until it is in range of character
    elif randDirection2==1:
        #monster will move right
        if monsterX < 20:
            monsterX +=0.2
            time.sleep(0.05)
        elif monsterX > 20:
            randDirection2 = 2
    elif randDirection2==2:
        #monster will move left
        if monsterX > 1:
            monsterX -=0.2
            time.sleep(0.05)
        elif monsterX < 1:
            randDirection2 = 3
    elif randDirection2==3:
        if monsterY < 19:
            #monster will move down
            monsterY +=0.2
            time.sleep(0.05)
        if monsterY > 19:
            randDirection = 4
    elif randDirection2==4:
        if monsterY > 1:
            #monster will move up
            monsterY -=0.2
            time.sleep(0.05)
        if monsterY < 1:
            randDirection = 1
    
#_______________________________________________________________________________


    #check to see if monster is in hitbox
    if monsterX < x+2 and monsterX > x-2 and monsterY < y+2 and monsterY > y-2:
        health -= 25+levelCounter
        monsterHealth += 10
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(health), 1, (255,0,0))
        time.sleep(0.10)
#_______________________________________________________________________________


    #check for amount of health the hero has
    if health <=0:
        print "game over, you died. Your total score is:"
        print score
        #Screen shuts down once character HP hits 0
        pygame.quit()
        sys.exit()

#_______________________________________________________________________________

        
    #extra delay
    time.sleep(0.05)   

    #checks need for delay
    if delayBoolean == 1:
        #applying change to x and y coordinates if x and y bigger then 0
        x+=movex
        y+=movey
        
        #else arrow position is shot 100pixels in specified direction
        for i in range (1,5):
            arrowX+=arrowx
            arrowY+=arrowy
            #Monster health decreases, score goes up if arrow hits
            if arrowX>monsterX-2 and arrowX<monsterX+2 and arrowY>monsterY and arrowY<monsterY+4:
                monsterHealth -= 10
                screen.blit(impact, (arrowX*20,arrowY*20))
                myfont = pygame.font.SysFont("monospace", 15)
                score+=0.5
                labelScore = myfont.render(str(score), 1, (255,0,0))
                label2 = myfont.render(str(monsterHealth),1,(255,0,0))
                time.sleep(0.10)
                #monster respawns if dies
                if monsterHealth<=0:
                    monsterLo = randint(1,4)
                    if monsterLo==1:
                        monsterX=10
                        monsterY=0
                    if monsterLo==2:
                        monsterX=20
                        monsterY=10
                    if monsterLo==3:
                        monsterX=0
                        monsterY=10
                    if monsterLo==4:
                        monsterX=10
                        monsterY=20
                    #Adds to levelCounter which increases monster strength
                    levelCounter= levelCounter+1
                    labelLevel = myfont.render(str(levelCounter), 1, (255,0,0))
                    monsterHealth = 150+(levelCounter*25)
                    label2 = myfont.render(str(monsterHealth),1,(255,0,0))
            screen.blit(charArrow, (arrowX*20, arrowY*20))
        #position of arrow remains same as character if not being shot
        arrowShootBoolean=0
        if arrowShootBoolean==0:
            arrowX+=movex
            arrowY+=movey
        
            
        #arrow position resets
        arrowX=x+1
        arrowY=y+1
        delayBoolean = 0
        #else character can only move right if x smaller then 0
        if x<0:
            x = 0
            
        #else character can only move left if x is bigger then 800
        if x>20:
            x = 20
            
        #else character can only move down if y smaller then 0
        if y<0:
            y = 0
            
        #else character can only move down if y bigger then 800
        if y>20:
            y = 20
        if arrowCounter==1:
            arrowX=x+1
            arrowY=y+2

    count +=1
    #makes monster faster as level scales higher
    monsterX+(0.01*levelCounter)
    monsterY+(0.01*levelCounter)
#______________calls addition method to create randomly generated addition questions_________________________________________________________________

    if addCounter==0:
        Add1,Add2,Add3=add()
        oKey, pKey =0,0
        #sets correct answer to one of the 2 choices
        randAdd = randint(1,2)
        if randAdd==1:
            oKey=Add3
            pKey=add3+(randint(-5,5))

        else:
            pKey=Add3
            oKey=Add3+(randint(-5,5))
        #prints out the numbers for adding, as well as the 2 choices
        labelAdd1 = myfont.render(str(Add1), 1, (255,0,0))
        labelAddSign = myfont.render(str("+"),1,(255,0,0))
        labelAdd2 = myfont.render(str(Add2), 1, (255,0,0))
        labelADD = myfont.render(str("Shoot Right"), 1, (255,0,0))
        labelAddEqual= myfont.render(str("="), 1, (255,0,0))
        labelO= myfont.render(str("Key O"), 1, (255,0,0))
        labelP= myfont.render(str("Key P"), 1, (255,0,0))
        labelAddO= myfont.render(str(oKey), 1, (255,0,0))
        labelAddP= myfont.render(str(pKey), 1, (255,0,0))
        addCounter=1
        
#______________calls subtraction method to create randomly generated addition questions______________________
    if subtractCounter==0:
        Subtract1,Subtract2,Subtract3=subtract()
        tKey, yKey =0,0
        #sets correct answer to one of the 2 choices
        randSubtract = randint(1,2)
        if randSubtract==1:
            tKey=Subtract3
            yKey=Subtract3+(randint(-5,5))

        else:
            yKey=Subtract3
            tKey=Subtract3+(randint(-5,5))
        #prints out the numbers for subtracting, as well as the 2 choices
        labelSubtract1 = myfont.render(str(Subtract1), 1, (255,255,0))
        labelSubtractSign = myfont.render(str("-"),1,(255,255,0))
        labelSubtract2 = myfont.render(str(Subtract2), 1, (255,255,0))
        labelSUBTRACT = myfont.render(str("Shoot Left"), 1, (255,255,0))
        labelSubtractEqual= myfont.render(str("="), 1, (255,255,0))
        labelT= myfont.render(str("Key T"), 1, (255,255,0))
        labelY= myfont.render(str("Key Y"), 1, (255,255,0))
        labelAddT= myfont.render(str(tKey), 1, (255,255,0))
        labelAddY= myfont.render(str(yKey), 1, (255,255,0))
        subtractCounter=1

    #______________calls subtraction method to create randomly generated addition questions______________________
    if multiplicationCounter==0:
        Multiplication1,Multiplication2,Multiplication3=multiplication()
        uKey, iKey =0,0
        #sets correct answer to one of the 2 choices
        randMultiplication = randint(1,2)
        if randMultiplication==1:
            uKey=Multiplication3
            iKey=Multiplication3+(randint(-5,5))

        else:
            iKey=Multiplication3
            uKey=Multiplication3+(randint(-5,5))
        #prints out the numbers for subtracting, as well as the 2 choices
        labelMultiplication1 = myfont.render(str(Multiplication1), 1, (0,255,0))
        labelMultiplicationSign = myfont.render(str("*"),1,(0,255,0))
        labelMultiplication2 = myfont.render(str(Multiplication2), 1, (0,255,0))
        labelMULTIPLICATION = myfont.render(str("Shoot Up"), 1, (0,255,0))
        labelMultiplicationEqual= myfont.render(str("="), 1, (0,255,0))
        labelU= myfont.render(str("Key U"), 1, (0,255,0))
        labelI= myfont.render(str("Key I"), 1, (0,255,0))
        labelMultiplicationT= myfont.render(str(uKey), 1, (0,255,0))
        labelMultiplicationY= myfont.render(str(iKey), 1, (0,255,0))
        multiplicationCounter=1

    #______________calls division method to create randomly generated addition questions______________________
    if divisionCounter==0:
        Division1,Division2,Division3=division()
        jKey, kKey =0,0
        #sets correct answer to one of the 2 choices
        randDivision = randint(1,2)
        if randDivision==1:
            jKey=Division3
            kKey=Division3+(randint(-5,5))

        else:
            kKey=Division3
            jKey=Division3+(randint(-5,5))
        #prints out the numbers for dividing, as well as the 2 choices
        labelDivision1 = myfont.render(str(Division1), 1, (0,0,255))
        labelDivisionSign = myfont.render(str("/"),1,(0,0,255))
        labelDivision2 = myfont.render(str(Division2), 1, (0,0,255))
        labelDIVISION = myfont.render(str("Shoot Down"), 1, (0,0,255))
        labelDivisionEqual= myfont.render(str("="), 1, (0,0,255))
        labelJ= myfont.render(str("Key J"), 1, (0,0,255))
        labelK= myfont.render(str("Key K"), 1, (0,0,255))
        labelDivisionJ= myfont.render(str(jKey), 1, (0,0,255))
        labelDivisionK= myfont.render(str(kKey), 1, (0,0,255))
        divisionCounter=1
        

    
#___printing objects to screen
    screen.blit(charArrow, (arrowX*20, arrowY*20))
    screen.blit(hero,(x*20,y*20))
    screen.blit(monster,(monsterX*20,monsterY*20))
    screen.blit(label, (20, 480))
    screen.blit(label2, (300, 480))
#___printing score and level____________________________________________________________
    screen.blit(LevelLabel, (0, 505))
    screen.blit(labelLevel, (0, 525))
    screen.blit(ScoreLabel, (0, 545))
    screen.blit(labelScore, (0, 565))
#___printing addition questions____________________________________________________________
    screen.blit(labelAdd1, (410,530))
    screen.blit(labelAddSign, (430,530))
    screen.blit(labelAdd2, (440,530))
    screen.blit(labelAddEqual, (460,530))
    screen.blit(labelADD, (385,500))
    screen.blit(labelO, (390,550))
    screen.blit(labelP, (390,570))
    screen.blit(labelAddEqual, (450,550))
    screen.blit(labelAddEqual, (450,570))
    screen.blit(labelAddO, (470,550))
    screen.blit(labelAddP, (470,570))
#___Printing subtraction questions____________________________________________________________
    screen.blit(labelSubtract1, (300,530))
    screen.blit(labelSubtractSign, (320,530))
    screen.blit(labelSubtract2, (330,530))
    screen.blit(labelSubtractEqual, (350,530))
    screen.blit(labelSUBTRACT, (275,500))
    screen.blit(labelT, (280,550))
    screen.blit(labelY, (280,570))
    screen.blit(labelSubtractEqual, (340,550))
    screen.blit(labelSubtractEqual, (340,570))
    screen.blit(labelAddT, (360,550))
    screen.blit(labelAddY, (360,570))
#___Printing Multiplication questions____________________________________________________________
    screen.blit(labelMultiplication1, (190,530))
    screen.blit(labelMultiplicationSign, (210,530))
    screen.blit(labelMultiplication2, (220,530))
    screen.blit(labelMultiplicationEqual, (240,530))
    screen.blit(labelMULTIPLICATION, (165,500))
    screen.blit(labelU, (170,550))
    screen.blit(labelI, (170,570))
    screen.blit(labelMultiplicationEqual, (230,550))
    screen.blit(labelMultiplicationEqual, (230,570))
    screen.blit(labelMultiplicationT, (250,550))
    screen.blit(labelMultiplicationY, (250,570))
#___Printing Division questions____________________________________________________________
    screen.blit(labelDivision1, (80,530))
    screen.blit(labelDivisionSign, (100,530))
    screen.blit(labelDivision2, (110,530))
    screen.blit(labelDivisionEqual, (130,530))
    screen.blit(labelDIVISION, (55,500))
    screen.blit(labelJ, (60,550))
    screen.blit(labelK, (60,570))
    screen.blit(labelDivisionEqual, (120,550))
    screen.blit(labelDivisionEqual, (120,570))
    screen.blit(labelDivisionJ, (140,550))
    screen.blit(labelDivisionK, (140,570))
    

    
    time.sleep(0.05);
    #refreshing
    pygame.display.update()
