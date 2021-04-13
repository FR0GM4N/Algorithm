import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = 0
    for i in range(N):
        if not M & (1<<i):
            print("#{} OFF".format(tc))
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        print("#{} ON".format(tc))


