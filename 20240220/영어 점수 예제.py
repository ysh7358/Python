minscore = 999 #꼴등의 점수를 저장하는 변수
maxscore = 0 #1등의 점수를 저장하는 변수
totalscore = 0 #총 점수를 저장하는 변수

for i in range(10) : #10명의 점수를 입력 받아야 하니 10번 반복한다
    score = int(input(str(i+1) + "번째 학생의 영어 성적을 입력해주세요 : "))
    
    if minscore > score : #minscore 보다 score가 작은 경우 minscore에 score 대입
        minscore = score
        
    if maxscore < score : #maxscore 보다 score가 큰 경우 maxscore에 score 대입
        maxscore = score

    totalscore = totalscore + score # 총계 누적
    avgscore = totalscore / (i+1) #총점 / 사람 수 = 평균

print("영어 성적의 총합은 : " + str(totalscore) + "점입니다.")
print("영어 성적의 평균은 : " + str(avgscore) + "점입니다.")
print("1등의 영어 성적은 : " + str(maxscore) + "점입니다.")
print("꼴등의 영어 성적은 : " + str(minscore) + "점입니다.")

