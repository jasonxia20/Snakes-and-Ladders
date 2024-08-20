import pygame
import sys
import random
import pygame_gui #NEED TO INSTALL PYGAME_GUI, TO DO THIS DO (pip install pygame_gui) in the terminal
import os

# --------------- Screen ---------------
width = 1100
height = 750
scrn = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snakes and Ladders")
bgc = (0, 0, 0)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# --------------- IMAGE PATHS --------------- 

#Font Paths
titlefontpath = os.path.join ("Fonts", "PressStart2P-Regular.ttf")
titlefont = pygame.font.Font(titlefontpath, 17)

#Button Paths
startb_path = os.path.join("Assets", "startbutton.png")
quitb_path = os.path.join("Assets", "quitbutton.png")
con_path = os.path.join("Assets", "continue.png")
p2b_path = os.path.join("Assets", "2pbutton.png")
p3b_path = os.path.join("Assets", "3pbutton.png")
p4b_path = os.path.join("Assets", "4pbutton.png")

# Normal Screen Paths
leftscrn_path = os.path.join("Assets", "1leftscrn.png")
rightscrn_path = os.path.join("Assets", "1rightscrn.png")

title_path = os.path.join("Assets", "titlescrn.png")
welcome_path = os.path.join("Assets", "welcome_v3.png")
playerselec_path = os.path.join("Assets", "playerscrn.png")

#Player Name Input Screen Paths
p2scrn_path = os.path.join("Assets", "2pscrn.png")
p3scrn_path = os.path.join("Assets", "3pscrn.png")
p4scrn_path = os.path.join("Assets", "4pscrn.png")

#Grid Path
grid_path = os.path.join("Assets", "num_grid.png")

#Player Sprite Paths
p1s_path = os.path.join("Assets", "p1sprite.png")
p2s_path = os.path.join("Assets", "p2sprite.png")
p3s_path = os.path.join("Assets", "p3sprite.png")
p4s_path = os.path.join("Assets", "p4sprite.png")

# --------------- IMAGE LOAD --------------- 

#Button Loading
startb = pygame.image.load(startb_path).convert_alpha()
continueb = pygame.image.load(con_path).convert_alpha()
quitb = pygame.image.load(quitb_path).convert_alpha()
p2b = pygame.image.load(p2b_path).convert_alpha()
p3b = pygame.image.load(p3b_path).convert_alpha()
p4b = pygame.image.load(p4b_path).convert_alpha()

# Normal Screen Loading
leftscrn = pygame.image.load(leftscrn_path).convert()
rightscrn = pygame.image.load(rightscrn_path).convert()
title = pygame.image.load(title_path).convert()
welcome = pygame.image.load(welcome_path).convert()
playerselec = pygame.image.load(playerselec_path).convert()

#Player Name Input Screen Loading
p2scrn = pygame.image.load(p2scrn_path).convert()
p3scrn = pygame.image.load(p3scrn_path).convert()
p4scrn = pygame.image.load(p4scrn_path).convert()
warn = titlefont.render(" You must hit enter \n after typing each \n       name", False, (255,255,255))
warn_area = warn.get_rect()

#Grid Loading
grid = pygame.image.load(grid_path).convert()

#Player Sprite Loading
p1sprite = pygame.image.load(p1s_path).convert_alpha()
p2sprite = pygame.image.load(p2s_path).convert_alpha()
p3sprite = pygame.image.load(p3s_path).convert_alpha()
p4sprite = pygame.image.load(p4s_path).convert_alpha()

#Portal Paths
aqua_path = os.path.join("Teleporters", "aqua.png")
blue_path = os.path.join("Teleporters", "blue.png")
brown_path = os.path.join("Teleporters", "brown.png")
cyan_path = os.path.join("Teleporters", "cyan.png")
green_path = os.path.join("Teleporters", "green.png")
grey_path = os.path.join("Teleporters", "grey.png")
indigo_path = os.path.join("Teleporters", "indigo.png")
lime_path = os.path.join("Teleporters", "lime.png")
magenta_path = os.path.join("Teleporters", "magenta.png")
orange_path = os.path.join("Teleporters", "orange.png")
pink_path = os.path.join("Teleporters", "pink.png")
purple_path = os.path.join("Teleporters", "purple.png")
red_path = os.path.join("Teleporters", "red.png")
white_path = os.path.join("Teleporters", "white.png")
yellow_path = os.path.join("Teleporters", "yellow.png")

#Portal Loading
aqua = pygame.image.load(aqua_path).convert_alpha()
blue = pygame.image.load(blue_path).convert_alpha()
brown = pygame.image.load(brown_path).convert_alpha()
cyan = pygame.image.load(cyan_path).convert_alpha()
green = pygame.image.load(green_path).convert_alpha()
grey = pygame.image.load(grey_path).convert_alpha()
indigo = pygame.image.load(indigo_path).convert_alpha()
lime = pygame.image.load(lime_path).convert_alpha()
magenta = pygame.image.load(magenta_path).convert_alpha()
orange = pygame.image.load(orange_path).convert_alpha()
pink = pygame.image.load(pink_path).convert_alpha()
purple = pygame.image.load(purple_path).convert_alpha()
red = pygame.image.load(red_path).convert_alpha()
white = pygame.image.load(white_path).convert_alpha()
yellow = pygame.image.load(yellow_path).convert_alpha()
colours = [aqua,blue,brown,cyan,green,grey,indigo,lime,magenta,orange,pink,purple,red,white,yellow]

