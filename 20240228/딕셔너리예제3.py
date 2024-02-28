items = {"커피":7, "펜":3, "종이컵":10, "우유":5, "콜라":4, "라면":11}
print("판매 전 재고", items)

while True :
    sell = input("판매한 물건을 입력하세요 : ")

    if sell in items:
        items[sell] = items[sell] - 1
        if items[sell] == 0 :
            print("재고가 모두 소진되었습니다. 해당 물건을 제거합니다.")
            del items[sell]
    else :
        print("판매 제품이 아닙니다")

    print("판매 후 재고", items)
