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


def find_dH(kmer, seq):
    min_distance = sys.maxint
    for s in seq:
        dH = sum(c1 != c2 for c1, c2 in itertools.izip(kmer, s))
        if dH < min_distance:
            min_distance = dH
    return min_distance 


def get_min_hamming_distance(possible_kmers, kmer_subs):
    min_distance = sys.maxint
    best_kmer = ''
    for kmer in possible_kmers:
        total_distance = 0
        for sub in kmer_subs:
            total_distance += find_dH(kmer, sub)
        if total_distance < min_distance:
            min_distance = total_distance
            best_kmer = kmer
    return best_kmer


def main():
    #k = int(sys.argv[1])
    f = open('input.txt', 'r')
    k = int(f.readline().strip('\n'))
    motifs = get_motif_collection(f, [])
    kmer_subs = find_kmers_collection(motifs, k, [])
    possible_kmers = [''.join(p) for p in itertools.product('ATCG', repeat=k)]

    best_kmer = get_min_hamming_distance(possible_kmers, kmer_subs)
    print best_kmer


if __name__ == '__main__':
    main()
