#20240223 창욱쌤 문제
'''
문) 영수증 출력
1. 마트 상품, 가격 리스트 8개 만들기
2. 편의점에 있는 물건을 3가지 고를때까지 반복
3. 제품명, 가격, 수량, 총 합 나오도록 출력

추가문제) 환불 영수증 출력
1. 구매한 물건 중 마음에 들지 않는 물건 입력하여 환불
2. 환불한 금액 출력
3. 환불 영수증 출력
'''
goods = ["연필", "과자", "마우스", "음료수", "껌", "책", "치킨", "피자"]
price = [100, 200, 300, 400, 500, 600, 700, 800]
myitem = []
itemCount = []
sum = 0
while(len(myitem) != 3) :
    print(goods)
    select = input("물건을 골라주세요 : ")
    if select in goods :
        myitem.append(select)
        count = int(input("몇 개 구매하시겠습니까? : "))
        itemCount.append(count)
    else :
        print("잘못 고르셨습니다")

for i in range(3) :
    name = myitem[i]
    goodsprice = price[goods.index(myitem[i])]
    goodsCount = itemCount[i]
    print("제품명은", name, ", 가격은", goodsprice, "원, 총 가격은", goodsCount*goodsprice, "원 입니다")
    sum = sum + goodsCount*goodsprice
print("지불하실 총 금액은 : ", sum, "원 입니다")
refund = input("마음에 들지 않는 물건을 입력해 주세요 : ")
if refund in myitem :
    print(refund, "물품의 구매 갯수는", itemCount[goods.index(refund)], "이며, 환불 금액은",price[goods.index(refund)] * itemCount[goods.index(refund)], "원 입니다")
    
