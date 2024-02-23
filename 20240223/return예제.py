'''
def f3() :
    print("나는 f3함수")
    return 50

value = f3()
print(value)

def calculate_area(radius) : #함수 선언
    area = 3.14 * radius **2
    return area

c_area = calculate_area(5.0) #5.0의 값을 함수로 전달해서 받은 return을 c_area에 대입
print(c_area)

#5.0의 값, 10.0의 값을 함수로 전달해서 받은 리턴값의 합
area_sum = calculate_area(5.0) + calculate_area(10.0)

print(area_sum)

def f1(line) :
    square = line * line
    return square

a = int(input("정사각형의 넓이를 구합니다. 한 변의 길이를 정해주세요 : "))

area = f1(a)
print(area)

def f2(sum) :
    total = 0
    for i in range(sum) :
        a = int(input("입력한 수의 누적을 구합니다 : "))
        total = total + a
    return total

answer = f2(10)
print(answer)

def judge(num) :
    if num % 3 == 0 :
        print("3의 배수")
        return
    elif num % 3 == 1 :
        print("3의 배수 + 1")
        return
    else :
        print("3의 배수 + 2")
num = int(input("자연수를 입력하세요: "))
judge(num)
'''
def f3(b) :
    for i in range(b) :
        num = int(input("수 입력 : "))
        if num%2 == 0 :
            print("짝수")
            return
        else :
            print("홀수")

a = int(input("몇 번 반복 입력 : "))
f3(a)
