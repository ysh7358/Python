'''
def sum(start, end) :
    total = 0
    for i in range(start, end+1) :
        total = total + i
    print("total =", total)
    
sum(1,10)
sum(10,20)

'''
#두 개의 정수를 입력받아 첫번째 정수부터 두번째 정수까지의 합을 계산
def sum(start, end) :
    total = 0
    for i in range(start, end+1) :
        total = total + i
    print(start, "부터", end, "까지의 합은 " , total, "입니다")

num1 = int(input("시작점을 입력해 주세요 : "))
num2 = int(input("끝점을 입력해 주세요 : "))

sum(num1, num2)
