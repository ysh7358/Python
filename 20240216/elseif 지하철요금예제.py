age = float(input("나이를 입력해주세요 : "))
#음수나 소수를 입력했을 경우
if(age<0 or (float(age) - int(age) != 0)) :
    print("잘못 입력하셨습니다")
    
else :
#65세 이상뿐 아니라 6세 미만도 무료
    if (age >= 65 or age < 6) :
        #print("요금은 무료입니다.")
         b = "무료"
    elif(age >=19) :
        #print("요금은 1250원입니다.")
        b = 1250
    elif(age >=13) :
        #print("요금은 850원입니다.")
        b = 850
    elif(age >=6) :
        #print("요금은 400원입니다.")
        b = 400
    else :
        b = "무료"
        #print("해당 없음")

print("지하철 요금은" , b , "원 입니다.")
