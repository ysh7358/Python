#키가 130cm이상이거나 8세 이상 탑승가능, 아니면 탑승불가
height = int(input("키가 얼마인가요? "))
age = int(input("나이는 몇 살 인가요? "))
print("\n손님의 키는 " + str(height) + "cm, " + "나이는 " + str(age) + "세 입니다\n")

if (height>=130 or age>=8) :
    print("놀이기구에 탑승 가능합니다")

else :
    print("탑승불가")
