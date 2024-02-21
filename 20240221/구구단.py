
#구구단 예제
for a in range(2, 10) :
    print(a, "단", "\t", end = '')
for i in range(1, 10) :
    print()
    for j in range(2,10) :
        print(str(j) + "*" + str(i) + "=" +  str(i*j) , "\t", end = '')
'''
#문제 : 단을 입력하면 해당 단을 출력
dan = int(input("출력할 단을 입력해주세요 : "))
print(str(dan)+"단")
for a in range(1, 10) :
    print(dan, "*" , a , "=", dan * a)
'''
