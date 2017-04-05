import pygame
import random
#800
#800
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
backgroundI = pygame.image.load('background.jpg')
queue = pygame.image.load('bar.png')
screen = pygame.display.set_mode((screenW, screenH))

def startMenu():
    intro = True
    print("HERERERE")
    highlight = 1
    enter = 0 #changes to 1 if enter is pushed on a option
    while intro:
        screen.blit(menuP,(0, 0))
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
                    enter = 1 # enter is pushed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_KP_ENTER:
                    highlight = 0
        #mouse = pygame.mouse.get_pos()
        screen.blit(newgame, (screenW/2 - startL/2, screenH/2.5))
        screen.blit(ranking, (screenW / 2 - startL/ 2, screenH / 2.5 + 100))
        screen.blit(level, (screenW / 2 - startL/2, screenH / 2.5 +200))
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
    screen.blit(backgroundI,(50, 25))
    #screen.blit(queue, (0,0))
    mat = Mat()
    mat.draw(screen)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def main():
    startMenu()

class Mat():
    def __init__(self):
        self.img = pygame.image.load('mat.png.')
        self.pos = [300,300]
    def draw(self, screen):
        screen.blit(self.img, self.pos)

if __name__ == "__main__":
    main()

