# while 문을 사용해 1부터 1000까지의 자연수에서 3의 배수만 뽑아서 합을 구하라.
number = 0
total_number = 0

while(number != 1000):
    number += 1
    if number % 3 == 0:
        total_number += number

print(total_number)
