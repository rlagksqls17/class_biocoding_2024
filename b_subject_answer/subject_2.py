coffee = 10
value = 300

while(1):
    money = int(input("돈을 넣어주세요:"))
    if money > value:
        print(f"거스름돈 {money - value}를 주고 커피를 줍니다.")
        coffee -= 1
    elif money == value:
        print("커피를 줍니다.")
        coffee -= 1
    else: print("돈을 다시 돌려주고 커피를 주지 않습니다.")

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    else:
        print(f"남은 커피의 양은 {coffee}개입니다.")
