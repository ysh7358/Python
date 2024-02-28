def delete(deletejelly) :
    #상품 삭제
    while True :
        item = input("젤리 이름을 입력하세요 : ")

        if item in deletejelly :
            check = input("정말 삭제하시겠습니까? Y/N : ")
            if check.upper() == "Y" :
                del deletejelly[item]
                print(item + "젤리를 삭제하였습니다.")
                print(deletejelly)
                break
            elif check.upper() == "N" :
                print("삭제를 취소하였습니다.")
            else :
                print("잘못 입력하셨어요")
        else :
            print("해당 젤리가 없습니다")

