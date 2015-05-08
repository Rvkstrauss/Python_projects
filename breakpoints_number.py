import sys

def create_number_list(perm_list):
    num_list = [0]
    for val in perm_list:
        if val[0] == '+':
            num_list.append(int(val[1:]))
        else:
            num_list.append(-1 * int(val[1:]))
    num_list.append(len(perm_list) + 1)
    return num_list

def count_breakpoints(perm):
    breakpoints = 0
    for i in range(0, len(perm)-1):
        if (perm[i + 1] - perm[i]) != 1:
            breakpoints += 1
    return breakpoints

def main():
    f = open('data.txt', 'r')
    perm_string = f.readline().strip('\n')
    perm_string = perm_string.strip('()')
    perm_list = perm_string.split(' ')

    perm = create_number_list(perm_list)
    breakpoints = count_breakpoints(perm)
    print breakpoints


if __name__ == '__main__':
    main()
