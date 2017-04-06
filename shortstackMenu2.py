import pygame
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
picH = 800
picV = 800
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
backgroundI = pygame.image.load('background_w_bar.jpg')
screen = pygame.display.set_mode((screenW, screenH))


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
    mat = Mat()
    mat.draw(screen)
    glass = pygame.image.load('glass.png')
    blender = pygame.image.load('blender.png')
    pot = pygame.image.load('top_pot.png')
    microwave = pygame.image.load('microwave.png')

    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and (mx > sqX and mx < sqX + startL) and (
                    my > sqY and my < sqY + startH):
                print(mx)
                print(my)
                held = True
                while (held):
                    for event in pygame.event.get():
                        if (event.type == pygame.MOUSEBUTTONUP):
                            held = False
                        mx, my = pygame.mouse.get_pos()
                        sqX = mx
                        sqY = my
                        screen.blit(backgroundI, (0, 0))
                        screen.blit(newgame, (sqX, sqY))
                        pygame.display.update()
                        if (held == False):
                            break
        pygame.display.update()

def mouseMov():
    held = True
    while (held):
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP):
                held = False
            mx, my = pygame.mouse.get_pos()
            sqX = mx
            sqY = my
            screen.blit(backgroundI, (0, 0))
            screen.blit(newgame, (sqX, sqY))
            pygame.display.update()
            if (held == False):
                break



def main():
    startMenu()


class Mat():
    def __init__(self):
        self.img = pygame.image.load('mat.png.')
        self.pos = [350, 375]
        self.baseY = 375 + 62
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
        self.image_size = self.img.size
        self.width = self.image_size[0]
        self.height = self.image_size[1]
        self.upperY = 0
        self.lowerY = 0 + self.height
        self.leftX = 0
        self.midLeftX = 0 + self.width / 3
        self.midRightX = 0 + 2 * self.width / 3
        self.rightX = 0 + self.width

    def loadImg(self, IMG):
        self.img = pygame.image.load(IMG)
        self.image_size = self.img.size
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

    def update(self, counter):
        if (self.selected == 0 and self.placed == 0)
            if ()
        elif (self.selected == 1 and self.placed == 0)

        elif (self.selected == 0 and self.placed == 1)


if __name__ == "__main__":
    main()
