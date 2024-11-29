num_stamp = 0

def stamp():
    global num_stamp  # global 문 사용 시 함수 안에서 전역변수 수정 가능
    num_stamp = num_stamp + 1   
    print(num_stamp)

stamp()
