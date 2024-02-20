x1 = int(input("첫 번째 x좌표값을 입력해 주세요. (단위 : cm) "))
x2 = int(input("두 번째 x좌표값을 입력해 주세요. (단위 : cm) "))
y1 = int(input("첫 번째 y좌표값을 입력해 주세요. (단위 : cm) "))
y2 = int(input("첫 번째 y좌표값을 입력해 주세요. (단위 : cm) "))

distance = ((y2-y1)**2 + (x2-x1)**2)**0.5
print("두 좌표 사이의 거리는" + str(distance) +"cm입니다.")
