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
winCount = 0
s = ['앞' , '뒤' ]

for i in range(10) :
    print(str(i+1) + "번째 게임입니다.")
    computer = random.choice(s)
    print(computer)
    player = input("앞 / 뒤! 어디에 거시겠습니까 : ")

    if player == computer :
        print("빙고\n")
        winCount = winCount + 1

    else :
        print("안빙고\n")

print("승리한 횟수는 " + str(winCount)+ "회입니다.")
