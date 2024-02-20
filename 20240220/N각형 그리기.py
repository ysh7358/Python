import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

a = int(turtle.textinput("", "몇 각형을 그리시겠습니까?"))
for i in range(a) : #반복횟수는 n각형의 획수와 같다
    t.fd(1)
    t.lt(360/a) #총 외각은 360이므로 360/s를 하면 각도를 구할 수 있음
'''
for i in range(30) :
    t.fd(random.randrange(1,100))
    t.lt(random.randrange(0,360))
'''
