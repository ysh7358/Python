import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = int(input("그리고자 하는 원의 반지름을 입력하세요: "))
firstColor = input("첫 번째 원의 색을 입력하세요: ")
secondColor = input("두 번째 원의 색을 입력하세요: ")
thirdColor = input("세 번째 원의 색을 입력하세요: ")

t.color(firstColor)
t.begin_fill()
t.circle(radius)
t.end_fill()
t.up()
t.goto(0, -radius*2)
t.down()
t.color(secondColor)
t.begin_fill()
t.circle(radius)
t.end_fill()
t.up()
t.goto(0, -radius*4)
t.down()
t.color(thirdColor)
t.begin_fill()
t.circle(radius)
t.end_fill()
