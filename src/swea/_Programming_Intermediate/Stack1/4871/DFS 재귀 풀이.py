import sys
sys.stdin = open("sample_input.txt")

def dfs(edge_list, S):
    global res, G
    if visited[G]:
        res = 1
        return

    visited[S] = True
    for v in edge_list[S]:
        if not visited[v]:
            visited[v] = True
            dfs(edge_list, v)
            # visited[v] = False  <- 이 줄 안써도 pass 됨... 미로문제처럼 다시 안 되돌려도 되는건가?? 어차피 안되는 곳 또 갈 필요 없어서??

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))

    visited = [False] * (V+1)
    res = 0
    dfs(edge_list, S)  # 연결리스트와 시작점을 인자로 받음

    print("#{} {}".format(tc, res))