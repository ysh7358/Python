#문제 f1함수에서 나이를 입력받아서 성인 / 안성인 출력

def f1() :
    age = int(input("나이를 입력해 주세요 : "))
    
    if age >= 20 :
        print("성인입니다")
    elif age <= 0 :
        print("타임머신을 타셨나요?")
    else :
        print("안성인입니다")

f1()
