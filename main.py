from inspect import iscode
from pickle import NONE, TRUE
from turtle import update
import pygame
from pygame import K_RIGHT, MOUSEBUTTONDOWN, QUIT, K_c, K_h, K_DOWN, K_UP, K_u
import random
import time
import math


# 창크기
w = 1300 #가로크기
h = 700 #세로크기
# s: 창에 관한 모든 정보
s = pygame.display.set_mode(    (w, h)     )
# 시간과 관련된 모든 정보
cloc = pygame.time.Clock()
airplane_image = pygame.image.load('./airplane.png')
airplane_image_width = airplane_image.get_width()
airplane_image_height = airplane_image.get_height()
# print(airplane_image_width, airplane_image_height)
airplane_image = pygame.transform.scale(airplane_image, (airplane_image_width//12 , airplane_image_height//12))
airplane_image_width = airplane_image.get_width()
airplane_image_height = airplane_image.get_height()

# 미사일의 위치 변수
# 비행기의 위치 변수
airplane_x = 0
airplane_y = 100
pygame.display.set_caption('run_bus')
start_tick4 = pygame.time.get_ticks()
mouse_x = 0
mouse_y = 0

Fever_Time2 = True





Sky_image = pygame.image.load('./Sky_image.png')
Sky_image_x = 0
Sky_image_y = 0
Sky_image = pygame.transform.scale(Sky_image, (w, h))


bullet_image = pygame.image.load('./bullet2.png')
bullet_image_width = bullet_image.get_width()
bullet_image_height = bullet_image.get_height()
print(bullet_image_width, bullet_image_height)
bullet_ratio = 0.08
bullet_image = pygame.transform.scale(bullet_image, (int(bullet_image_width * bullet_ratio) , int(bullet_image_height*bullet_ratio)))
bullet_image_width = bullet_image.get_width()
bullet_image_height = bullet_image.get_height()
num_bullets = 70 #로켓의 수
bullet_positions = []
bullet_rects = []

for _ in range(num_bullets):
    # 빈 리스트에 원소를 꽁무니에 삽입(추가 함수를 이용해)
    bullet_x = random.randrange(900, 25000)
    bullet_y = random.randrange(1, 630 + bullet_image_height)
    bullet_position = [bullet_x, bullet_y]
    bullet_positions.append(bullet_position)
    bullet_rects.append(pygame.Rect(bullet_x, bullet_y, bullet_image_width, bullet_image_height))


explosion_image = pygame.image.load('./explo2.png')
explosion_image_width = explosion_image.get_width()
explosion_image_height = explosion_image.get_height()
explosion_image = pygame.transform.scale(explosion_image, (explosion_image_width//6, explosion_image_width//6)) 
explosion_image_width = explosion_image.get_width()
explosion_image_height = explosion_image.get_height()
    
    

sleep_time = 0.75
is_collided = []
for i in range(num_bullets):
    is_collided.append(False)

# 색상 튜플 (R, G, B)
BLACK = ( 0, 0, 0)
GREEN = (0 , 255, 0 )
BLUE = (0 , 0, 255)
RED = (255,0,0)
White = (255, 255, 255)
#score
pygame.init()

font1 = pygame.font.SysFont('hy견고딕', 30)


# 테두리 굶기 (0이면 안쪽 색칠)
Th = 1
# 파이게임 루프
running = True

start_tick = pygame.time.get_ticks()
start_tick2 = pygame.time.get_ticks()
start_tick3 = pygame.time.get_ticks()
message_game_over = 'Game Over'
score = 0
game_over = False
bullet_speed = 20
Max_Score = 0
Fever_Time1 = False
Fever_Time = 0

# 안쪽 사각형 비율
ratio = 0.8


# 유도탄 이동(x,y는 탄환의 좌표, mx, my는 캐릭터의 좌표, speed는 탄환의 속도)
def MoveSimpleHomingBullet(x,y, mx, my, speed):
    # 목표까지의 거리: d
    d = math.sqrt((mx-x)*(mx-x)+(my-y)*(my-y))

    # 탄환의 속도 벡터(vx,vy) 구하기
    # 속도가 일정한 값(speed)가 되도록 함
    # 목표까지 거리 d가 0일 때는 속도 벡터를 화면 아래쪽으로 함
    vx = 0
    vy = 0
    if d:
        vx = (mx - x) / d * speed
        vy = (my - y) / d * speed
    else:
        vx = 0
        vy = speed
    
    # 탄환의 좌표(x,y)를 갱신하여 탄환을 이동!
    if x <= 120:
        x2 = x - speed
        y2 = y
    else:
        x2 = x + vx
        y2 = y + vy
    return x2, y2





while running:

    




    
    # 모든 이벤트를 검사
    for event in pygame.event.get():
        
        # 만약 가져온 이벤트가
        # 종료버튼을 누른 것이라면
        if event.type == QUIT:
            running = False
            break

    #키를 검사
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_DOWN] and keys[pygame.K_LCTRL]:
        airplane_y += 5
        Fever_Time += 3
        score -= 1
    if keys[pygame.K_UP] and keys[pygame.K_LCTRL]:
        airplane_y -= 5
        Fever_Time += 3
        score -= 1
    if keys[pygame.K_UP]:
        airplane_y -= 9

    elif keys[pygame.K_LEFT]:
        airplane_x -= 1

    elif keys[pygame.K_RIGHT]:
        airplane_x += 1
    
    elif keys[pygame.K_DOWN]:
        airplane_y += 9

    if keys[pygame.K_UP] and keys[pygame.K_LCTRL] and keys[pygame.K_DOWN]:
        Fever_Time -= 4
        score += 1
    

    if keys[pygame.K_e]:
        num_bullets = 50
        bullet_speed = 15
        Fever_Time2 = False

    

    # if keys[pygame.K_BACKSPACE] and keys[pygame.K_BACKSPACE] and keys[pygame.K_F9] and keys[pygame.K_DELETE] and keys[pygame.K_LEFT]:
    #     score += 1110


    if keys[pygame.K_r] and keys[K_u] and keys[pygame.K_n]:
        score += -0.01
    # airplane_y = airplane_y % (h -70)
    
    if airplane_y <= 0:
        airplane_y = 0
        
    if airplane_y >= h - airplane_image_height:
        airplane_y = h - airplane_image_height
    
    if airplane_x < -1:
        airplane_x = 0

    if score <= -101:
        game_over = True

   
    for i in range(num_bullets):
        # 총알의 번호가 10,15인 경우만 유도탄
        if i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35:
            x = bullet_positions[i][0]
            y = bullet_positions[i][1]
            x2, y2 = MoveSimpleHomingBullet(x,y, airplane_x, airplane_y, bullet_speed)
            bullet_positions[i][0] = x2
            bullet_positions[i][1] = y2
        # 나머지는 일반 탄환
        else:
            bullet_positions[i][0] -= bullet_speed

        if bullet_positions[i][0] <= 0:
            bullet_positions[i][0] = random.randrange(900, 25000) 
            bullet_positions[i][1] = random.randrange(1, 650 + bullet_image_height)
    
        # MoveSimpleHomingBullet(x,y, mx, my, speed)


    # 충돌감지
    rw = bullet_image.get_width()
    rh = bullet_image.get_height()
    for i in range(num_bullets):
        bullet_rects[i] = pygame.Rect(bullet_positions[i][0] + (rw - rw * ratio) // 2, bullet_positions[i][1] + (rh - rh * ratio) // 2, rw * ratio , rh * ratio)

    
    aw = airplane_image.get_width()
    ah = airplane_image.get_height()

    airplane_rect = pygame.Rect(airplane_x + (aw - aw * ratio) // 2,\
        airplane_y + (ah - ah * ratio) // 2, aw * ratio , ah * ratio)
    # airplane_rect = pygame.Rect(airplane_x, airplane_y, aw , ah)


    for i in range(num_bullets):
        is_collided[i] = pygame.Rect.colliderect(bullet_rects[i], airplane_rect)
        if is_collided[i]:
            game_over = True
            break
    
    s.fill((0, 0, 0))
    s.blit(Sky_image, (Sky_image_x, Sky_image_y))
    # 로켓s 그리기
    for i in range(num_bullets):
        s.blit(bullet_image, (bullet_positions[i][0],bullet_positions[i][1])) 

    


    # 게임 오버
    
    if game_over:
        explosion_x = airplane_x
        explosion_y = airplane_y
        ew = explosion_image.get_width()
        eh = explosion_image.get_height()
        s.blit(explosion_image, (explosion_x, explosion_y - eh//4))
        img_game_over_Text = font1.render(message_game_over, True, White)
        # img_game_over_text
        s.blit(img_game_over_Text, (w//2 - 100, h//2-15))
        s.blit(img1, (1000,30))
        s.blit(img3,  (30, 30))
        Fever_Time = 0
        pygame.display.update()
        airplane_x = 0
        
        time.sleep(sleep_time)
        

        for i in range(num_bullets):
            # if is_collided[i]:
            bullet_x = random.randrange(900, 25000)
            bullet_y = random.randrange(1, 600 + bullet_image_height)
            bullet_position = [bullet_x, bullet_y]
            bullet_positions[i] = bullet_position
            bullet_rects[i] = pygame.Rect(bullet_x, bullet_y, bullet_image_width, bullet_image_height)
            is_collided[i] = False 
        
        airplane_y = 100
        score = 0
        game_over = False
        start_tick = pygame.time.get_ticks()
    else:
        s.blit(airplane_image, (airplane_x,airplane_y))
        
        end_tick = pygame.time.get_ticks()
        end_tick2 = pygame.time.get_ticks()
        end_tick3 = pygame.time.get_ticks()
        if end_tick - start_tick > 500:
            start_tick = end_tick
            score += 1
        if Max_Score < score:
            Max_Score = score
        if end_tick2 - start_tick2 > 50 and Fever_Time2:
            start_tick2 = end_tick2
            Fever_Time += 1
    # 화면에 메세지를 띄움
    message = 'Score: '+ str(score)
    message2 = 'Max Score: '+ str(Max_Score)
    message3 = 'Fever Time: '+ str(Fever_Time) + '%'
    message4 = """'E' key is Easy_Mode"""
    img1 = font1.render(message, True, White)
    img3 = font1.render(message2, False, White)
    img4 = font1.render(message3, False, White)
    img5 = font1.render(message4, False, White)
    s.blit(img1, (1000,30))
    s.blit(img3, (30, 30))
    s.blit(img4, (w / 2 - 100, 30))
    if Fever_Time > 100:
       Fever_Time1 = True
    if Fever_Time1:
        Fever_Time -= 2
        if end_tick3 - start_tick3 > 25:
            start_tick3 = end_tick3
            score += 1
        if Fever_Time == 0:
            Fever_Time = 0
            Fever_Time1 = False
    if Fever_Time < -1:
        Fever_Time1 = False
        Fever_Time = 0      
    end_tick4 = pygame.time.get_ticks()
    if not end_tick4 - start_tick4 > 3000:
            s.blit(img5,  (w / 2.6, h / 2.2))

            
            

    # 화면을 주기적으로 다시 그려줌(1/60초,마다)
    pygame.display.update()
    cloc.tick(60)