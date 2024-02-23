# 20240223 스터디 문제

'''
5자리로 이루어진 ‘행운복권‘이 있습니다. 
이 복권을 구매하는 구매자가 정한 숫자 5개가
모두 일치하면 100만원, 3개가 일치하면 50만원,
1개만 일치하면 만원을 받을 수 있어요.
하나도 일치하지 않으면 “다음 기회에”가
출력되고 일치하는 숫자에 따라 각각의 상금이 출력되도록 작성해봐요!
'''
import random

lottoarray = []
myarray = []
count = 0

lotto = random.randrange(10000,99999)
print(lotto)
lottoarray.append(lotto // 10000)
lottoarray.append((lotto % 10000) // 1000)
lottoarray.append((lotto % 1000) // 100)
lottoarray.append((lotto % 100) // 10)
lottoarray.append(lotto % 10)
print(lottoarray)
myNum = int(input("내 번호를 입력해 주세요(10000에서 99999까지) : "))

myarray.append(myNum // 10000)
myarray.append((myNum % 10000) // 1000)
myarray.append((myNum % 1000) // 100)
myarray.append((myNum % 100) // 10)
myarray.append(myNum % 10)
print(myarray)
for i in range(5) :
    if myarray[i] == lottoarray[i] :
        count = count + 1

if count == 5 :
    print("100만원을 받았어요")
elif count >= 3 :
    print("50만원을 받았어요")
elif count >= 1 :
    print("1만원을 받았어요")
else :
    print("다음 기회에")
