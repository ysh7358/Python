phone_book = {"사람1" : "010-1234-1234"}
phone_book["여상혁"] = "010-8243-7358"

name = input("이름을 입력해 주세요 : ")

if name in phone_book :
    print("전화번호는 : " + phone_book[name])

else :
    print("비회원이에요")
