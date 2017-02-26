import random
import pygame
import time
import sys
import time
#colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.init()
file = "song.mp3"
#screen variables
screenH = 800
screenW = 800
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("This is the Game")
clock = pygame.time.Clock()
johncena = pygame.image.load('johnce.png')
belt = pygame.image.load('Belt2.png')
fist = pygame.image.load('Fist2.png')
john_w = 90
john_h = 119
belt_w = 50
belt_h = 40
pygame.mixer.music.load(file)
def scoreD(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score: " + str(count), True, blue)
    screen.blit(text, (650, 0))

def player(x,y):
    screen.blit(johncena,(x, y))
def enemy(x, y):
    #pygame.draw.rect(screen, blue, [startx, starty, width, height])
    screen.blit(fist, (x, y))

def ally(x,y):
    screen.blit(belt, (x, y))


def main():
    x1 = (screenH * 0.45)
    y1 = (screenW * 0.8)
    enemy_s = 7
    running = 1
    changex = 0
    starty = -200
    startx = random.randrange(0, screenW - 50)
    width = 60
    height = 57
    score = 0
    belt_sy = -800
    belt_sx = random.randrange(0, screenW- 50)
    belt_speed = 5
    while running == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changex = -5
                if event.key == pygame.K_RIGHT:
                    changex = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    changex = 0
        temp = x1
        temp += changex
        if temp > screenW - john_w or temp < 0:
            changex = 0
        x1 += changex
        screen.fill(black)
        enemy(startx, starty)
        ally(belt_sx, belt_sy)
        starty += enemy_s
        belt_sy += belt_speed
        player(x1, y1)
        if y1 < starty + height: #detects if you get hit
            if ((x1 > startx and x1 < startx + width) or (x1 + john_w > startx and x1 + john_w < startx + width) or startx > x1 and startx < x1 + john_w):
                main()
        if y1 < belt_sy + belt_h:
            if ((x1 > belt_sx and x1 < belt_sx + belt_w) or (x1 + john_w > belt_sx and x1 + john_w < belt_sx + belt_w) or belt_sx > x1 and belt_sx < x1 + john_w):
                score += 1
                belt_sy = -500
                belt_sx = random.randrange(0, screenW - 50)
        scoreD(score)
        if starty > screenH:
            starty = 0 - 10
            startx = random.randrange(0, screenW -50)
        if belt_sy > screenH:
            belt_sy = -500
            belt_sx = random.randrange(0, screenW -50)

        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()



