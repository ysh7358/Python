import random

gameCount = 0
player = 0

computer = random.randint(1,50)

while(player != computer) :
    
    player = int(input("업다운 게임입니다. 1~50까지의 정수를 입력해주세요. : "))
    gameCount = gameCount + 1
    
    if player > computer :
        print("입력하신 수 보다 작습니다")
        
    elif player < computer :
        print("입력하신 수 보다 큽니다")
        
    else :
        print("빙고! 총 플레이 횟수는 " + str(gameCount) + "입니다")
        print("게임 종료")
