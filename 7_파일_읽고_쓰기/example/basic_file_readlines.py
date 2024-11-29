f = open("new_file.txt", 'r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)

f.close()


