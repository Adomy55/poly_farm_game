import pygame, sys, time
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 600
TOPBL = 60
FARMSPACE = 108
UPGRADESPACE = 60
ballance = 0
FARMSTART = 600
#polygons
class triangle:
    cool_down = 3
    money = 1
    is_unlocked = True
#shapes
triangle_image = pygame.image.load(os.path.join('poly assets', 'triangle.png'))
square_image = pygame.image.load(os.path.join('poly assets', 'square.png'))
pentagon_image = pygame.image.load(os.path.join('poly assets', 'pentagon.png'))
hexagon_image = pygame.image.load(os.path.join('poly assets', 'hexagon.png'))

tri = pygame.transform.scale(triangle_image, ( FARMSPACE - 10, FARMSPACE - 10))
sqwr = pygame.transform.scale(square_image, ( FARMSPACE - 10, FARMSPACE - 10))
pent = pygame.transform.scale(pentagon_image, ( FARMSPACE - 10, FARMSPACE - 10))
hex = pygame.transform.scale(hexagon_image, ( FARMSPACE - 10, FARMSPACE - 10))

#color
BG_COLOR = (150, 150, 160)
TOPBAR = (120, 170, 255)
FARMBG = (255, 255, 30)
BLACK = (0, 0, 0)
TOOLSCOLOR = (130, 255, 130)
#main screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("poly farm")
screen.fill(BG_COLOR)
pygame.draw.line(screen, FARMBG, (WIDTH - 150, 0), (WIDTH - 150, HEIGHT), 300)
#seperation lines
pygame.draw.line(screen, BLACK, (WIDTH - 300, 0), (WIDTH - 300, HEIGHT), 5)
pygame.draw.line(screen, BLACK, (WIDTH - 300, TOPBL + FARMSPACE), (WIDTH, TOPBL + FARMSPACE), 5)
pygame.draw.line(screen, BLACK, (WIDTH - 300, TOPBL + FARMSPACE * 2), (WIDTH, TOPBL + FARMSPACE * 2), 5)
pygame.draw.line(screen, BLACK, (WIDTH - 300, TOPBL + FARMSPACE * 3), (WIDTH, TOPBL + FARMSPACE * 3), 5)
pygame.draw.line(screen, BLACK, (WIDTH - 300, TOPBL + FARMSPACE * 4), (WIDTH, TOPBL + FARMSPACE * 4), 5)
pygame.draw.line(screen, TOOLSCOLOR, (150, 0), (150, HEIGHT), 300)
pygame.draw.line(screen, BLACK, (300, 0), (300, HEIGHT), 5)
#seperation lines
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE), (300, TOPBL + UPGRADESPACE), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*2), (300, TOPBL + UPGRADESPACE*2), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*3), (300, TOPBL + UPGRADESPACE*3), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*4), (300, TOPBL + UPGRADESPACE*4), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*5), (300, TOPBL + UPGRADESPACE*5), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*6), (300, TOPBL + UPGRADESPACE*6), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*7), (300, TOPBL + UPGRADESPACE*7), 3)
pygame.draw.line(screen, BLACK, (0, TOPBL + UPGRADESPACE*8), (300, TOPBL + UPGRADESPACE*8), 3)
pygame.draw.line(screen, TOPBAR, (0, 30), (WIDTH, 30), 60)
#images display
screen.blit(tri, (FARMSTART + 5, TOPBL + 5))
screen.blit(sqwr, (FARMSTART + 5, TOPBL + FARMSPACE + 5))
screen.blit(pent, (FARMSTART + 5, TOPBL + FARMSPACE * 2 + 5))
screen.blit(hex, (FARMSTART + 5, TOPBL + FARMSPACE * 3 + 5))
pygame.draw.circle(screen, BLACK, (FARMSTART + 5 + 55, TOPBL + FARMSPACE * 4 + 60), 45, 5)
#STATS
BAL_font = pygame.font.SysFont('comicsans', 40)
ballance_text = BAL_font. render(str(ballance), 1, BLACK)
screen.blit(ballance_text, (WIDTH - 10 - ballance_text.get_width(), 10))

def farm(polygon):
    if polygon == "triangle":
        print("clicked triangle")
    if polygon == "square":
        print("clicked square")
    if polygon == "pentagon":
        print("clicked pentagon")
    if polygon == "hexagon":
        print("clicked hexagon")
    if polygon == "circle":
        print("clicked circle")

def buy_upgrade(upgrade):
    if upgrade == 1:
        print("first upgrade")
    if upgrade == 2:
        print("second upgrade")
    if upgrade == 3:
        print("third upgrade")
    if upgrade == 4:
        print("fourth upgrade")
    if upgrade == 5:
        print("fifth upgrade")
    if upgrade == 6:
        print("sixth upgrade")
    if upgrade == 7:
        print("seventh upgrade")
    if upgrade == 8:
        print("eight upgrade")
    if upgrade == 9:
        print("ninth upgrade")
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
          mousex = event.pos[0]
          mousey = event.pos[1]
          if mousex >= 600:
              if mousey >= TOPBL + FARMSPACE * 4:
                  farm("circle")
              elif mousey >= TOPBL + FARMSPACE * 3:
                  farm("hexagon")
              elif mousey >= TOPBL + FARMSPACE * 2:
                  farm("pentagon")
              elif mousey >= TOPBL + FARMSPACE:
                  farm("square")
              elif mousey >= TOPBL:
                  farm("triangle")
          if mousex <= 300:
              if mousey >= TOPBL * 9:
                  buy_upgrade(9)
              elif mousey >= TOPBL * 8:
                  buy_upgrade(8)
              elif mousey >= TOPBL * 7:
                  buy_upgrade(7)
              elif mousey >= TOPBL * 6:
                  buy_upgrade(6)
              elif mousey >= TOPBL * 5:
                  buy_upgrade(5)
              elif mousey >= TOPBL * 4:
                  buy_upgrade(4)
              elif mousey >= TOPBL * 3:
                  buy_upgrade(3)
              elif mousey >= TOPBL * 2:
                  buy_upgrade(2)
              elif mousey >= TOPBL * 1:
                  buy_upgrade(1)
    pygame.display.update()
