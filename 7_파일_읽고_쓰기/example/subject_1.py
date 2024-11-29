seqs = open("reference_seq.txt", 'r')
line_list = []

for line in seqs.readlines():
    line_list.append(line.replace("$", "").strip())

profile_list_A = [0, 0, 0, 0, 0, 0, 0, 0]
profile_list_C = [0, 0, 0, 0, 0, 0, 0, 0]
profile_list_G = [0, 0, 0, 0, 0, 0, 0, 0]
profile_list_T = [0, 0, 0, 0, 0, 0, 0, 0]

for line in line_list:
    count = 0

    for w in line:
        if w == "A":
            profile_list_A[count] += 1
        elif w == "C":
            profile_list_C[count] += 1
        elif w == "G":
            profile_list_G[count] += 1
        elif w == "T":
            profile_list_T[count] += 1
        count += 1

string = ""
for i in range(0, 8):
    A = profile_list_A[i]
    C = profile_list_C[i]
    G = profile_list_G[i]
    T = profile_list_T[i]
    target = [A, C, G, T]

    if max(target) == A:
        string += "A"
    elif max(target) == C:
        string += "C"
    elif max(target) == G:
        string += "G"
    elif max(target) == T:
        string += "T"

print(f"consensus sequence : {string}")
