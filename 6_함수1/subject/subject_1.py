DNA_to_RNA_nuc = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}
DNA = str(input("DNA sequence : "))
RNA = ""

if len(DNA) > 3:
    for DNA_nuc in DNA: 
        RNA += DNA_to_RNA_nuc[DNA_nuc]
    print(f"RNA sequence : {RNA}")
else:
    print("error!")

