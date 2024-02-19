#국, 영, 수 점수 입력받아서 평균이 90이상 A 80이상 B 70이상 C 60이상 D 나머지 F
a = float(input("국어 점수를 입력해 주세요 : "))
b = float(input("수학 점수를 입력해 주세요 : "))
c = float(input("영어 점수를 입력해 주세요 : "))

#100점 초과 / 0점 미만의 점수는 없음
if (a or b or c) < 0 or (a or b or c) > 100 :
    print("점수를 잘못 입력하셨습니다")
else :
    #평균 점수 구하기
    avg = (a+b+c) / 3
    print("평균 점수는 " + str(avg) + "입니다.")
    if avg >= 90 :
        print("A")
    elif avg >= 80 :
        print("B")
    elif avg >= 70 :
        print("C")
    elif avg >= 60 :
        print("D")
    else :
        print("F")

