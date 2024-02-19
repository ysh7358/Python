'''number = int(input("번호를 입력해주세요 : "))
if (number % (2*3) == 0) :
    print("당첨")
else :
    print("다음 기회에")'''

'''number = int(input("번호를 입력해주세요 : "))
if (number % 2 == 0) and (number % 3 == 0) :
    print("당첨")
else :
    print("다음 기회에")'''

number = int(input("번호를 입력해주세요 : "))
if (number % 2 == 0) :
    if (number % 3 == 0) :
        print("당첨")
else :
    print("다음 기회에")
