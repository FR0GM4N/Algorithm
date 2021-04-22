import sys
sys.stdin = open("sample_input.txt")

from collections import deque

# 최소 -> 큐
def bfs(x):  # 연산 전 숫자
    global res
    q = deque()
    q.append(x)
    visited = [0]*1000001
    while q:
        x = q.popleft()
        if x == M:
            res = visited[x]
            return
        for v in (x+1, x-1, x*2, x-10):
            if 0<=v<=1000000 and not visited[v]:
                visited[v] = visited[x]+1
                q.append(v)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = 0
    bfs(N)
    print("#{} {}".format(tc, res))

