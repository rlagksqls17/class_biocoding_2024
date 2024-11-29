f = open("new_file.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()


