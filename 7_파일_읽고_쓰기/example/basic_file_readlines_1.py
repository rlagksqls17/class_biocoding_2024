f = open("new_file.txt", 'r')
lines = f.readlines()

for line in lines:
    line = line.strip()
    print(line)

f.close()


