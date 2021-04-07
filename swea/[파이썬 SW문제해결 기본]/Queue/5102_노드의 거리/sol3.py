import sys
sys.stdin = open("sample_input.txt")


def bfs(S):
    global res
    visited = [0] * (V + 1)
    queue = [S]
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        if t == G:
            res = visited[t]-1
            return
        for v in edge_list[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        edge_list[s].append(e)
        edge_list[e].append(s)

    S, G = map(int, input().split())
    res = 0
    bfs(S)

    print("#{} {}".format(tc, res))