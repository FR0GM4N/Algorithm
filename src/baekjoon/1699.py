import sys

N = int(sys.stdin.readline())
dp = [0 for i in range(N+1)]
sq_lst = [i*i for i in range(1, 317)]

for i in range(1, N+1):
    tmp = []
    for sq in sq_lst:
        if i >= sq:
            tmp.append(dp[i-sq])
    dp[i] = min(tmp)+1

print(dp[N])