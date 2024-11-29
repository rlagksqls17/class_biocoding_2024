def Parsing_Fasta(fasta):
    comment = ""
    sequence = ""
    for line in fasta.readlines():
        if ">" in line:
            comment = line
        else:
            sequence += line.strip()

    return [comment, sequence]


def Read_Fasta(path):
    fasta = open(path, 'r')
    return fasta


def main():
    path = "/home/bilab/khb/biocoding_genome_class_python/class/9_FASTA_FASTQ/TDP1_datasets/ncbi_dataset/data/gene.fna"
    fasta = Read_Fasta(path)
    information = Parsing_Fasta(fasta)
    print(f"comment : {information[0]}")
    print(f"sequence head (80) : {information[1][:80]}")

main()
