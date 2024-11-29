codon_table = {'UUU':'Phe', 'UUC':'Phe','UUA':'Leu','UUG':'Leu','UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser','UAU':'Tyr','UAC':'Tyr','UAA':'Stop','UAG':'Stop','UGU':'Cys','UGC':'Cys','UGA':'Stop','UGG':'Trp','CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu','CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro','CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln','CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg','AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met', 'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr','AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys','AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg','GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val','GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala','GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu','GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}

RNA = str(input("번역할 RNA sequence를 입력하세요 : "))
protein = ""

if len(RNA) % 3 == 0:
    for index in range(len(RNA) // 3):
        start_index = index * 3
        end_index = (index + 1) * 3
        protein += codon_table[RNA[start_index:end_index]]
    print(f"아미노산 서열 : {protein}")
else:
    print("error!")
