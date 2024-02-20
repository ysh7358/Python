# 193p 랜덤워크 시뮬레이션.
# 화면 밖으로 벗어났을 때 화면 중앙으로 돌아오기 까지 구현.

import turtle
import random

# 화면 크기 설정
screen = turtle.Screen()
screen.setup(width=800, height=600)  # 적절한 크기로 조정 가능

t = turtle.Turtle()
t.shape("turtle")           # 펜모양 거북이
turtle.colormode(255)   # 선 색깔  R,G,B 모드 사용
turtle.bgcolor("black")      # 배경 :  BLACK

for i in range(30):
    r = random.randint(0, 255)      # R 랜덤
    g = random.randint(0, 255)      # G 랜덤
    b = random.randint(0, 255)      # B 랜덤
    t.color(r, g, b)                        # 펜색깔

    ps=random.randint(1,10)         # 펜사이즈 랜덤 1~10
    t.pensize(ps)                       
    
    length = random.randint(80,100)            # 80~100 에서 무작위 수 하나를 length 에 저장
    t.forward(length)                               # length 만큼 앞으로 이동
    angle = random.randint(-180,180)      # -180 ~ 180 에서 무작위 수 하나 angle 에 저장
    t.right (angle)                                 # angle 만큼 오른쪽으로 회전

    # 화면 바깥으로 나갔을 때 처리
    if t.xcor() > screen.window_width() / 2 or t.xcor() < -screen.window_width() / 2 or \
            t.ycor() > screen.window_height() / 2 or t.ycor() < -screen.window_height() / 2:
        t.penup()
        t.goto(0, 0)
        t.pendown()

turtle.done()
