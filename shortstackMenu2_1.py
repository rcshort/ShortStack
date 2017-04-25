import pygame
#import nltk
import random

# 800
# 800
gravity = 0.4
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.init()
screenH = 500
screenW = 888
startL = 274
startH = 56
newgame = pygame.image.load('newgame.png')
newgameC = pygame.image.load('newgame_click.png')
ranking = pygame.image.load('ranking.png')
rankingC = pygame.image.load('ranking_click.png')
level = pygame.image.load('levels.png')
levelC = pygame.image.load('levels_click.png')
menuP = pygame.image.load('mainmenu.png')
queue = pygame.image.load('bar.png')
#object array
xCord = []
yCord = []
screen = pygame.display.set_mode((screenW, screenH))
blender = pygame.image.load('blender.png')
blender = pygame.transform.scale(blender, (80, 100))
pot = pygame.image.load('top_pot.png')
microwave = pygame.image.load('microwave.png')
microwave = pygame.transform.scale(microwave, (110, 72))
glass = pygame.image.load('glass.png')
glass = pygame.transform.scale(glass, (75, 100))
objectS = [microwave, glass, blender]
StoreC = 3
storeX = [5, 20, 20]
storeY = [400, 275, 150]
objectL = [110, 75, 80]
objectH = [72, 100, 100]
count = 0
file = "calming.wav"
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


def startMenu():
    intro = True
    print("HERERERE")
    highlight = 1
    enter = 0  # changes to 1 if enter is pushed on a option
    while intro:
        screen.blit(menuP, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and highlight != 3:
                    highlight += 1
                if event.key == pygame.K_UP and highlight != 1:
                    highlight -= 1
                if event.key == pygame.K_RETURN:
                    enter = 1  # enter is pushed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_KP_ENTER:
                    highlight = 0
        # mouse = pygame.mouse.get_pos()
        screen.blit(newgame, (screenW / 2 - startL / 2, screenH / 2.5))
        screen.blit(ranking, (screenW / 2 - startL / 2, screenH / 2.5 + 100))
        screen.blit(level, (screenW / 2 - startL / 2, screenH / 2.5 + 200))
        if highlight == 1:
            screen.blit(newgameC, (screenW / 2 - startL / 2, screenH / 2.5))
        elif highlight == 2:
            screen.blit(rankingC, (screenW / 2 - startL / 2, screenH / 2.5 + 100))
        elif highlight == 3:
            screen.blit(levelC, (screenW / 2 - startL / 2, screenH / 2.5 + 200))
        pygame.display.update()
        if enter == 1:
            levelOne()


def levelOne():
    backgroundI = pygame.image.load('background_w_bar.jpg')
    backgroundI = pygame.transform.scale(backgroundI, (888, 500))
    screen.blit(backgroundI, (0, 0))
    # screen.blit(queue, (0,0))
    sqX = 5
    sqY = 400
    sqX2 = 20
    sqY2 = 275
    mat = Mat()
    mat.draw(screen)
    microX = 110
    microY = 72
    MICROWAVE = RectObject()
    GLASS = RectObject()
    POT = RectObject()
    BLENDER = RectObject()
    GLASS.loadImg('glass.png')
    BLENDER.loadImg('blender.png')
    POT.loadImg('top_pot.png')
    MICROWAVE.loadImg('microwave.png')
    objectS = [MICROWAVE, GLASS, BLENDER]
    blX = 80
    blY = 100
    gX = 75
    gY = 100
    #screen.blit(microwave, (sqX,sqY))
    #screen.blit(glass, (sqX2, sqY2))
    printObjects()
    global count
    while (1):
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and count == 0 and (mx > storeX[count] and mx < storeX[count] + objectL[count]) and (
                            my > storeY[count] and my < storeY[count] + objectH[count]):
                count = count + 1
                Move = mouseMov(count -1,mat, backgroundI)
                if(Move == False):
                    count = count - 1
                    screen.blit(backgroundI, (0, 0))
                    mat.draw(screen)
                    printObjects()
                    pygame.display.update()
        i = 0
        while(i < 3):
            objectS[i].update(objectS, i)
            i = i+1


def printObjects():
    for x in range(count, StoreC):
        screen.blit(objectS[x], (storeX[x], storeY[x]))
    pygame.display.update()

def mouseMov(current, mat,back):
    held = True
    while (held):
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP):
                held = False
            mx, my = pygame.mouse.get_pos()
            sqX = mx
            sqY = my
            screen.blit(back, (0, 0))
            mat.draw(screen)
            screen.blit(objectS[current], (sqX, sqY))
            printObjects()
            pygame.display.update()
            if (held == False):
                print(my)
                if(sqY < mat.minX and sqX >mat.minX and sqX < mat.maxX):
                    while(my < mat.minX):
                        my = my + 1
                    sqY= my
                    screen.blit(back, (0, 0))
                    #for x in range(count, StoreC):
                     #   storeY[x] = storeY[x] + 125
                    mat.draw(screen)
                    printObjects()
                    screen.blit(objectS[current], (sqX, sqY))
                    pygame.display.update()
                    return True
                else:

                    return False
                break


def main():
    startMenu()


class Mat():
    def __init__(self):
        self.img = pygame.image.load('mat.png.')
        self.pos = [350, 375]
        self.baseY = 375 - 62
        self.minX = 350
        self.maxX = 350 + 326

    def draw(self, screen):
        screen.blit(self.img, self.pos)


class RectObject():
    def __init__(self):
        self.selected = 0
        self.placed = 0
        self.img = pygame.image.load('display.png')
        self.pos = [0, 0]
        self.image_size = self.img.get_rect().size
        self.width = self.image_size[0]
        self.height = self.image_size[1]
        self.upperY = 0
        self.lowerY = 0 + self.height
        self.leftX = 0
        self.midLeftX = 0 + self.width / 3
        self.midRightX = 0 + 2 * self.width / 3
        self.rightX = 0 + self.width

    def collide(self,objArray, i): #array of our objects, index of object just dropped
        while i >= 0:
            if self.upperY >= objArray[i-1].lowerY:
                self.upperY = objArray[i-1].lowerY
                self.placed = 1
                return
            i = i-1

        #check falling object against base object


    def loadImg(self, IMG):
        self.img = pygame.image.load(IMG)
        self.image_size = self.img.get_rect().size
        self.width = self.image_size[0]
        self.height = self.image_size[1]

    def setPos(self, pos):
        self.pos = pos
        self.upperY = pos[1]
        self.lowerY = pos[1] + self.height
        self.leftX = pos[0]
        self.midLeftX = pos[0] + self.width / 3
        self.midRightX = pos[0] + 2 * self.width / 3
        self.rightX = pos[0] + self.width

    def update(self, objArray, i):
        if(self.lowerY <= Mat.self.baseY and self.rightX > 100):
            if(self.midX < Mat.rightX and self.midX > Mat.leftX):
                screen.blit(self.img)
                self.placed = 1
                return
            else: return
        elif(self.lowerY > Mat.self.baseY and self.right > 100 and self.placed == 0):
            setPos([self.pos[0],self.pos[1]-1])
            screen.blit(self.img)
            if(self.lowerY >= 500):
                setPos(5, 400)
                screen.blit(self.img)
                return
            collide(objArray, i)


if __name__ == "__main__":
    main()