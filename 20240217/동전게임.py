import random
'''
num = random.randrange(2)

if num == 1 :
    computer = "앞"

else :
    computer = "뒤"

player = input("앞 / 뒤! 어디에 거시겠습니까 : ")
print("컴퓨터는 " + computer + "입니다")

if player == computer :
    print("빙고")

else :
    print("안빙고")
'''

s = ['앞' , '뒤' ]

computer = random.choice(s)
print(computer)
player = input("앞 / 뒤! 어디에 거시겠습니까 : ")

if player == computer :
    print("빙고")

else :
    print("안빙고")
    
