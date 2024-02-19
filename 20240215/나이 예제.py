import time

print(time.time())
a = time.time()
b = int(1970 + a//(365*24*3600))
print("올해는" , b)
c = int(input("출생년도 입력 : "))
print("당신의 나이는 만" , (b-c) + 1 , "세 입니다.")
