import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    cnt = 0
    for i in range(N):
        if not M & (1<<i):
            print("#{} OFF".format(tc))
            break
        else:
            cnt += 1
    if cnt == N:
        print("#{} ON".format(tc))