print("각 자릿수의 합을 계산하는 문제")
number = int(input("정수를 입력해 주세요 : "))

firstNumber = number // 1000 # 천의 자리
secondNumber = (number % 1000) // 100 #백의 자리
thirdNumber = (number % 100) // 10 #십의 자리
fourthNumber = number % 10 #일의 자리

total = firstNumber + secondNumber + thirdNumber + fourthNumber #총합

print("각 자릿수의 합은 " , total , "입니다.")
