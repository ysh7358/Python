'''
가나다 순으로 정렬

heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes.sort()
print(heroes)

#기본 : 오름차순으로 정렬
#reverse : 내림차순으로 정렬

heroes.sort(reverse = True)
print(heroes)

newHeroes = sorted(heroes)
print(newHeroes)

a = [10, 5, 8, 2, 7, 20]
print(a)
a.sort()
print(a)
a.sort(reverse = True)
print(a)

#문자일 경우 앞자리를 우선 비교한다
b = ["1", "2", "10", "20"]
b.sort(reverse = True)
print(b)

#리버스 없이 내림차순으로 정렬하는 방법
a = [10, 5, 8, 2, 7, 20]
a.sort()
print(a)
a = a[: : -1]
print(a)

#리버스 없이 내림차순으로 정렬하는 방법2
a = [10, 5, 8, 2, 7, 20]
a.sort()
for i in range(4, -1, -1) :
    print(a[i], end= ', ')

#원본 리스트를 남기고 싶을 때는 sorted()를 사용
a = [10, 5, 8, 2, 7]
print(a) #원본 리스트
print(sorted(a)) #정렬된 새로운 리스트
print(a)

#sort 원본에 영향을 미침
a = [10, 5, 8, 2, 7]
print(a) #10,5,8,2,7
a.sort()
b = a
print(a) #2,5,7,8,10
print(b) #2,5,7,8,10
'''
#sorted 원본에 영향을 미치지 않음
a = [10, 5, 8, 2, 7]
print(a)
b = sorted(a, reverse = True)
print(a) #10,5,8,2,7
print(b) #10,8,7,5,2

