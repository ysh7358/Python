'''
#10명의 농구선수의 키를 입력받는 리스트
plist = []
for i in range(10) :
    height = input(str(i + 1)+"번째 농구 선수의 키를 입력해주세요 : ")
    plist.append(height + "cm")
print(plist)
'''
#스트림스 게임. 단 조커는 0으로 두고 코드를 작성한다.
streams = []
for i in range(0, 31) :
    if 11<=i<=19 :
        streams.append(i)
        streams.append(i)
    else :
        streams.append(i)

print(streams)
