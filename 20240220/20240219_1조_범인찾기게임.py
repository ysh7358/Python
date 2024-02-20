
# 범인 찾기 게임

import random
score = 0     # score :게임점수저장

while True :
    room = random. randint(1,3)
    n = int(input("범인이 있는방은 : ")) # n ; 사용자가 입력한 방 번호

    if n == room :                      # room ;범인이 들어간 방 번호
        print("잡았다!요놈!")
        score = score +100
        break
    elif n > 3 :
        print(n, "번 방은 없습니다.")

    else:
        print("범인이 없습니다")
        score = score - 10

print("게임종료!")
print("점수:",score,"점")
