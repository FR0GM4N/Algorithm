import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    b = input()
    t = input()

    b_set = set()
    for i in range(len(b)):
        for k in range(2):
            b_set.add(int(b[:i] + str(k) + b[i+1:], 2))

    t_set = set()
    for i in range(len(t)):
        for k in range(3):
            t_set.add(int(t[:i] + str(k) + t[i+1:], 3))

    res = b_set & t_set
    print("#{} {}".format(tc, *res))