import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def dfs(s, cnt):  # 시작노드, 카운트
    global res
    if res < cnt:
        res = cnt
    visited[s] = 1
    for v in edge_list[s]:
        if not visited[v]:
            dfs(v, cnt+1)
    visited[s] = 0


for tc in range(1, T+1):
    N, M = map(int, input().split())  # N:정점, M:간선개수
    edge_list = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        edge_list[x].append(y)
        edge_list[y].append(x)

    res = 0
    visited = [0] * (N + 1)
    for i in range(1, N+1):
        dfs(i, 1)

    print("#{} {}".format(tc, res))

