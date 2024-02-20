import turtle, random #터틀 / 랜덤 가져오기

t = turtle.Turtle() #터틀 불러오기
t.pensize(3) #펜의 굵기

count = int(turtle.textinput("", "사각형의 갯수를 정해주세요")) #사각형 갯수 입력받기
for i in range(count) : #입력한 횟수만큼 반복
    r = random.random() #red 색깔 (0~1 사이의 난수) 
    g = random.random() #green 색깔
    b = random.random() #blue 색깔

    x = random.randint(-300,300) # x좌표값 (-300~300 사이의 정수)
    y = random.randint(-300,300) # y좌표값 (-300~300 사이의 정수)
    length = random.randint(10,300) # 사각형 한 변의 길이(10~300 사이의 정수)

    t.pencolor("black") #펜의 색깔을 검정색으로 지정
    t.penup() #펜 들기
    t.goto(x,y) #위에서 지정한 x,y 좌표값으로 이동
    t.pendown() #펜 내리기
    t.fillcolor(r, g, b) #위에서 지정한 rgb색으로 펜의 색깔을 변경
    t.begin_fill() 
    for j in range(4) : #한 변의 길이가 length인 사각형 그리기
        t.forward(length)
        t.right(90)
    t.end_fill()
    
turtle.write(str(count) + "개의 사각형을 그렸어요!") #사각형의 갯수를 출력
