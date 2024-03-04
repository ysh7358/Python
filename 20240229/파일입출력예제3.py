file = open("name.txt", "w")
file2 = open("eng.txt", "w")

for i in range(1, 11) :
    
    name = input(str(i) + "번째 학생의 이름을 입력해 주세요 : ")
    score = input(str(i) + "번째 학생의 점수를 입력해 주세요 : ")

    file.write(str(i) + "번째 학생의 이름은 : " + name + "\n")
    file2.write(str(i) + "번째 학생의 점수는 : " + score + "\n")

file.close()
file2.close()
