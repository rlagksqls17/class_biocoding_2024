dan = int(input("단 수를 입력하세요. : "))
if dan < 1 or dan > 9:
    print("1 ~ 9범위의 숫자만 입력하세요.")
else:
    for i in range(1, 10):
        print(f"{dan} * {i} = {dan * i}")
