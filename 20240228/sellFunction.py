def sell(selljelly) :
    #상품 판매
    while True :
        name = input("젤리 이름을 입력하세요 : ")
        try :        
            if name in selljelly :
                print(name + " 젤리의 가격은 " + str(selljelly[name]) + "원 입니다")
                count = int(input("구매하실 수량을 입력하세요 : "))
                print("지불하실 가격은 " + str(selljelly[name] * count) + "원 입니다")
                break
            else :
                print("해당 젤리가 없습니다")

        except :
            print("올바른 수량을 입력하세요")
