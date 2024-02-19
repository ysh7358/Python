#입력
print("사칙 연산을 진행합니다. 두 수를 입력해 주세요.")
num1 = int(input("첫 번째 숫자 : "))
num2 = int(input("두 번째 숫자 : "))

plus = num1 + num2
minus = num1 - num2
multiple = num1 * num2
divide = num1 / num2

#출력
print()
print("*" * 20)
print(num1 , "+", num2 , " = " , plus , "입니다." )
print(num1 , "-", num2 , " = " , minus , "입니다." )
print(num1 , "*", num2 , " = " , multiple , "입니다." )
print(num1 , "/", num2 , " = " , divide , "입니다." )
print("*" * 20)
