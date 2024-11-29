def Complement(DNA_seq):
    DNA_com = {'A': 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    com_seq = ""
    for seq in DNA_seq:
        com_seq += DNA_com[seq]

    return com_seq


def Info_From_FASTQ(path): # 지난 실습에서 짠 코드를 복사한 것이다.
    f = open(path, 'r')
    read_count = 0
    comment, sequence = [], []
    result_info = []

    for line in f.readlines():
        read_count += 1
        if read_count % 4 == 1:
            comment.append(line.strip())
        elif read_count % 4 == 2:
            sequence.append(line.strip())

    for i in range(len(comment)):
        result_info.append([comment[i], sequence[i]])

    return result_info


def Paired_to_Single(fq_1_path, fq_2_path, output_path):
    fq_1_info = Info_From_FASTQ(fq_1_path)
    fq_2_info = Info_From_FASTQ(fq_2_path)
    
    #fq_1과 fq_2의 length는 같으므로 fq_1 length만 가져와도 된다.
    for i in range(len(fq_1_info)): 
        comment = fq_1_info[i][0]
        fq_1_sequence = fq_1_info[i][1]
        preprocessed_fq_2_sequence = Complement("".join(list(fq_2_info[i][1])[::-1]))
    single_seq = fq_1_sequence + preprocessed_fq_2_sequence
    return [comment, single_seq]


def Write_Single_Fastq(single_info, output_path):
    f = open(output_path, 'w')
    comment = single_info[0]
    single_seq = single_info[1]
    f.write(comment+"\n")
    f.write(single_seq+"\n")
    f.write("+\n")
    f.write("FFFFFFFFFFFFFFFFFF")
    f.close()
    
    return 0


def main():
    fq_1_path = "/root/khb/biocoding_genome_class_python/class/9_FASTA_FASTQ/ref_file/paired_end_1.fq"
    fq_2_path = "/root/khb/biocoding_genome_class_python/class/9_FASTA_FASTQ/ref_file/paired_end_2.fq"
    output_path = "/root/khb/biocoding_genome_class_python/class/9_FASTA_FASTQ/ref_file/single_end.fq"
    single_info = Paired_to_Single(fq_1_path, fq_2_path, output_path)
    Write_Single_Fastq(single_info, output_path)
    
    print("single-end 파일 작성 완료!")

main()
