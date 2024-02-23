#전해주는 파라미터와 전달받는 파라미터의 이름은 다르게 선정하자

myAge = int(input("나이를 입력해주세요 : "))

def f2(age) :
    if age >= 20 :
        print("성인")
    else :
        print("안성인")

f2(myAge)
