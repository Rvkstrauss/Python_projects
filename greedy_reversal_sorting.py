import sys


def change_sign(perm_list, i, o):
    if perm_list[i] == '-' + str(i + 1):
        perm_list[i] = '+' + str(i + 1) 
        print_permutation(perm_list, o)

def reverse_block_signs(perm_list, i, ind):
    for j in range(i, ind + 1):
        if '+' in perm_list[j]:
            perm_list[j] = perm_list[j].replace('+', '-')
        else:
            perm_list[j] = perm_list[j].replace('-', '+')

def reverse_block(perm_list, i, ind):
    temp_list = perm_list[i:ind + 1]
    temp_list.reverse()
    perm_list[i:ind + 1] = temp_list

def is_in_order(perm_list, i):
    return perm_list[i] == ('+' + str(i + 1))

def find_index_of_block(perm_list, i):
    for j in range(0, len(perm_list)):
        if perm_list[j].strip('+-') == str(i + 1):
            ind = j
    return ind

def reverse_to_identity_permutation(perm_list, o):
    for i in range(0, len(perm_list)):
        if not is_in_order(perm_list, i):
            ind = find_index_of_block(perm_list, i) 
            reverse_block(perm_list, i, ind)
            reverse_block_signs(perm_list, i, ind)
            print_permutation(perm_list, o)
        change_sign(perm_list, i, o)

def print_permutation(perm_list, o):
    o.write('(')
    for i in range(0, len(perm_list)): 
        if i != len(perm_list) - 1:
            o.write(perm_list[i] + ' ')
        else:
            o.write(perm_list[i])
    o.write(')\n')

def main():
    f = open('input.txt', 'r')
    o = open('output.txt', 'w')
    perm_string = f.readline().strip('\n')
    perm_string = perm_string.strip('()')
    perm_list = perm_string.split(' ')

    reverse_to_identity_permutation(perm_list, o)
    f.close()
    o.close()

if __name__ == '__main__':
    main()
