RNA_1 = "AUGGGGATTAAUGCAUAGCGUAG"
RNA_2 = "AUGGCGTTTAAAUCGCCCUAG"
RNA_3 = "AUGTTAAAAAAUGGGUAA"

# 4-1
print(f"RNA-1 : {RNA_1[-3:]}\nRNA-2 : {RNA_2[-3:]}\nRNA-3 : {RNA_3[-3:]}")

# 4-2
print("----------------------------------")
print(f"RNA-1: {'TTAAA' in RNA_1}\nRNA-2: {'TTAAA' in RNA_2}\nRNA-3: {'TTAAA' in RNA_3}")

# 4-3
print("----------------------------------")
print(f"RNA-1: {len(RNA_1)}\nRNA-2: {len(RNA_2)}\nRNA-3: {len(RNA_3)}")
print(f"mean RNA length : {(len(RNA_1) + len(RNA_2) + len(RNA_3)) / 3}")
