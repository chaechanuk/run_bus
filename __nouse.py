from pickle import REDUCE
from pickletools import read_unicodestring1
import pygame
from pygame import K_RIGHT, QUIT,                                                                                                                                                                     KEYDOWN, K_LEFT, Rect, K_DOWN , K_UP
import random

# 창크기
w = 900 #가로크기
h = 700 #세로크기
# s: 창에 관한 모든 정보
s = pygame.display.set_mode(    (w, h)     )
# 시간과 관련된 모든 정보
cloc = pygame.time.Clock()
# 사각형의 최초위치
x1 = 699
y1 = -499

x2 = 30
m1 = 70
m2 = 70
y2 = 15

x = random.randrange(1,800)

x1 += x

x3 = 50
y3 = 200
w3 = 300
h3 = 50

x4 = 50
y4 = 500
w4 = 100
h4 = 200
image = pygame.image.load('./rocket2.png')
image_width = image.get_width()
image_height = image.get_height()
print(image_width, image_height)
image = pygame.transform.scale(image, (image_width//3 , image_height//3))

# 색상 튜플 (R, G, B)
BLACK = ( 0, 0 , 0)
GREEN = (0 , 255, 0 )
BLUE = (0 , 0, 255)
RED = (255,0,0)
# 테두리 굶기 (0이면 안쪽 색칠)
Th = 1
# 파이게임 루프
running =True

mx = 0
my = 0
while running:
    
    # 모든 이벤트를 검사
    for event in pygame.event.get():
        # 만약 가져온 이벤트가
        # 종료버튼을 누른 것이라면
        if event.type == QUIT:
            running = False
            break

    mykeys = pygame.key.get_pressed()
    if mykeys[K_RIGHT]:
        m1 += 2
    elif mykeys[K_LEFT]:
        m1 -= 2
  

    s.fill( (0,0,0)  )
    s.blit(image, (m1,m2))


    # 화면을 주기적으로 다시 그려줌(1/60초,마다)
    pygame.display.update()
    cloc.tick(144)