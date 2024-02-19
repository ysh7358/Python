import turtle
t = turtle.Turtle()
t.shape("turtle")
number = turtle.textinput("N각형 그리기", "3이나 4를 입력해 주세요 : ")
#삼각형 그리기
if number == "3" :
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
#사각형 그리기
elif number == "4" :
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
else :
    t.write("잘못 입력하셨어요. 숫자 3이나 4를 입력해주세요.")
