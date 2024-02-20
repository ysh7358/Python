#무한한 동전게임, 3빙고일때 게임 종료

#while(True)로 주고 아래쪽에서 if winCount == 3 break 걸어도 됨

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
