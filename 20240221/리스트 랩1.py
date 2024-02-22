'''
#1번
king_table = []
for i in range(4) :
    king = input("조선시대 왕 순서 구절을 입력하시오: ")
    king_table.append(king)

print(king_table)

count = 1

for i in king_table :
    for j in i :
        if j == '연' :
            print('연산군')
        elif j == '광' :
            print('광해군')
        elif count in [1, 7, 14, 16, 21, 22, 23] :
            print(j + '조')
        else :
            print(j + '종')
        count = count + 1

#3번
import turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)
length = 10
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
while length < 500 :
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length+=5
'''
#5번
temp_list = [0, 10, 20, 30]
vapor_list = [4.8, 9.4, 17.3, 30.4]

temp = int(input())

if temp in temp_list :
    index = temp_list.index(temp)
    print(index)
    print(vapor_list[index])