#Snake Parts Paths
b_horizontal_path = os.path.join("Snake Parts", "b_horizontal.png")
b_vertical_path = os.path.join("Snake Parts", "b_vertical.png")
h_downleft_path = os.path.join("Snake Parts", "h_downleft.png")
h_downright_path = os.path.join("Snake Parts", "h_downright.png")
h_upleft_path = os.path.join("Snake Parts", "h_upleft.png")
h_upright_path = os.path.join("Snake Parts", "h_upright.png")
t_downleft_path = os.path.join("Snake Parts", "t_downleft.png")
t_downright_path = os.path.join("Snake Parts", "t_downright.png")
t_upleft_path = os.path.join("Snake Parts", "t_upleft.png")
t_upright_path = os.path.join("Snake Parts", "t_upright.png")

#Snake Parts Loading
b_horizontal = pygame.image.load(b_horizontal_path).convert_alpha()
b_vertical = pygame.image.load(b_vertical_path).convert_alpha()
h_downleft = pygame.image.load(h_downleft_path).convert_alpha()
h_downright = pygame.image.load(h_downright_path).convert_alpha()
h_upleft = pygame.image.load(h_upleft_path).convert_alpha()
h_upright = pygame.image.load(h_upright_path).convert_alpha()
t_downleft = pygame.image.load(t_downleft_path).convert_alpha()
t_downright = pygame.image.load(t_downright_path).convert_alpha()
t_upleft = pygame.image.load(t_upleft_path).convert_alpha()
t_upright = pygame.image.load(t_upright_path).convert_alpha()


#Text
pressspace = titlefont.render("Press space \n  to begin", False, (255,255,255))
yourturn = titlefont.render("Your Turn,", False, (255,255,255))
youwon = titlefont.render("You Won,", False, (255,255,255))
roll1 = titlefont.render("Rolled a 1", False, (255,255,255))
roll2 = titlefont.render("Rolled a 2", False, (255,255,255))
roll3 = titlefont.render("Rolled a 3", False, (255,255,255))
roll4 = titlefont.render("Rolled a 4", False, (255,255,255))
roll5 = titlefont.render("Rolled a 5", False, (255,255,255))
roll6 = titlefont.render("Rolled a 6", False, (255,255,255))
EncNothing = titlefont.render("Encountered \n  Nothing", False, (255,255,255))
EncSnake = titlefont.render("Encountered \n  A Snake", False, (255,255,255))
EncLadder = titlefont.render("Encountered \n A Teleporter", False, (255,255,255))
EncWin = titlefont.render("Encountered \nFinal Tile", False, (255,255,255))

mng = pygame_gui.UIManager((width,height))
tick = pygame.time.Clock()




