### 돌피하기 게임 - 돌 하나만 구현 ###

import pygame
import random

# pygame을 실행할때는 init(), 종료할때는 quit()을 꼭 적어줘야 함!
pygame.init()
clock = pygame.time.Clock()

# 창 크기 지정
background = pygame.display.set_mode((480, 360))
# 창 이름 지정
pygame.display.set_caption('Moving Game')

# fps설정
clock = pygame.time.Clock()

    ### 게임 물체 자동차 설정 ###
# 화면 가장 하단, 중간에 위치하도록 x, y 좌표 설정
player_x_p = background.get_size()[0] // 2 -10  # 230
player_y_p = background.get_size()[1] - 50  # 310

# 게임 물체 설정
player = pygame.image.load("Player.png")
player = pygame.transform.scale(player, (20, 50))

# 좌표 이동 누적값 설정
to_x = 0
to_y = 0


    ### 장애물 돌 설정 ###
# 생성 위치 가장 상단, 좌우 랜덤 설정
stone_x_p = random.randint(0, background.get_size()[0])
stone_y_p = 0
stone_speed = 0

# 장애물 설정
stone = pygame.image.load("Stone.png")
stone = pygame.transform.scale(stone, (40, 60))

# boolean 함수를 생성해 while문 작성
play = True
while play:
    df = clock.tick(60) #20인 이유? 그냥 내 감

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # game의 event type이 QUIT 명령이라면
            play = False  # while문을 종료시킴

        # 방향키 player 이동
        if event.type == pygame.KEYDOWN:  # game의 event type이 키보드를 누른 상태일 때
            if event.key == pygame.K_UP:
                to_y = - 10  # pygame에서는 위로 올라갈수록 y값이 감소한다.
            elif event.key == pygame.K_DOWN:
                to_y = + 10
            elif event.key == pygame.K_RIGHT:
                to_x = + 10
            elif event.key == pygame.K_LEFT:
                to_x = - 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0

        # 가로 경계값 처리
        if player_x_p < 0:
            player_x_p = 0
        elif player_x_p > background.get_size()[0] - player.get_size()[0]:
            player_x_p = background.get_size()[0] - player.get_size()[0]

        # 세로 경계값 처리
        if player_y_p < 0:
            player_y_p = 0
        elif player_y_p > background.get_size()[1] - player.get_size()[1]:
            player_y_p = background.get_size()[1] - player.get_size()[1]

    # 충돌 처리를 위한 rect 정보 업데이트
    player_rect = player.get_rect()
    player_rect.left = player_x_p # 위치가 계속 변하기 때문에 업데이트가 필요하다.
    player_rect.top = player_y_p

    stone_rect = stone.get_rect()
    stone_rect.left = stone_x_p
    stone_rect.top = stone_y_p

    # 충돌설정
    if player_rect.colliderect(stone_rect): # 만약 캐릭터가 적과 충돌 했을 때
        play = False

    # 돌 낙하
    if stone_y_p < background.get_size()[1]: # 바닥 닿기 전까지 아래로 낙하
        stone_y_p = stone_y_p + 10 + stone_speed
    elif stone_y_p >= background.get_size()[1]: # 바닥에 닿으면 랜덤 리스폰
        stone_x_p = random.randint(0, background.get_size()[0])
        stone_y_p = 0

    stone_speed += 0.1

    # 변수 저장값을 좌표에 누적
    player_x_p += to_x
    player_y_p += to_y

    # 항상 배경 - 이미지(도형) 순으로 코드를 작성해야 함! (반대로 하면 이미지가 배경에 덮여버림)
    background.fill((255, 255, 255))  # 배경색 : 흰색
    background.blit(player, (player_x_p, player_y_p))
    background.blit(stone, (stone_x_p, stone_y_p))
    pygame.display.update()  # 현재 화면 상태를 업데이트

pygame.quit()
