import turtle
t = turtle.Turtle()
t.shape("turtle")

t.write("안녕하세요! " + name + "님 전 거북이에요")
t.speed(20)
t.forward(100)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(0,-100)
t.down()
t.color("green")
t.forward(100)
t.up()
t.goto(0,100)
t.color("red")
t.down()
t.right(90)
t.forward(100)
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.write(t.pos())
t.home()
t.write(t.pos())
