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
