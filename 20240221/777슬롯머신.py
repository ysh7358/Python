import random

number = random.randint(0, 999)
jackpot = 777
count = 1

while(number != jackpot) :
    print(number)
    count = count + 1
    number = random.randint(0, 999)

print("잭팟(777)이 나올 때까지의 총 횟수는 : " + str(count) + "입니다")
