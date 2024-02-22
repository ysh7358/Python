'''5명의 학생
국어, 영어, 수학 점수 입력받아서
출력하기

koreanScore = []
englishScore = []
mathScore = []

for i in range(5) :
    koreanScore.append(input(str(i+1) + "번째 학생의 국어 점수를 입력해 주세요 : "))
    englishScore.append(input(str(i+1) + "번째 학생의 영어 점수를 입력해 주세요 : "))
    mathScore.append(input(str(i+1) + "번째 학생의 수학 점수를 입력해 주세요 : "))
print(("*" * 11) + "성적표" + ("*" * 11))
print("번호\t국어\t영어\t수학)
for j in range(5) :
    print(str(j+1) + '\t' ,end = '')
    print(str(koreanScore[j]) + '\t',end = '')
    print(str(englishScore[j]) + '\t',end = '')
    print(str(mathScore[j]) + '\t')
print("*" * 28)
'''
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
