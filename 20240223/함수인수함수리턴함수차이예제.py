'''
두 수를 키보드로 입력받아서
f 함수에서 두 수 덧셈 출력

1. 함수 ( 예 f1()
2. 인수가 있는 함수
3. 리턴이 있는 함수

def f1() :
    a = int(input("첫 번째 수를 입력해 주세요"))
    b = int(input("두 번째 수를 입력해 주세요"))
    print(a+b)
f1()

n1 = int(input("첫 번째 수를 입력해 주세요"))
n2 = int(input("두 번째 수를 입력해 주세요"))
def f2(num1, num2) :
    print(num1 + num2)
f2(n1, n2)

n1 = int(input("첫 번째 수를 입력해 주세요"))
n2 = int(input("두 번째 수를 입력해 주세요"))

def f3(num1, num2) :
    return(num1 + num2)

value = f3(n1,n2)
print(value)
'''

def f4() :
    num1 = int(input("첫 번째 수를 입력해 주세요"))
    num2 = int(input("두 번째 수를 입력해 주세요"))
    return num1 + num2
value = f4()
print(value)
