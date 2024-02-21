'''
for i in range(5):
    for j in range(5) :
        print("*", end = ' ')
    print()
for a in range(3) : #0~2
    for b in range(5) : #0~4
        print("a = ", a, " , b  =" ,b)
for i in range(1,6) :
    for j in range(1, i+1) :
        print("*", end = '')
    print()
'''

'''
for i in range(5,0,-1) :
    for j in range(1, i+1) :
        print("*", end = '')
    print()

for i in range(1,6) :
    for j in range(-6, -i) :
        print("*", end = '')
    print()
'''
for i in range(5) :
        print("*" * (5-i))

i = 5
while(i != 0) :
    print("*" * i )
    i = i - 1
