N = int(input())
a = list(map(int, input().split()))
a.sort()
memo = [0]*N
memo[0] = a[0]
for i in range(1, N):
    memo[i] = memo[i-1] + a[i]

print(sum(memo))