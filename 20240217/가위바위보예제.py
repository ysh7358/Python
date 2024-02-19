import random

print("*" * 20)
print("가위바위보 게임")
print("*" * 20)

s = ["가위", "바위", "보"]
computer = random.choice(s)
print(computer)

player = input("가위, 바위, 보 중에 하나를 내 주세요! : ")

if player == computer :
    print("비겼습니다")

else :
    print("안 비김!")
