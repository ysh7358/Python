#상품 추가
def add(addjelly) :
    while True :
        try :
            item = input("추가하실 젤리 이름을 입력하세요 : ")
            if item in addjelly :
                print("해당 젤리가 있습니다")
            else :
                price = int(input("추가하실 젤리의 가격을 입력하세요 : "))
                addjelly[item] = price
                print(addjelly)
                break

        except :
            print("젤리의 가격을 잘못 입력하셨습니다")

