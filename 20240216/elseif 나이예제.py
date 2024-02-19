#나이를 입력받아서 1,2,30대 / 해당없음을 출력하는 문제

age = float(input("나이를 입력해주세요 : "))
generation = int(age // 10)

if(age<0 or (float(age) - int(age) != 0)) :
    print("잘못 입력하셨습니다")
else :
    if (1<=generation<=3) :
        print(str(generation) + "0대 입니다.")
    else :
        print("해당 없음")
'''
a = int(input("나이 : "))
print(str(a//10) + "0대 ")
print((a//10)*10 , "대")
'''
