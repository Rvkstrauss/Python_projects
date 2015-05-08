#use the algorithm for cyclopeptide spectrums in Lecture three, an treat the for word as an if condition,
# meaning what do you want the program to consider about the peptide when it is circularizing it
import sys


def circularize(line):  #HINT: see cyclopeptide_sequencing code, or vice versa, they operate the same way.
    for i in range(0,len(line)):
        sum = 0
        for j in range(i,len(line)):
            sum += line[j]
            subpeptides.append(sum)
            if i >= 1 and j == len(line) - 1:
                for k in range(0, i-1):
                    sum += line[k]
                    subpeptides.append(sum)
        print (' '.join(map(str, sorted(subpeptides))))


def main():
    print('enter peptide sequence')
    peptide = input()
    peptide_dict = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                    'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    line = []
    for char in peptide:
        line.append(peptide_dict.get(char))
    subpeptides = [0]
    circularize(line)

if __name__ == '__main__':
  main()

