file = open("email.txt", "r")
myId = input("아이디를 입력해주세요 : ")
idList = []

for i in file :
    idList.append((i.split("@"))[0])

if myId in idList :
    print("로그인 성공")
else :
    print("로그인 실패")

file.close()
