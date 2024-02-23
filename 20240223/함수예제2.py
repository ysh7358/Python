num1 = int(input("첫 번째 수를 입력해주세요 : "))
num2 = int(input("두 번째 수를 입력해주세요 : "))

def f2(n1, n2) :
    print(n1," + ", n2, " = ", n1+n2)
    print(n1," - ", n2, " = ", n1-n2)
    print(n1," * ", n2, " = ", n1*n2)
    if n2 == 0 :
        print("0으로 나눌 수 없습니다.")
    else :
        print(n1," / ", n2, " = ", n1/n2)
f2(num1, num2)
