file = open("id.txt", "r")
myId = input("아이디를 입력해주세요 : ")
'''
#첫 번째 방법

check = False
for i in file :
    id = i.rstrip()
    if myId == id :
        check = True
        break
    else :
        check = False

if check == True :
    print("로그인 성공")
else :
    print("로그인 실패")
'''
#두 번째 방법
idList = []
for i in file :
    id = i.rstrip()
    idList.append(id)
    
if myId in idList :
    print("로그인 성공")
else :
    print("로그인 실패")
    
file.close()
