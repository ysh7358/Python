print("*" * 24)
print("무인 젤리 가게입니다.")
print("*" * 24)

price = int(input("구매하실 젤리의 가격을 입력해주세요 : "))
count = int(input("구매하실 젤리의 갯수를 입력해주세요 : "))

totalPrice = price * count

print("총 지불 가격은 : " , totalPrice , "원 입니다.")

money = int(input("지불하실 금액을 입력해주세요 : "))
change = money - totalPrice
moneyCount1 = change // 5000
moneyCount2 = (change%5000) // 1000

print("고객님께서 지불하신 금액은 " , money, "원 입니다")
print("거스름돈은 " , change, "원 입니다.")
print("오천원 짜리가 " , moneyCount1, "장 반환됩니다.")
print("천원 짜리가 " , moneyCount2, "장 반환됩니다.")
print("나머지 금액은" , change%1000, "원 입니다.")
