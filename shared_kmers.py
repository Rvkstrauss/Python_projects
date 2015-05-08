from collections import defaultdict
import reverse_complement as rc


def parse_data():
    data = open('input.txt', 'r')
    k = int(data.readline().strip())
    str1 = data.readline().strip()
    str2 = data.readline().strip()
    data.close()
    return k, str1, str2


def find_kmer_set(k, str1):
    kmers = defaultdict(list)
    for i in range(0, len(str1) - k + 1):
        kmers[str1[i:i + k]].append(i)
    return kmers

def main():
    f = open('output.txt', 'w')
    k, str1, str2 = parse_data()
    kmers_str1 = find_kmer_set(k, str1)

    for j in range(0, len(str2) - k + 1):
        for i in kmers_str1[str2[j:j+k]]:
            f.write('(' + str(i) + ', ' + str(j) + ')\n')
        for i in kmers_str1[rc.rev_comp(str2[j:j+k])]:
            f.write('(' + str(i) + ', ' + str(j) + ')\n')

    f.close()

if __name__ == '__main__':
    main()