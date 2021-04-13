import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = []
    for i in range(N):
        res.append(M % 2)
        M //= 2

    ans = 'OFF' if 0 in res[:N] else 'ON'
    print("#{} {}".format(tc, ans))

