'''
phone_book = {'홍길동' : '010:1234-5678',
              '강감찬' : '010-4235-1358'}

print(phone_book['강감찬'])
print(phone_book)
'''
#딕셔너리 선언
phone_book = {"홍길동" : "010-1234-5678",
              "강감찬" : "010-4235-1234"}
#딕셔너리 요소 추가
phone_book["사람1"] = "010-1234-1234"
phone_book["사람2"] = "010-5678-5678"

#딕셔너리 키에 맞는 값 불러오기
print(phone_book["강감찬"])
print(phone_book["사람2"])
print()
print(phone_book)
print()
'''
#딕셔너리 값 모음
print(phone_book.values())
#딕셔너리 키 모음
print(phone_book.keys())

#원하는 요소 삭제
print(phone_book.pop("강감찬"))
del phone_book["홍길동"]

print(phone_book)

#전체 요소 삭제
phone_book.clear()
print(phone_book)

#요소 정렬
for key in sorted(phone_book.keys()) :
    print(key, phone_book[key])
#print(sorted(phone_book))

for i in sorted(phone_book.keys()) :
    print(i, phone_book[i])

#for i in sorted(phone_book.values()) :
  #  print(i)
'''
checkValue = False

for i in phone_book :
    if "강감찬" in i :
        checkValue = True
    else :
        ''

if checkValue == True :
    print("존재합니다")
elif checkValue == False :
    print("존재하지 않습니다")
