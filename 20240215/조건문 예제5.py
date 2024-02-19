a = int(input("국어 점수를 입력하세요 : "))
b = int(input("수학 점수를 입력하세요 : "))
c = int(input("영어 점수를 입력하세요 : "))

avg = (a+b+c) / 3

if avg >= 90 :
    print("합격입니다")

else :
    print("불합격입니다")
