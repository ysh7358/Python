file = open("kor.txt", "w")

for i in range(1,11) :
    while True :
        try :
            score = int(input(str(i) + "번째 학생의 국어 점수를 입력해주세요: "))
            file.write(str(i) + "번째 학생의 점수는 : " + str(score) + "\n")
            break
        except :
            print("잘못 입력했어요")
            continue

file.close()
