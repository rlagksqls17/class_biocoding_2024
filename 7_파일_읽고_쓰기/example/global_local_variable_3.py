num_stamp1 = 0


def stamp(argument):
    num_stamp2 = argument + 1
    print(f"num_stamp2 : {num_stamp2}")
    return num_stamp2


num_stamp1 = stamp(num_stamp1)
print(f"num_stamp1 : {num_stamp1}")
num_stamp1 = stamp(num_stamp1)
print(f"num_stamp1 : {num_stamp1}")
