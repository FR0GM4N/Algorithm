# 4871_그래프 경로 큐 풀이 (BFS)

import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    # V개의 노드, E개의 간선
    V, E = map(int, input().split())

    edge_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))

    visited = [False] * (V+1)  # 방문했는지 안했는지 체크하는 리스트 ( V = [ F F F F F F] )
    queue = [S]  # 출발점을 S로 하겠다.

    while queue:  # 하나라도 queue에 있으면 계속 반복. queue 다 돌면 비어있게 됨.
        now = queue.pop(0)
        # 방문 안 한 경우
        if not visited[now]:
            visited[now] = True
            # 현재 노드와 연결된 모든 노드를 반복
            for v in edge_list[now]:
                # 방문을 안했다면 if visited[v] == False:
                if not visited[v]:
                    queue.append(v)

    result = 1 if visited[G] else 0

    print("#{} {}".format(tc, result))