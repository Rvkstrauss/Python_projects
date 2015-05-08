import sys
import itertools

def get_motif_collection(f, motifs):
    for line in f:
        motifs.append(line.strip('\n'))
    f.close()
    return motifs

def find_kmers(motif, k, kmers):
    for i in range(0, len(motif) - k + 1):
        kmer = motif[i:i + k]
        if kmer not in kmers:
            kmers.append(kmer)
    return kmers

def find_kmers_collection(motifs, k, all_kmers):
    for motif in motifs:
        kmers = find_kmers(motif, k, [])
        all_kmers.append(kmers)
    return all_kmers

def find_match_in_list(kmer_list, kmer, d):
    i = 0
    no_match = True
    count = 0
    while i < len(kmer_list) and no_match:
        diff = sum(c1 != c2 for c1, c2 in itertools.izip(kmer, kmer_list[i]))
        if diff <= d:
            no_match = False
            count = 1
        i += 1
    return count

def main():
    #k = int(sys.argv[1])
    f = open('input.txt', 'r')
    #d = int(sys.argv[2])
    k = int(f.readline().strip('\n'))
    d = int(f.readline().strip('\n'))
    o = open('output.txt', 'w')

    motifs = get_motif_collection(f, [])
    all_kmers = find_kmers_collection(motifs, k, [])
    kmers = [''.join(p) for p in itertools.product('ATCG', repeat=k)]

    for kmer in kmers:
        match_count = 0
        for kmer_list in all_kmers:
            match_count += find_match_in_list(kmer_list, kmer, d)
        if match_count == len(motifs):
            o.write(kmer + '\n')
    o.close()

if __name__ == '__main__':
    main()
