def Info_From_FASTQ(fastq):
    read_count = 0
    comment, sequence = [], []
    result_info = []

    for line in fastq.readlines():
        read_count += 1
        if read_count % 4 == 1:
            comment.append(line.strip())
        elif read_count % 4 == 2:
            sequence.append(line.strip())
    
    for i in range(len(comment)):
        result_info.append([comment[i], sequence[i]])

    return result_info


def FASTA_Write(info, output_path):
    f = open(output_path, 'w')
    for e in info:
        comment = e[0]
        sequence = e[1]
        f.write(f">{comment}\n")
        f.write(f"{sequence}\n")

    return 0


def main():
    input_path = "/home/bilab/khb/biocoding_genome_class_python/class/9_FASTA_FASTQ/ref_file/example.fq"
    output_path = "/home/bilab/khb/biocoding_genome_class_python/class/9_FASTA_FASTQ/train/example.fa"
    
    fastq = open(input_path, 'r')

    info = Info_From_FASTQ(fastq)

    FASTA_Write(info, output_path)

main()
