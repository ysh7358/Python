#문제 : 메인에서 주민번호 입력받아서 f2 함수에서 나이와 성별 출력
import time
now = time.time()
def f2(y, s) :
    year = int(1970 + now // (365 * 24 * 3600))
    
    age = year - y
    
    print("당신의 나이는 ", age)
    
    if int(s[7]) % 2 == 0 :
        print("여자")
    else:
        print("남자")
        
a = int(input("출생년도 : "))
b = input("주민번호 : ")

f2(a,b)

'''
from datetime import datetime
todayyear = datetime.now().year

myNumber = input("주민번호를 입력해주세요 : ")

def f2(number) :
    
    if(int(number[7]) % 2 == 0) :2
        print("여자입니다")
    else :
        print("남자입니다")

    if(number[7] == "1" or number[7] == "2") :
        birthyear = int("19" + number[0] + number[1])
        age = todayyear - birthyear + 1
        print("현재 나이는 " + str(age) + "입니다.")
        
    elif(number[7] == "3" or number[7] == "4") :
        birthyear = int("20" + number[0] + number[1])
        age = todayyear - birthyear + 1
        print("현재 나이는 " + str(age) + "입니다.")

f2(myNumber)
'''
