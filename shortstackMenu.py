import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.init()
screenH = 800
screenW = 800
startL = 274
startH = 56
newgame = pygame.image.load('newgame.png')
newgameC = pygame.image.load('newgame_click.png')
ranking = pygame.image.load('ranking.png')
rankingC = pygame.image.load('ranking_click.png')
level = pygame.image.load('levels.png')
levelC = pygame.image.load('levels_click.png')
screen = pygame.display.set_mode((screenW, screenH))

def startMenu():
    intro = True
    highlight = 1
    enter = 0 #changes to 1 if enter is pushed on a option
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and highlight != 3:
                    highlight += 1
                if event.key == pygame.K_UP and highlight != 1:
                    highlight -= 1
                if event.key == pygame.K_KP_ENTER:
                    enter = 1 # enter is pushed
                    print("HERERERE")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    highlight = 0
        screen.fill(white)
        #mouse = pygame.mouse.get_pos()
        screen.blit(newgame, (screenW/2 - startL/2, screenH/2.5))
        screen.blit(ranking, (screenW / 2 - startL/ 2, screenH / 2.5 + 100))
        screen.blit(level, (screenW / 2 - startL/2, screenH / 2.5 +200))
        if highlight == 1:
            screen.blit(newgameC, (screenW / 2 - startL / 2, screenH / 2.5))
            if enter == 1:
                screen.fill(blue) #testing to see if gets there
        elif highlight == 2:
            screen.blit(rankingC, (screenW / 2 - startL / 2, screenH / 2.5 + 100))
        elif highlight == 3:
            screen.blit(levelC, (screenW / 2 - startL / 2, screenH / 2.5 + 200))
        pygame.display.update()

def main():
    startMenu()

if __name__ == "__main__":
    main()
