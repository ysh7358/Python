file = open("kor1.txt", "r")
'''
#방법1
sum = 0

newScoreList = []
scoreList = file.readlines()

for i in range(10) :
    newScoreList.append(scoreList[i].split("\n"))
for j in range(10) :
        sum = sum + int(newScoreList[j][0])   
print(sum)
#방법2
for i in range(10) :
    line = int(file.readline().rstrip())
    sum = sum + line
print(sum)
'''
#방법3
scoreList = []
for i in range(10) :
    scoreList.append(int(file.readline().rstrip()))
print(sum(scoreList))

file.close()
