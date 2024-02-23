#정정일 선생님 문제

'''
정수 10개를 저장한 리스트 arr을 임의로 만듭니다. (0-99)
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고,
50보다 작은 홀수라면 2를 곱한 값을 각 원소에 다시 덮어씁니다.
그 결과인 정수 리스트 arr을 출력해 주세요.
'''
import random

arr = []
for i in range(10) :
    number = random.randrange(0,99)
    arr.append(number)
print(arr)

def f1(arr) :
    for j in range(10) :
        if (arr[j] % 2 == 0) and (arr[j] >= 50) :
            arr[j] = int((arr[j] / 2))
        elif (arr[j] % 2 == 1 ) and (arr[j] < 50) :
            arr[j] = (arr[j] * 2)
    return arr

print(f1(arr))
