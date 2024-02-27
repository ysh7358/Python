#2024년 2월 27일 프로젝트 1안 - 게임 만들기

import random
import time

def generateNumber(): #4자리 랜덤 번호를 생성하는 함수
    numberList = '0123456789' #0~9까지의 숫자
    secretNumber = '' #비밀번호를 담을 변수 선언
    for i in range(4): #4자리를 추출해야 하니 4번 반복한다
        number = random.choice(numberList) #리스트에서 랜덤으로 번호 추출
        secretNumber = secretNumber + number #문자열이니 계속 뒷자리에 붙음
        numberList = numberList.replace(number, '')  #뽑은 번호는 지워서 중복을 방지한다.
    return secretNumber #생성된 비밀번호를 리턴

def check(secretNumber, myNumber): #비밀번호와 내 번호를 파라미터로 받아와서 일치하는지 체크하는 함수
    strike = 0 #스트라이크 초기화값
    ball = 0 #볼 초기화값
    for i in range(4): #0번~3번의 인덱스 값을 비교해야 하니 4번 반복
        if myNumber[i] == secretNumber[i] : #번호, 자리 모두 일치 시 스트라이크
            strike = strike + 1
        elif myNumber[i] in secretNumber : #번호만 일치 시 볼
            ball = ball + 1
    return strike, ball #스트라이크와 볼 값을 리턴

def main(): #메인, 게임 실행부 함수
    secretNumber = generateNumber() #생성한 비밀번호를 비밀번호로 설정
    count = 0 #시도한 횟수 초기화
    start = time.time() #게임을 시작했을 때의 시간을 start 변수에 담음
    timeLimit = 300  # 5분 = 300초

    print(secretNumber)
    print("몰래 집으로 잠입을 시도합니다. 제한 시간은 5분입니다.")
    print("5분이 지나면 무슨 일이 일어날지 상상도 하기 싫습니다.")
    print("비밀번호는 0부터 9까지의 서로 다른 4자리 숫자입니다.")
    print("비밀번호의 숫자와 위치를 맞추면 스트라이크")
    print("숫자만 맞추면 볼입니다.")

    while True:
        if time.time() - start > timeLimit: #현재시각 - 시작시간 > 5분시 시간 초과
            print("시간이 초과되었습니다. 삐----")
            print("정답은 ", secretNumber, "입니다.")
            print("각목을 들고 나온 아버지와 눈이 마주쳤습니다.")
            print("GAME OVER")
            break #게임 오버 시 프로그램 종료

        myNumber = input("4자리 숫자를 입력하세요: ") #추측한 비밀번호 입력
        
        if len(myNumber) != 4 : #4자리를 입력하지 않을 시 재입력 
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            continue #올바르게 입력하지 않을 시, 아래 코드는 실행하지 않음

        #0123456789를 제외한 다른 문자를 사용할 시 잘못 입력했습니다를 출력
        checkValue = True
        
        for i in range(4) :
            if myNumber[i] not in '0123456789':
                checkValue = False
                break

        if not checkValue:
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            continue
        
        #시도 횟수 증가
        count = count + 1
        
        #비밀번호와 내 번호를 비교해서 나온 리턴값을 strike, ball에 대입
        strike, ball = check(secretNumber, myNumber)
        

        if strike == 4 : #정답
            print(count, "번 만에 비밀번호를 맞추셨습니다. 현관문이 열립니다")
            print("발소리를 죽인 채, 살금살금 방으로 들어가서 방문을 닫습니다.")
            print("The End")
            break
        else: #N스트라이크 N볼을 출력
            print(strike, "스트라이크", ball, "볼입니다.")
            
main() #메인 게임 호출
