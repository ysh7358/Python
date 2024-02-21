'''
a = [1,2,3,4,5,6,7,8,9,10] #리스트 선언

print(a) # 1~10
print(a[:]) #1~10
print(a[0]) #1
print(a[0:3]) #123
print(a[:3]) #123

a = "청년취업사관학교"

print(a)
print("청년" in a) #true
print("새싹" in a) #false
print("청학" in a) #false

jelly = ['하리보', '왕꿈틀이', '망고', '지구', '마이구미', '웰치스', '박카스', '비타500', '후루팁스', '트롤리']

name = input("젤리명을 입력해 주세요 : ")

if (name in jelly) : #jelly 리스트 안에 name이 있다면
    count = int(input("저희 가게에는 해당 젤리가 있습니다. 개당 가격은 700원 입니다.\n구매하실 수량을 입력해 주세요 : "))
    print("지불하실 금액은 " + str(count * 700) + "원입니다")

else :
    print("저희 가게에는 해당 젤리가 없습니다")

jelly = ['하리보', '왕꿈틀이', '망고', '지구', '마이구미', '웰치스', '박카스', '비타500', '후루팁스', '트롤리']

#del jelly[2]
print(jelly)
while(True) :
    e = input("제거할 젤리를 적어 주세요 : ")
    if e in jelly :
        jelly.remove(e) #입력한 젤리를 리스트에서 제거
    print(jelly)
#item = jelly.pop() #젤리 리스트의 마지막 요소를 제거 후 item에 저장
#print(item)

while(True) :
    e = input("인덱스를 확인할 젤리를 적어 주세요 : ")
    if e in jelly : #젤리 안에 e가 있다면
        print(jelly.index(e)) #e의 인덱스를 출력해라 
'''
