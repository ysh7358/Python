from sellFunction import sell
from deleteFunction import delete
from addFunction import add

def menu(jelly) :
    while True :
        try :
            number = int(input("번호를 입력해 주세요(1.판매  2.추가  3.삭제) : "))
            if number == 1 :
                sell(jelly)
            elif number == 2 :
                add(jelly)
            elif number == 3 :
                delete(jelly)
            else :
                print("1,2,3 중 하나의 숫자를 입력해 주세요.")
        except :
            print("1,2,3 중 하나의 숫자를 입력해 주세요.")

jelly = {'하리보' : 2000, '왕꿈틀이' : 1500, '망고' : 1200, '지구' : 300, '마이구미' : 1300,
         '웰치스' : 1700, '박카스' : 1000, '비타500' : 700, '후루팁스' : 600, '트롤리' : 1800}

menu(jelly)
