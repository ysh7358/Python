print("소금물의 농도를 구하는 프로그램")
salt = int(input("소금의 양을 정해주세요 : "))
water = int(input("물의 양을 정해주세요 : "))
saltwater = salt + water
density = (salt / saltwater) * 100
print("소금물의 농도는 : " , density , "%입니다")
