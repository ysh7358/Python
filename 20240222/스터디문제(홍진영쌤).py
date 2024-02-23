h'''
묵찌빠게임
비길때까지 가위바위보 하다가 비기기전에 이긴사람이 승으로 끝나는 게임
'''
import random

choice = ["가위", "바위", "보"]
player = ""

player, computer = "",""

turn = ""
while(True) :
    computer = random.choice(choice) # 컴퓨터 선택
    print(computer)
    player = input("가위/바위/보 or 게임 종료는 1: ")
    if (computer == "가위" and player == "바위") or (computer == "바위" and player == "보") or (computer == "보" and player == "가위") :
        turn = "player"
        print(turn + "턴")
        break

    elif (computer == "바위" and player == "가위") or (computer == "보" and player == "바위") or (computer == "가위" and player == "보") :
        turn = "computer"
        print(turn + "턴")
        break
    elif (computer == "바위" and player == "바위") or (computer == "보" and player == "보") or (computer == "가위" and player == "가위") :
        print("비겼습니다")
        continue
    else :
        print("가위 바위 보 중에 내주세요")
        continue

while(computer != player) :
    computer = random.choice(choice) # 컴퓨터 선택
    print(computer)
    player = input("가위/바위/보 or 게임 종료는 1: ")
    if (computer == "가위" and player == "바위") or (computer == "바위" and player == "보") or (computer == "보" and player == "가위") :
        turn = "player"
        print(turn + "턴")
    elif (computer == "바위" and player == "가위") or (computer == "보" and player == "바위") or (computer == "가위" and player == "보") :
        turn = "computer"
        print(turn + "턴")
    elif (computer == "바위" and player == "바위") or (computer == "보" and player == "보") or (computer == "가위" and player == "가위") :
        if turn == "computer" :
            print("컴퓨터 승리")
            break
        elif turn == "player" :
            print("유저 승리")
            break
    else :
        print("가위 바위 보 중에 내주세요")
        
print("게임을 종료합니다!!")
