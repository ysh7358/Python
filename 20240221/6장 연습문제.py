'''
#연습문제 1번
for i in range(1, 101) :
    if i % 2 == 0 :
        print(i, end = '')

#연습문제 2번
for i in range(2, 10) :
    for j in range(1, 10) :
        print(i*j)
        
#연습문제 3번
import turtle
t = turtle.Turtle()
for i in range(3) :    
    t.forward(100)
    t.left(120)

#연습문제 4번
import turtle, random
t = turtle.Turtle()

for i in range(10) :
    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)
    r = random.randint(1, 100)
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(r)

#연습문제 5번 (각 자리 숫자의 합)
n = 1234
sum = 0
while n > 0 :
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)

#연습문제 6번
year = 0
balance = 1000
while balance < 2000 :
    year = year + 1
    balance = balance*1.07
print(year)

#연습문제 7번
import turtle
t = turtle.Turtle()
for i in range(10) :
    t.fd(100)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(20)
    t.lt(90)
    t.write(abs(t.pos()))

#연습문제 8번
import random
num1 = 0
num2 = 0
player = 1
while(num1*num2 != player) :
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    player = int(input(str(num1) + "*" + str(num2) + "= ?"))
print("게임 종료")
'''
