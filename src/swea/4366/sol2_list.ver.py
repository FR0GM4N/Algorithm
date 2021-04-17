import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    b = input()
    t = input()

    b_lst = []
    for i in range(len(b)):
        if b[i] == '1':
            tmp = '0'
        else:
            tmp = '1'
        b_lst.append(int(b[:i] + tmp + b[i+1:], 2))

    for i in range(len(t)):
        for k in range(3):
            if t[i] != str(k):
                ter = int(t[:i] + str(k) + t[i+1:], 3)
                if ter in b_lst:
                    res = ter

    print("#{} {}".format(tc, res))