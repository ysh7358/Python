#동전게임 함수 정의
def fa() :
    print("1. 동전게임 시작")
    import random
    count = 0
    winCount = 0
    s = ["앞", "뒤"]
    while(winCount != 3) : #무한 반복 하고싶으면 True를 넣고, 마지막 print 제거
        count = count + 1
        computer = random.choice(s)
        player = input(str(count) + "번째 동전게임! 앞 / 뒤중 하나를 입력해 주세요 ")
        
        if computer == player :
            winCount = winCount + 1
            print("빙고")
        else :
            print("안빙고")
            print("승리한 횟수는 " + str(winCount) + "회입니다")

    print()
    print("3회 승리하셨습니다. 게임이 종료됩니다.")
    print("총 전적은 " + str(winCount) + "승 " + str(count-winCount) + "패입니다")
    print("승률은 " + str(winCount / count * 100) + "%입니다")
    menu() 

#가위바위보 함수 정의
def fb() :
    print("2. 가위바위보 시작")
    import random
    print("*" * 20)
    print("가위바위보 게임")
    print("*" * 20)
    gameCount = 0
    winCount = 0
    loseCount = 0
    drawCount = 0
    s = ["가위", "바위", "보"]
    while(winCount != 3) : 
        computer = random.choice(s)

        #잘못 냈을 때 반복문 처음으로 돌아감, 게임 횟수 증가X
            
        player = input(str(gameCount + 1) + "번째 게임입니다. 가위, 바위, 보!: ")
        if(player not in ["가위", "바위", "보"]) :
            print("잘못 내셨습니다 가위, 바위, 보 중에 내 주세요.")
            continue
        
        gameCount = gameCount + 1 #게임 횟수 증가
            
        if (player == "가위" and computer == "바위") or (player == "바위" and computer == "보") or (player == "보" and computer == "가위"):
            print("패배했습니다") #패배
            loseCount = loseCount + 1
                
        elif (player == "바위" and computer == "가위") or (player == "보" and computer == "바위") or (player == "가위" and computer == "보"):
            print("승리했습니다") #승리
            winCount = winCount + 1
        else :
            print("비김!") #비김
            drawCount = drawCount + 1

    print("최종 전적은 " + str(gameCount) + "전 " + str(winCount) + "승 " + str(drawCount) + "무 " + str(loseCount) + "패") #전적
    print("승률은 " + str((winCount/gameCount) * 100) + "%입니다.") #최종 승률
    menu()

#성적처리 함수 정의
def fc() :
    print("성적처리")
    #5명의 국어 / 영어 / 수학 점수 입력 받아서 각 과목의 점수와 총점 / 평균 출력 (2차원 리스트)

    score = []
    for i in range(5):
        studentNumber = []              
        koreanScore = int(input(str(i+1) + "번째 학생의 국어 점수를 입력해 주세요 : "))
        englishScore = int(input(str(i+1) + "번째 학생의 영어 점수를 입력해 주세요 : "))
        mathScore = int(input(str(i+1) + "번째 학생의 수학 점수를 입력해 주세요 : "))
        studentNumber.append(koreanScore) 
        studentNumber.append(englishScore)
        studentNumber.append(mathScore)
        studentNumber.append(koreanScore + englishScore + mathScore) #총점
        studentNumber.append((koreanScore + englishScore + mathScore)/3) #평균
        score.append(studentNumber) # N번째 학생의 점수 리스트가 리스트의 N-1번째 인덱스로 들어감
        
    print(score) #리스트 확인

    print(("*" * 19) + "성적표" + ("*" * 19))
    print("번호\t국어\t영어\t수학\t합계\t평균")
    for j in range(5) :
        print(str(j+1) + '\t' ,end = '')
        for i in range(5) :
            print(str(score[j][i]) + '\t',end = '') #2차원 리스트 요소 가져오기
        print() #한 줄 띄우기
    print("*" * 44)
    menu()
          

def menu() :#메뉴
    print()
    while(True) :
        number = input("메뉴를 선택하세요(1.동전게임, 2.가위바위보게임, 3.성적처리) : ")
        if number == "1" :   #동전게임 함수 호출
            fa()
            break

        elif number == "2" :   #가위바위보 함수 호출
            fb()
            break

        elif number == "3" :   #성적처리 함수 호출
            fc()
            break
        else :  #잘못 입력 시 메뉴로 돌아감
            print("번호를 잘못 입력하셨습니다")

menu()
