# 두 수의 뺄셈 문제

import random

num1 = random.randrange(100) + 1
num2 = random.randrange(100) + 1

print(num1, num2)

if num1 >= num2 :
    answer = num1 - num2
    playerAnswer = input(str(num1) + " - " + str(num2) + " = ? ")
    
else :
    answer = num2 - num1
    playerAnswer = input(str(num2) + " - " + str(num1) + " = ? ")

if answer == int(playerAnswer) :
    print("정답이에요")

else :
    print("오답이에요")
