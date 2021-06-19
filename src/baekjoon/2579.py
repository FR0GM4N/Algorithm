N = int(input())
s = [int(input()) for _ in range(N)]
s.reverse()

dp = [0]*N
dp[0] = s[0]

for i in range(1, N):
    if i < 3:
        dp[i] = s[0] + s[i]
    else:
        dp[i] = max(dp[i-2]+s[i], dp[i-3]+s[i-1]+s[i])

print(max(dp[N-2], dp[N-1]))