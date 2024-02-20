import random

num = [1 , 2 , 3 , 4 , 5 , 6]
c = random.choice(num)
print(c)

#sign = ['Red', 'Yellow', 'Green']
#randomSign = random.choice(sign)
#print(randomSign)
ranNum = random.randrange(3)

if ranNum == 0 :
    print("red")

elif ranNum == 1 :
    print("yellow")

else :
    print("green")
#ranSign = sign[ranNum]
#print(ranSign)
