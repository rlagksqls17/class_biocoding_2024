def cost(city):
    dic = {'춘천':5000, '부산':30000, '대구':20000, '수원':10000}

    for tmp in dic.keys():
        if tmp == city:
            print(f"{tmp}까지의 금액은 {dic[tmp]}입니다.")

city = input('춘천(운임:5000원) / 부산(운임:30000원) / 대구(운임:20000원) / 수원(운임:10000원) \n중 한 곳을 입력하세요:')
cost(city)
