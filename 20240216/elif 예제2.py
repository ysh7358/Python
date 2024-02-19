#성별 코드 입력받아서 1/3 남자 2/4 여자 나머지 해당없음
a = input("주민등록번호를 입력해주세요\n 예시 : 960209-1111111 ")
code = a[7]
if (code == "1") or (code == "3") :
    print("남자 입니다.")
elif (code == "2" ) or (code == "4") :
    print("여자 입니다.")
else :
    print("해당없음.")
