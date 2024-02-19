import time
now = time.time()
nowYear = int(1970 + now//(3600*24*365))
nowMonth = int((now%(3600*24*365)) // (3600*24*(365/12)))
print(nowMonth)
print("현재 연도는  " + str(nowYear) + "년입니다.")
bornYear = int(input("출생 연도를 입력해주세요 : "))
age = nowYear - bornYear + 1
print("현재 나이는 " + str(age) + "세입니다.")
