'''
#상품 판매
jelly = {'하리보' : 2000, '왕꿈틀이' : 1500, '망고' : 1200, '지구' : 300, '마이구미' : 1300,
         '웰치스' : 1700, '박카스' : 1000, '비타500' : 700, '후루팁스' : 600, '트롤리' : 1800}
while True :
    name = input("젤리 이름을 입력하세요 : ")
    
    try :        
        if name in jelly :
            print(name + " 젤리의 가격은 " + str(jelly[name]) + "원 입니다")
            count = int(input("구매하실 수량을 입력하세요 : "))
            print("지불하실 가격은 " + str(jelly[name] * count) + "원 입니다")
            break
        else :
            print("해당 젤리가 없습니다")

    except :
        print("올바른 수량을 입력하세요")

#상품 삭제
jelly = {'하리보' : 2000, '왕꿈틀이' : 1500, '망고' : 1200, '지구' : 300, '마이구미' : 1300,
         '웰치스' : 1700, '박카스' : 1000, '비타500' : 700, '후루팁스' : 600, '트롤리' : 1800}

while True :
    item = input("젤리 이름을 입력하세요 : ")

    if item in jelly :
        check = input("정말 삭제하시겠습니까? Y/N")
        if check == "Y" :
            del jelly[item]
            print(item + "젤리를 삭제하였습니다.")
            print(jelly)
        elif check == "N" :
            print("삭제를 취소하였습니다.")
        else :
            print("잘못 입력하셨어요")
    else :
        print("해당 젤리가 없습니다")
'''

#상품 추가
jelly = {'하리보' : 2000, '왕꿈틀이' : 1500, '망고' : 1200, '지구' : 300, '마이구미' : 1300,
         '웰치스' : 1700, '박카스' : 1000, '비타500' : 700, '후루팁스' : 600, '트롤리' : 1800}

while True :
    try :
        item = input("추가하실 젤리 이름을 입력하세요 : ")
        if item in jelly :
            print("해당 젤리가 있습니다")
            break
        else :
            price = int(input("추가하실 젤리의 가격을 입력하세요 : "))
            jelly[item] = price
            print(jelly)

    except :
        print("젤리의 가격을 잘못 입력하셨습니다")