#Button Class
class Button():
    def __init__(self,x,y,image,scale):
        b_width = image.get_width()
        b_height = image.get_height()
        #Scales the Button
        self.image = pygame.transform.scale(image, (int(b_width * scale),int(b_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.status = False

    #Draws Image
    def draw(self):
        action = False


        #Gets the position of the mouse
        pos = pygame.mouse.get_pos()
    
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.status == False:
                self.status = True
                action = True
        #draw button on screen
        scrn.blit(self.image, (self.rect.x, self.rect.y))

        return action
        # Allows the image to perform an action if it is clicked


#Generate Ladder Locations
def generate_ladders_position(ls):
    ladders = []
    #Generate 15 Random Beginning and End Positions for Ladders or "Teleporters"
    for i in range (15):
        valid = False
        while valid == False:
            randomcell = random.randint(5,85)
            if randomcell not in ls and randomcell + 15 not in ls:
                ladders.append([randomcell, randomcell+15])
                ls.append(randomcell)
                ls.append(randomcell+15)
                valid = True
    return ladders

#Display Ladders
def generate_ladders(ladpos):
    for item in colours:
        #Goes through a the list "item" of various colors and blits a different colored pair for each teleporter
        if ((ladpos[colours.index(item)][0]-1)//10) % 2 == 0:
            #print("hi",ladpos[colours.index(item)][0])
            if (ladpos[colours.index(item)][0])%10 == 0:
                xp = ((10)-1)*69+30
            else:
                xp = (((ladpos[colours.index(item)][0])%10)-1)*69+30
            yp = (9-((ladpos[colours.index(item)][0]-1)//10))*69+30
            tele = pygame.transform.scale(item,(69,69))

        elif ((ladpos[colours.index(item)][0]-1)//10) % 2 == 1:
            if (ladpos[colours.index(item)][0])%10 == 0:
                xp = ((11-10)-1)*69+30
            else:
                xp = ((11-((ladpos[colours.index(item)][0])%10))-1)*69+30
            yp = (9-((ladpos[colours.index(item)][0]-1)//10))*69+30
            tele = pygame.transform.scale(item,(69,69))

            
        
        if ((ladpos[colours.index(item)][1]-1)//10) % 2 == 0:
            #print("hi",ladpos[colours.index(item)][1])
            if (ladpos[colours.index(item)][1])%10 == 0:
                xp2 = ((10)-1)*69+30
            else:
                xp2 = (((ladpos[colours.index(item)][1])%10)-1)*69+30
            yp2 = (9-((ladpos[colours.index(item)][1]-1)//10))*69+30

            tele2 = pygame.transform.scale(item,(69,69))
        elif ((ladpos[colours.index(item)][1]-1)//10) % 2 == 1:
            if (ladpos[colours.index(item)][1])%10 == 0:
                xp2 = ((11-10)-1)*69+30
            else:
                xp2 = ((11-((ladpos[colours.index(item)][1])%10))-1)*69+30
            yp2 = (9-((ladpos[colours.index(item)][1]-1)//10))*69+30

            tele2 = pygame.transform.scale(item,(69,69))
        scrn.blit(tele2,(xp2,yp2))
        scrn.blit(tele,(xp,yp))

#Generate Snake Locations      
def generate_snakes_position(ls):
    snakes = []
    #Generate 15 Random Beginning and End Positions for Ladders or "Teleporters"
    for i in range (10):
        valid = False
        while valid == False:
            randomcell = random.randint(20,85)
            if randomcell not in ls and randomcell -10 not in ls:
                snakes.append([randomcell, randomcell-10])
                ls.append(randomcell)
                ls.append(randomcell-10)
                valid = True
    return snakes

# Display Snakes
def generate_snakes(snakpos):
    #Blits body segments of Snake
    for i in range(10):
        if ((snakpos[i][0]-1)//10) % 2 == 0:
            #print("hi",snakpos[i][0])
            if (snakpos[i][0])%10 == 0:
                xp = ((10)-1)*69+30
            else:
                xp = (((snakpos[i][0])%10)-1)*69+30
            yp = (9-((snakpos[i][0]-1)//10))*69+30

        elif ((snakpos[i][0]-1)//10) % 2 == 1:
            if (snakpos[i][0])%10 == 0:
                xp = ((11-10)-1)*69+30
            else:
                xp = ((11-((snakpos[i][0])%10))-1)*69+30
            yp = (9-((snakpos[i][0]-1)//10))*69+30
            
        
        if ((snakpos[i][1]-1)//10) % 2 == 0:
            #print("hi",snakpos[i][1])
            if (snakpos[i][1])%10 == 0:
                xp2 = ((10)-1)*69+30
            else:
                xp2 = (((snakpos[i][1])%10)-1)*69+30
            yp2 = (9-((snakpos[i][1]-1)//10))*69+30


        elif ((snakpos[i][1]-1)//10) % 2 == 1:
            if (snakpos[i][1])%10 == 0:
                xp2 = ((11-10)-1)*69+30
            else:
                xp2 = ((11-((snakpos[i][1])%10))-1)*69+30
            yp2 = (9-((snakpos[i][1]-1)//10))*69+30

            
        snakeheadleft = pygame.transform.scale(h_upleft,(46,46))
        snakeheadright = pygame.transform.scale(h_upright,(46,46))
        snaketailleft = pygame.transform.scale(t_downleft,(46,46))
        snaketailright = pygame.transform.scale(t_downright,(46,46))
        snakelenver = pygame.transform.scale(b_vertical,(17,69))
        snakelenhor = pygame.transform.scale(b_horizontal,(69,17))
        
        if xp >= xp2:
            scrn.blit(snakeheadright,(xp,yp+40))
            scrn.blit(snaketailleft, (xp2+40, yp2))
            for i in range((xp2-30)//69+1,(xp-30)//69):
                #print(i)
                scrn.blit(snakelenhor,((i*69)+30,yp+68))
                
            
        elif xp < xp2:
            scrn.blit(snakeheadleft,(xp+40,yp+40))
            scrn.blit(snaketailright,(xp2,yp2))
            #print((xp-30)/69)
            
            for i in range((xp-30)//69+1,(xp2-30)//69):
                scrn.blit(snakelenhor,((i*69)+30,yp+68))
            for i in range((yp-30)//69+1,(yp2-30)//69):
                scrn.blit(snakelenver,(xp,(i*69)+30))

#Dice Roller                
def roll_dice(player):
    dieroll = random.randint(1,6)
    return dieroll, player

#Function To Move Players
def moveplayers(diceinfo,ppos,amt,coordsx,coordsy,ladders, snakes):
    notladders = False
    notsnakes = False
    reached100 = False
    winner = None
    issnake = False
    isladder = False
    
    if 100 not in ppos:
        if diceinfo[1] == 1:
            a = ppos[0]+diceinfo[0]
            if a <= 100:
                ppos.pop(0)
                ppos.insert(0, a)
            else:
                ppos.pop(0)
                ppos.insert(0, 100)
                coordsx[0] = 30
                coordsy[0] = 30
            
        if diceinfo[1] == 2:
            a = ppos[1]+diceinfo[0]
            if a <= 100:
                ppos.pop(1)
                ppos.insert(1, a)
            else:
                ppos.pop(1)
                ppos.insert(1, 100)
                coordsx[1] = 66
                coordsy[1] = 30

        
        if diceinfo[1] == 3:
            a = ppos[2]+diceinfo[0]
            if a <= 100:
                ppos.pop(2)
                ppos.insert(2, a)
            else:
                ppos.pop(2)
                ppos.insert(2, 100)
                coordsx[2] = 30
                coordsy[2] = 66

        
        if diceinfo[1] == 4:
            a = ppos[3]+diceinfo[0]
            if a <= 100:
                ppos.pop(3)
                ppos.insert(3, a)
            else:
                ppos.pop(3)
                ppos.insert(3, 100)
                coordsx[3] = 66
                coordsy[3] = 66
        
    else:
        reached100 = True
    
    # Tile handling for player 1
    if True:
        for item in ladders: #Checking for Ladders
            if ppos[0] == item[0]:
                ppos[0] = item[1]
                isladder = True
                if ((item[1]-1)//10) % 2 == 0:
                    if (item[1])%10 == 0:
                        coordsx[0] = ((10)-1)*69+30
                    else:
                        coordsx[0] = (((item[1])%10)-1)*69+30
                        coordsy[0] = (9-((item[1]-1)//10))*69+30

                elif ((item[1]-1)//10) % 2 == 1:
                    if (item[1])%10 == 0:
                        coordsx[0] = ((11-10)-1)*69+30
                    else:
                        coordsx[0] = ((11-((item[1])%10))-1)*69+30
                        coordsy[0] = (9-((item[1]-1)//10))*69+30
            else:
                notladders = True
            
        for item in snakes: #Checking for Snakes
            if ppos[0] == item[0]:
                ppos[0] = item[1]
                issnake = True
                if ((item[1]-1)//10) % 2 == 0:
                    if (item[1])%10 == 0:
                        coordsx[0] = ((10)-1)*69+30
                    else:
                        coordsx[0] = (((item[1])%10)-1)*69+30
                        coordsy[0] = (9-((item[1]-1)//10))*69+30

                elif ((item[1]-1)//10) % 2 == 1:
                    if (item[1])%10 == 0:
                        coordsx[0] = ((11-10)-1)*69+30
                    else:
                        coordsx[0] = ((11-((item[1])%10))-1)*69+30
                        coordsy[0] = (9-((item[1]-1)//10))*69+30
            else: # No snakes and no Ladders
                notsnakes = True
        if notladders == True and notsnakes == True:
            if ((ppos[0]-1)//10) % 2 == 0:
                if (ppos[0])%10 == 0:
                    coordsx[0] = ((10)-1)*69+30
                else:
                    coordsx[0] = (((ppos[0])%10)-1)*69+30
                    coordsy[0] = (9-((ppos[0]-1)//10))*69+30

            elif ((ppos[0]-1)//10) % 2 == 1:
                if (ppos[0])%10 == 0:
                    coordsx[0] = ((11-10)-1)*69+30
                else:
                    coordsx[0] = ((11-((ppos[0])%10))-1)*69+30
                    coordsy[0] = (9-((ppos[0]-1)//10))*69+30
            
            
        
        # Tile handling for player 2
        for item in ladders:
            if ppos[1] == item[0]:
                ppos[1] = item[1]
                if ((item[1]-1)//10) % 2 == 0:
                    if (item[1])%10 == 0:
                        coordsx[1] = ((10)-1)*69+30
                    else:
                        coordsx[1] = (((item[1])%10)-1)*69+30
                        coordsy[1] = (9-((item[1]-1)//10))*69+30

                elif ((item[1]-1)//10) % 2 == 1:
                    if (item[1])%10 == 0:
                        coordsx[1] = ((11-10)-1)*69+30
                    else:
                        coordsx[1] = ((11-((item[1])%10))-1)*69+30
                        coordsy[1] = (9-((item[1]-1)//10))*69+30
            else:
                for i in range(len(ppos)):
                    if ppos[i] == 100:
                        winner = i
                notladders = True

        for item in snakes:
            if ppos[1] == item[0]:
                ppos[1] = item[1]
                issnake = True
                if ((item[1]-1)//10) % 2 == 0:
                    if (item[1])%10 == 0:
                        coordsx[1] = ((10)-1)*69+30
                    else:
                        coordsx[1] = (((item[1])%10)-1)*69+30
                        coordsy[1] = (9-((item[1]-1)//10))*69+30

                elif ((item[1]-1)//10) % 2 == 1:
                    if (item[1])%10 == 0:
                        coordsx[1] = ((11-10)-1)*69+30
                    else:
                        coordsx[1] = ((11-((item[1])%10))-1)*69+30
                        coordsy[1] = (9-((item[1]-1)//10))*69+30
            else:
                notsnakes = True
        if notladders == True and notsnakes == True:
            if ((ppos[1]-1)//10) % 2 == 0:
                if (ppos[1])%10 == 0:
                    coordsx[1] = ((10)-1)*69+66
                else:
                    coordsx[1] = (((ppos[1])%10)-1)*69+66
                    coordsy[1] = (9-((ppos[1]-1)//10))*69+30

            elif ((ppos[1]-1)//10) % 2 == 1:
                if (ppos[1])%10 == 0:
                    coordsx[1] = ((11-10)-1)*69+66
                else:
                    coordsx[1] = ((11-((ppos[1])%10))-1)*69+66
                    coordsy[1] = (9-((ppos[1]-1)//10))*69+30
                
                
                
        # Tile handling for player 3
        if amt == 3 or amt == 4:
            for item in ladders:
                if ppos[2] == item[0]:
                    ppos[2] = item[1]
                    isladder = True
                    if ((item[1]-1)//10) % 2 == 0:
                        if (item[1])%10 == 0:
                            coordsx[2] = ((10)-1)*69+30
                        else:
                            coordsx[2] = (((item[1])%10)-1)*69+30
                            coordsy[2] = (9-((item[1]-1)//10))*69+30

                    elif ((item[1]-1)//10) % 2 == 1:
                        if (item[1])%10 == 0:
                            coordsx[2] = ((11-10)-1)*69+30
                        else:
                            coordsx[2] = ((11-((item[1])%10))-1)*69+30
                            coordsy[2] = (9-((item[1]-1)//10))*69+30
                else:
                    notladders = True
                
            for item in snakes:
                if ppos[2] == item[0]:
                    ppos[2] = item[1]
                    issnake = True
                    if ((item[1]-1)//10) % 2 == 0:
                        if (item[1])%10 == 0:
                            coordsx[2] = ((10)-1)*69+30
                        else:
                            coordsx[2] = (((item[1])%10)-1)*69+30
                            coordsy[2] = (9-((item[1]-1)//10))*69+30

                    elif ((item[1]-1)//10) % 2 == 1:
                        if (item[1])%10 == 0:
                            coordsx[2] = ((11-10)-1)*69+30
                        else:
                            coordsx[2] = ((11-((item[1])%10))-1)*69+30
                            coordsy[2] = (9-((item[1]-1)//10))*69+30
                else:
                    notsnakes = True
            if notladders == True and notsnakes == True:
                if ((ppos[2]-1)//10) % 2 == 0:
                    if (ppos[2])%10 == 0:
                        coordsx[2] = ((10)-1)*69+30
                    else:
                        coordsx[2] = (((ppos[2])%10)-1)*69+30
                        coordsy[2] = (9-((ppos[2]-1)//10))*69+66

                elif ((ppos[2]-1)//10) % 2 == 1:
                    if (ppos[2])%10 == 0:
                        coordsx[2] = ((11-10)-1)*69+30
                    else:
                        coordsx[2] = ((11-((ppos[2])%10))-1)*69+30
                        coordsy[2] = (9-((ppos[2]-1)//10))*69+66

        if amt == 4:
            for item in ladders:
                if ppos[3] == item[0]:
                    ppos[3] = item[1]
                    isladder = True
                    if ((item[1]-1)//10) % 2 == 0:
                        if (item[1])%10 == 0:
                            coordsx[3] = ((10)-1)*69+30
                        else:
                            coordsx[3] = (((item[1])%10)-1)*69+30
                            coordsy[3] = (9-((item[1]-1)//10))*69+30

                    elif ((item[1]-1)//10) % 2 == 1:
                        if (item[1])%10 == 0:
                            coordsx[3] = ((11-10)-1)*69+30
                        else:
                            coordsx[3] = ((11-((item[1])%10))-1)*69+30
                            coordsy[3] = (9-((item[1]-1)//10))*69+30
                else:
                    notladders = True
                
            for item in snakes:
                if ppos[3] == item[0]:
                    issnake = True
                    ppos[3] = item[1]
                    if ((item[1]-1)//10) % 2 == 0:
                        if (item[1])%10 == 0:
                            coordsx[3] = ((10)-1)*69+30
                        else:
                            coordsx[3] = (((item[1])%10)-1)*69+30
                            coordsy[3] = (9-((item[1]-1)//10))*69+30

                    elif ((item[1]-1)//10) % 2 == 1:
                        if (item[1])%10 == 0:
                            coordsx[3] = ((11-10)-1)*69+30
                        else:
                            coordsx[3] = ((11-((item[1])%10))-1)*69+30
                            coordsy[3] = (9-((item[1]-1)//10))*69+30
                else:
                    notsnakes = True
            if notladders == True and notsnakes == True:
                if ((ppos[3]-1)//10) % 2 == 0:
                    if (ppos[3])%10 == 0:
                        coordsx[3] = ((10)-1)*69+66
                    else:
                        coordsx[3] = (((ppos[3])%10)-1)*69+66
                        coordsy[3] = (9-((ppos[3]-1)//10))*69+66

                elif ((ppos[3]-1)//10) % 2 == 1:
                    if (ppos[3])%10 == 0:
                        coordsx[3] = ((11-10)-1)*69+66
                    else:
                        coordsx[3] = ((11-((ppos[3])%10))-1)*69+66
                        coordsy[3] = (9-((ppos[3]-1)//10))*69+66
                        
    return coordsx, coordsy, reached100, issnake, isladder, winner

#Player Icon Display              
def display_players(coords, amt):
    play1 = pygame.transform.scale(p1sprite,(34,34))
    play2 = pygame.transform.scale(p2sprite,(34,34))
    play3 = pygame.transform.scale(p3sprite,(34,34))
    play4 = pygame.transform.scale(p4sprite,(34,34))
    if amt == 2:
        scrn.blit(play1,(coords[0][0], coords[1][0]))
        scrn.blit(play2,(coords[0][1], coords[1][1]))
    if amt == 3:
        scrn.blit(play1,(coords[0][0], coords[1][0]))
        scrn.blit(play2,(coords[0][1], coords[1][1]))
        scrn.blit(play3,(coords[0][2], coords[1][2]))
    if amt == 4:
        scrn.blit(play1,(coords[0][0], coords[1][0]))
        scrn.blit(play2,(coords[0][1], coords[1][1]))
        scrn.blit(play3,(coords[0][2], coords[1][2]))
        scrn.blit(play4,(coords[0][3], coords[1][3]))

#Display for Game Board
def board_bg(): #actual game board
    lscrn = pygame.transform.scale(leftscrn,(550,750))
    scrn.blit(lscrn,(0,0))
    rscrn = pygame.transform.scale(rightscrn,(550,750))
    scrn.blit(rscrn,(width/2,0))
    grid1 = pygame.transform.scale(grid,(690,690))
    scrn.blit(grid1,(30,30))

#Display for 4 Player Select
def players4():
    screen4player = pygame.transform.scale(p4scrn,(550,750))
    scrn.blit(screen4player,(width/4,0))

#Display for 3 Player Select
def players3():
    screen3player = pygame.transform.scale(p3scrn,(550,750))
    scrn.blit(screen3player,(width/4,0))

#Display for 2 Player Select
def players2():
    screen2player = pygame.transform.scale(p2scrn,(550,750))
    scrn.blit(screen2player,(width/4,0))

#Choose Amount of Players Display Menu
def chooseplayers():
    selec_1 = pygame.transform.scale(playerselec,(550,750))
    scrn.blit(selec_1,(width/4,0))
    scrn.blit(warn, ((width-warn_area.w)/2, 600))

#Welcome Menu Display Function
def welcomemenu():
    welcome_1 = pygame.transform.scale(welcome,(550,750))
    scrn.blit(welcome_1,(width/4,0))

#Start Screen Display Function
def startscreen():
    title_1 = pygame.transform.scale(title,(550,750))
    scrn.blit(title_1,(width/4,0))

#Input Names for 2 Players
def inp_name2():
    p1name2 = ""
    p2name2 = ""
    p1_entered2 = False
    p2_entered2 = False

    text2_entry_p1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2-60 , height / 2-80), (200, 50)), manager=mng, object_id="#p1_text2_entry")
    text2_entry_p2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2-60, height / 2 + 50), (200, 50)), manager=mng, object_id="#p2_text2_entry")

    while True:
        fps = tick.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == "#p1_text2_entry":
                    p1name2 = event.text
                    playername1 = titlefont.render(p1name2,True,(224, 77, 54))
                    p1_entered2 = True
                elif event.ui_object_id == "#p2_text2_entry":
                    p2name2 = event.text
                    playername2 = titlefont.render(p2name2,True,(99, 146, 235))
                    p2_entered2 = True

            mng.process_events(event)

        mng.update(fps)

        mng.draw_ui(scrn)
        pygame.display.update()
        

        if p1_entered2 and p2_entered2:
            return p1name2, p2name2

#Input Names for 3 Players
def inp_name3():
    p1name3 = ""
    p2name3 = ""
    p3name3 = ""
    p1_entered3 = False
    p2_entered3 = False
    p3_entered3 = False

    text3_entry_p1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 -125), (200, 50)), manager=mng, object_id="#p1_text3_entry")
    text3_entry_p2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 ), (200, 50)), manager=mng, object_id="#p2_text3_entry")
    text3_entry_p3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 + 145), (200, 50)), manager=mng, object_id="#p3_text3_entry")

    while True:
        fps = tick.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == "#p1_text3_entry":
                    p1name3 = event.text
                    playername1 = titlefont.render(p1name3,True,(224, 77, 54))
                    p1_entered3 = True
                elif event.ui_object_id == "#p2_text3_entry":
                    p2name3 = event.text
                    playername2 = titlefont.render(p2name3,True,(99, 146, 235))
                    p2_entered3 = True
                elif event.ui_object_id == "#p3_text3_entry":
                    p3name3 = event.text
                    playername3 = titlefont.render(p3name3,True,(70, 199, 132))
                    p3_entered3 = True

            mng.process_events(event)

        mng.update(fps)

        mng.draw_ui(scrn)
        pygame.display.update()

        if p1_entered3 and p2_entered3 and p3_entered3:
            return p1name3, p2name3, p3name3

#Input Names for 4 Players
def inp_name4():
    p1name4 = ""
    p2name4 = ""
    p3name4 = ""
    p4name4 = ""
    p1_entered4 = False
    p2_entered4 = False
    p3_entered4 = False
    p4_entered4 = False

    text4_entry_p1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 - 195), (200, 50)), manager=mng, object_id="#p1_text4_entry")
    text4_entry_p2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 - 65), (200, 50)), manager=mng, object_id="#p2_text4_entry")
    text4_entry_p3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 + 75), (200, 50)), manager=mng, object_id="#p3_text4_entry")
    text4_entry_p4 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 60, height / 2 + 210), (200, 50)), manager=mng, object_id="#p4_text4_entry")


    while True:
        fps = tick.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == "#p1_text4_entry":
                    p1name4 = event.text
                    playername1 = titlefont.render(p1name4,True,(224, 77, 54))
                    p1_entered4 = True
                elif event.ui_object_id == "#p2_text4_entry":
                    p2name4 = event.text
                    playername2 = titlefont.render(p2name4,True,(99, 146, 235))
                    p2_entered4 = True
                elif event.ui_object_id == "#p3_text4_entry":
                    p3name4 = event.text
                    playername3 = titlefont.render(p3name4,True,(70, 199, 132))
                    p3_entered4 = True
                elif event.ui_object_id == "#p4_text4_entry":
                    p4name4 = event.text
                    playername4 = titlefont.render(p4name4,True,(237, 195, 55))
                    p4_entered4 = True                                        

            mng.process_events(event)

        mng.update(fps)

        mng.draw_ui(scrn)
        pygame.display.update()

        if p1_entered4 and p2_entered4 and p3_entered4 and p4_entered4:
            return p1name4, p2name4, p3name4, p4name4
        
    
#Button Outputs 
start_button = Button((width/2)-60,(height/1.5),startb,0.2)
quit_button = Button((width/2)-60,((height/1.5)+80),quitb,0.2)
continue_button = Button((width/3)+70,((height/1.5)+94),continueb,0.26)
players2button = Button((width/3)+70,((height/3)-50),p2b,0.26)
players3button = Button((width/3)+70,((height/3)+50),p3b,0.26)
players4button = Button((width/3)+70,((height/3)+150),p4b,0.26)

entlist = []
# Gane Loop Function
def game_loop():
    run = True
    timer = 0
    o = [0,0,0,0] # Checks if someone has gone before the current player, 0th element is player 1, etc.
    whoseturn = 0
    xcrds = [30,66,30,66]
    ycrds = [9*69+30,9*69+30,9*69+66,9*69+66]
    coords = [xcrds,ycrds, False, False, False, None]
    dice = [0,0]
    dice2 = dice
    pinfo = [1,1,1,1]
    done100 = False
    generated = False
    current_scrn = "title screen" #Initializes starting screen, game always starts here

    while run:
        timer = 0
        scrn.fill(bgc)
        # Runs title screen
        if current_scrn == "title screen":
            startscreen()
            #If preses start it continues to welcome menu
            if start_button.draw():
                current_scrn = "welcome screen"
                print("welcome screen")
            #If presses quit, the game ends
            if quit_button.draw():
                run = False
        # Displays Welcome Screen
        if current_scrn == "welcome screen":
            welcomemenu()
            #If the continue button is pressed the game is taken to the player selection
            if continue_button.draw():
                current_scrn = "player select"
                print("player screen")
        # Displays Player selection screen
        if current_scrn == "player select":
            print("PS")
            chooseplayers()
            # If chooses to play with 2 players, then gets taken to 2 player name selection
            if players2button.draw():
                current_scrn = "menu 2 players"
                print("2")
            # If chooses to play with 3 players, then gets taken to 3 player name selection
            elif players3button.draw():
                current_scrn = "menu 3 players"
                print("3")
            # If chooses to play with 4 players, then gets taken to 4 player name selection
            elif players4button.draw():
                current_scrn = "menu 4 players"
                print("4")

        #Displays 2 player name selection
        if current_scrn == "menu 2 players":
            players2()
            p1name, p2name = inp_name2()
            print(f"Player 1: {p1name}, Player 2: {p2name}")
            #amount of players = 2
            amt = 2
            o = [0,0]
            current_scrn = "grid"
            
        #Displays 3 player name selection
        if current_scrn == "menu 3 players":
            players3()
            p1name, p2name, p3name = inp_name3()
            print(f"Player 1: {p1name}, Player 2: {p2name}, Player 3: {p3name}")
            #amount of players = 3
            amt = 3
            o = [0,0,0]
            current_scrn = "grid"
            
        #Displays 4 player name selection   
        if current_scrn == "menu 4 players":
            players4()
            p1name, p2name, p3name, p4name = inp_name4()
            print(f"Player 1: {p1name}, Player 2: {p2name}, Player 3: {p3name}, Player 4: {p4name}")
            #amount of players = 4
            amt = 4
            current_scrn = "grid"

        #Take players to main board after all names have been entered
        if current_scrn == "grid":
            board_bg()
            #Blit the game board, snakes and teleporters (ladders)
            if generated == False:
                ladder = generate_ladders_position(entlist)
                snakes = generate_snakes_position(entlist)
                generated = True
            generate_ladders(ladder)
            generate_snakes(snakes)

            # Display Rolled Value
            if dice2[0] == 1:
                scrn.blit(roll1, (800,350))
            if dice2[0] == 2:
                scrn.blit(roll2, (800,350))
            if dice2[0] == 3:
                scrn.blit(roll3, (800,350))
            if dice2[0] == 4:
                scrn.blit(roll4, (800,350))
            if dice2[0] == 5:
                scrn.blit(roll5, (800,350))
            if dice2[0] == 6:
                scrn.blit(roll6, (800,350))
            
            # Runs to check the current players turn, rolls the dice, and updates the array o with 0, saying that that user has already played
            timer += 1
            if whoseturn % 4 == 0 and amt == 4 and whoseturn != 0 and o[3] == 1:
                dice = roll_dice(4)
                print("p4",whoseturn)
                o[3] = 0
            elif whoseturn % 3 == 0 and amt >=3 and whoseturn != 0 and o[2] == 1:
                dice = roll_dice(3)
                print("p3",whoseturn)
                o[2] = 0
            elif whoseturn % 2 == 0 and whoseturn != 0 and o[1] == 1:
                dice = roll_dice(2)
                print("p2",whoseturn)
                o[1] = 0
            elif whoseturn % 1 == 0 and whoseturn != 0 and o[0] == 1:
                dice = roll_dice(1)
                print("p1",whoseturn)
                o[0] = 0
            
            #Error Checking, to display player coords
            if whoseturn != 0:
                display_players(coords,amt)
            
            #Display the press space to begin, the current person's turn
            if whoseturn == 0:
                scrn.blit(pressspace,(800, 330))
            elif whoseturn != 0 and coords[2] == False:
                scrn.blit(yourturn,(800, 150))
            else:
                scrn.blit(youwon,(800,150))
            
            # if player 1's turn, show that it is player 1's turn "Its your turn! (Player 1)"
            if whoseturn % 4 == 1 and whoseturn != 0 and coords[2] == False or coords[5] == 0:
                playername1 = titlefont.render(p1name,True,(224, 77, 54))
                scrn.blit(playername1,(800,175))
            # if player 2's turn, show that it is player 2's turn "Its your turn! (Player 2)"
            elif whoseturn % 4 == 2 and whoseturn != 0 and coords[2] == False or coords[5] == 1:
                playername2 = titlefont.render(p2name,True,(99, 146, 235))
                scrn.blit(playername2,(800,175))
            # if player 3's turn, show that it is player 3's turn "Its your turn! (Player 3)"
            elif whoseturn % 4 == 3 and whoseturn != 0 and coords[2] == False or coords[5] == 2:
                playername3 = titlefont.render(p3name,True,(70, 199, 132))
                scrn.blit(playername3,(800,175))
            # if player 4's turn, show that it is player 4's turn "Its your turn! (Player 4)"
            elif whoseturn % 4 == 0 and whoseturn != 0 and coords[2] == False or coords[5] == 3:
                playername4 = titlefont.render(p4name,True,(237, 195, 55))
                scrn.blit(playername4,(800,175))
            
            
            # If space is pressed roll dice
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if coords[5] == None:
                            dice2 = dice
                        # Turn is incremented
                        whoseturn += 1
                        if whoseturn > amt:
                            whoseturn = 1
                        coords=moveplayers(dice, pinfo, amt, xcrds, ycrds, ladder, snakes)
                        #Updates if a player has gone or not
                        o[(whoseturn)%amt-1] = 1
                
                if event.type == pygame.QUIT:
                    run = False

            #Displays if the player has encountered a snake, a teleporter, the final tile, or nothing     
            if coords[3] == True:
                scrn.blit(EncSnake, (800, 600))
            if coords[4] == True:
                scrn.blit(EncLadder, (800, 600))
            if coords[5] != None:
                scrn.blit(EncWin, (800,600))
            if coords[3] != True and coords[4] != True and coords[5] == None:
                scrn.blit(EncNothing, (800,600))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)

game_loop()
print("")
pygame.quit()
sys.exit()
