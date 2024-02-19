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
'''
sum = 0

for e in range (1, 11) :
    sum = sum + e
    print("1부터" , e, "까지의 합 : ", sum)
