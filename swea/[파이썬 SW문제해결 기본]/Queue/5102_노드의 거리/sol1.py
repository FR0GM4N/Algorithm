import sys
sys.stdin = open("sample_input.txt")


def bfs(S):
    global res
    visited = [0] * (V + 1)
    queue = [S]  # 시작점부터 시작. 큐에 넣다 빼면서 체킹할거임
    visited[S] = True
    k = 0
    while queue:  # while True 아님! 주의할것
        size = len(queue)
        for i in range(size):
            t = queue.pop(0)  # 큐 첫번째 원소 pop
            if t == G:
                res = visited[t]
                return
            for v in edge_list[t]:
                if not visited[v]:
                    visited[v] = k+1  # 큐의 사이즈 만큼 반복문 돌면서 해당하는 노드들만 길이 증가
                    queue.append(v)
        k += 1

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


