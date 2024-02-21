count = 0

jelly = ['하리보', '왕꿈틀이', '망고', '지구', '마이구미', '웰치스', '박카스', '비타500', '후루팁스', '트롤리']
price = [700, 500, 1000, 600, 700, 500, 800, 1200, 1000, 700]

print(jelly)
item = input("구매하실 젤리명을 입력해 주세요 : ")

if item in jelly :
    print(item, "제품의 비용은", price[jelly.index(item)], "입니다\n")
    count = int(input("몇 개 구매하시겠습니까? : "))
    print("총 가격은 : " + str(price[jelly.index(item)] * count) + "원 입니다")
else :
    print("저희 편의점에는 해당 제품이 없어요 ㅠ")
