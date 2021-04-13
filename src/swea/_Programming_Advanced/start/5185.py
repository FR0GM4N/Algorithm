import sys
sys.stdin = open("sample_input.txt")

T = int(input())

hexa = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
for tc in range(1, T+1):
    N, inp = input().split()

    res = ""
    for ele in inp:
        if ele not in hexa:
            m = int(ele)
        else:
            m = hexa[ele]
        tmp = ""
        for i in range(4):
            tmp += str(m % 2)
            m //= 2
        res += tmp[::-1]
    print("#{} {}".format(tc, res))
