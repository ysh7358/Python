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

# 가장 간단하고 추천!!!
'''
import random

a =[ "가위", "바위", "보"]

r = random.choice(a)

print(r)

s = input("가위, 바위, 보:")

if r == s :
    print("비김")

elif (r == "가위" and s == "보") or (r == "바위" and s == "가위") or (r == "보" and s == "바위"):
     print("컴퓨터 승!")       
    
else:
    print("플레이어 승!")
'''
