
while True :
    try :
        age = int(input("나이를 입력해주세요 : "))
        print(str(age)+"살")
        break
    except :
        print("입력 오류")
'''
#함수를 활용

def age_input() :
    try :
        age = int(input("나이를 입력해주세요 : "))
        return age
    except :
        return age_input()

print(age_input())
'''
