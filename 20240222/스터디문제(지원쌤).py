count = 0

l = ['과자1', '과자2', '과자3', '과자4', '과자5', '과자6', '과자7', '과자8', '과자9', '과자10']
price = [700, 500, 1000, 600, 700, 500, 800, 1200, 1000, 700]

print(l)
item = input("구매하실 과자명을 입력해 주세요 : ")

if item in l :
    print("과자가 있어요")
    print(item, "과자의 비용은", price[l.index(item)], "입니다\n")
    count = int(input("몇 개 구매하시겠습니까? : "))
    print("총 가격은 : " + str(price[l.index(item)] * count) + "원 입니다")
else :
    print("해당 과자는 없습니다")
