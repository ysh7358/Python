'''
#문제) 축구선수 10명의 키를 입력받아서 큰 순서대로 출력
player = []
for i in range(10) :    
    height = int(input(str(i+1) + "번째 축구 선수의 키를 입력해주세요"))
    player.append(height)

player.sort()
print(player)

'''
#스트림스 단, 조커는 0으로 출력한다.
import random
streams = []
number = []
#값이 0으로 초기화된 크기가 20인 리스트 선언
player = [str(p+1)+"번째" for p in range(20)] 
for i in range(0, 31) :
        if 11<=i<=19 :#11~19는 두 개씩 들어있음
            streams.append(i)
            streams.append(i)
        else :
            streams.append(i)
#번호 추출 및 자리 선정   
for j in range(20) :
    num = streams[random.randrange(0,39-j)]
    print("추출한 번호는 " + str(num))
    playerNum = int(input("몇 번째에 추출한 번호를 넣으시겠습니까? : "))

#이미 넣은 자리에 넣은 경우
    while(("번째" in (str(player[playerNum-1]))) == False) :
        print("중복된 자리입니다. 다른 자리를 선택해 주세요")
        playerNum = int(input("몇 번째에 추출한 번호를 넣으시겠습니까? : "))
    
    if num == 0 :
        streams.remove(num)
        player[playerNum - 1] = "★"
        number.append("★")  
        print(player)
    else :
        player[playerNum - 1] = num
        number.append(num)
        streams.remove(num)
        print(player)
    
print("남은 번호의 모음은 : ", streams)
print("추출한 번호의 모음은 : ", number)

#점수 계산, 현재 점수 버그 있음 수정해야 함.
'''
print("점수 계산중...")
score = 0
increment = [0,1,3,5,7,9,11,15,20,25,30,35,40,50,60,70,85,100,150,300]
#몇번째 연속인지를 count에 기록함
count = 0
for i in range(1, 20) :
    #pass
    # 순차적인 값인가?
    # 이전 카드 값 == 현재 카드값 + 1
    # 연속 증가 횟수에 따라 증가값 increment 결정
    
        if player[i-1] != "★" and player[i] != "★" :
                
            if player[i-1] <= player[i] or player[i] == 0:
                count = count + 1
        else :
                playerPointNumber = player[i-count:i]
                playerPointNumber.append("★")
                count = count + 1

        if count >=2 :
                if player[i-1] == "★" or player[i] == "★" :
                        print("연속된 수:", playerPointNumber)
                        print("득점:", increment[count-1])
                        score = score + increment[count-1]
                        count = 0
                else :
                        print("연속된 수:", player[i-count:i])
                        print("득점:", increment[count-1])
                        score = score + increment[count-1]
                        count = 0

print(" 당신의 점수는?", score , "점 입니다.")
'''
