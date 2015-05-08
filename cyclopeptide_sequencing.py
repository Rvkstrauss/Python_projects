

import sys
import collections

def circularize(line):
    subpeptides = [0]
    for i in range(0,len(line)):
        sum = 0
        for j in range(i,len(line)):
            sum += line[j]
            subpeptides.append(sum)
            if i >= 1 and j == len(line) - 1:
                for k in range(0, i-1):
                    sum += line[k]
                    subpeptides.append(sum)
    return sorted(subpeptides)

def get_starter_peptides(mass_table, exp_spec):
    singles = []
    for num in mass_table:
       if num in exp_spec:
           singles.append(str(num))
    return singles

def append_peptides(peptides, start_peptides):
    temp = []
    for p in peptides:
        for peptide in start_peptides:
            temp.append(p + '-' + peptide)
    return temp

def get_linear_spec(line):
    subpeptides = [0]
    for i in range(0,len(line)):
        sum = 0
        for j in range(i,len(line)):
            sum += line[j]
            subpeptides.append(sum)
    return sorted(subpeptides)

def is_consistent(spec, exp_spec):
    spec_counts = collections.Counter(spec)
    exp_counts = collections.Counter(exp_spec)
    for key in spec_counts:
        if not (key in exp_counts) or (spec_counts[key] > exp_counts[key]):
            return False
    return True

def main():
    print('enter experimental spectrum')
    #sys.argv[1]
    exp_spec_str = input()
    exp_spec =[int(n) for n in exp_spec_str.split()]
    exp_mass = max(exp_spec)
    mass_table = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
   
    start_peptides = get_starter_peptides(mass_table, exp_spec)   
    peptides = start_peptides
    while not not peptides and len(peptides[0]) < len(exp_spec):
        orig_peptides = append_peptides(peptides, start_peptides)
        peptides = append_peptides(peptides, start_peptides) 
        for peptide in orig_peptides:
            pep = [int(n) for n in peptide.split('-')]
            spec = get_linear_spec(pep) 
            if max(spec) == exp_mass:
                cyclic = circularize(pep)
                if cyclic == exp_spec:
                    print (peptide)
                    peptides.remove(peptide)
            if not is_consistent(spec, exp_spec):
                peptides.remove(peptide)

if __name__ == '__main__':
  main()

