def rev_comp(dna):
    base_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev = dna[::-1]
    rev_dna = ''
    for base in rev:
        rev_dna += base_pairs[base]
    return rev_dna


def main():
    dna_file = open('dna.txt', 'r')
    dna = dna_file.readline().strip()
    print rev_comp(dna)


if __name__ == '__main__':
    main()