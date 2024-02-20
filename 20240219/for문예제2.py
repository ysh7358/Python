'''
#1부터 10까지 출력
for a in range(1, 11) :
    print(a)

#1부터 10까지의 홀수 출력
for b in range(1, 11) :
    if b%2 == 1 :
        print(b)
        
#1부터 10까지의 짝수 출력
for c in range(1, 11) :
     if c%2 ==  0:
        print(c)
        
#10부터 1까지의 짝수 출력
for d in range (10, 0, -1) :
    if d%2 == 0 :
        print(d)

#1부터 10까지의 합
sum = 0

for e in range (1, 11) :
    sum = sum + e
    print("1부터" , e, "까지의 합 : ", sum)

#1부터 입력한 값까지 홀/짝수의 합

print("1부터 입력한 수 까지의 홀수 짝수의 합을 구하는 프로그램")

sum1 = 0
sum2 = 0

e = int(input("숫자를 입력해 주세요 : "))

for e in range (e+1) :
    if e % 2 == 1 :
        sum1 = sum1 + e
        
    elif e % 2 == 0 :
        sum2 = sum2 + e
        
print("1부터" , e, "까지의 홀수 합 : ", sum1)
print("1부터" , e, "까지의 짝수 합 : ", sum2)

#1부터 입력한 값까지 홀/짝수의 곱

print("1부터 입력한 수 까지의 홀수 짝수의 합을 구하는 프로그램")

num1 = 1
num2 = 1

e = int(input("숫자를 입력해 주세요 : "))

for e in range (1, e+1) :
    if e % 2 == 1 :
        num1 = num1 * e
        
    elif e % 2 == 0 :
        num2 = num2 * e
        
print("1부터" , e, "까지의 홀수 곱 : ", num1)
print("1부터" , e, "까지의 짝수 곱 : ", num2)

print("1부터 입력한 수 까지의 전체와 홀짝으로 덧셈 곱셈을 하는 프로그램")
print()

sum1 = 0
sum2 = 0
num1 = 1
num2 = 1

f = int(input("숫자를 입력해 주세요 : "))
print("숫자", f ,"를 입력하셨습니다")
print()

for e in range (1, f+1) :
    
    if e % 2 == 1 :
        sum1 = sum1 + e
        num1 = num1 * e
        
    elif e % 2 == 0 :
        num2 = num2 * e
        sum2 = sum2 + 2
        
sum = sum1 + sum2
num = num1 * num2

print("1부터" , f, "까지의 홀수 합 : ", sum1)
print("1부터" , f, "까지의 홀수 곱 : ", num1)
print("1부터" , f, "까지의 짝수 합 : ", sum2)
print("1부터" , f, "까지의 짝수 곱 : ", num2)
print("1부터" , f, "까지의 합 : ", sum)
print("1부터" , f, "까지의 곱 : ", num)

#농구선수 10명의 키를 입력받아서 키의 총합을 출력
sum = 0
maxheight = 0
minheight = 0
index1 = 0
index2 = 0

for i in range(10) :
    height = int(input("농구선수의 키를 입력해주세요 (단위 : cm) : "))
    if i == 0 :
        minheight = height
        
    else : 
        if height > maxheight :
           maxheight = height
           index1 = i+1
           
        if height < minheight :
            minheight = height
            index2 = i+1
            
    sum = sum + height
    
print("농구선수의 키의 총합은 ",sum,"cm 입니다")
print("가장 작은 키를 가진 선수는 ", index2, "번째 선수로," ,minheight, "cm 입니다")
print("가장 큰 키를 가진 선수는 ", index1, "번째 선수로," ,maxheight, "cm 입니다")
'''

