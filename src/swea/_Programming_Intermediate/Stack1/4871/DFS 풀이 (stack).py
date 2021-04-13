import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    # V개의 노드, E개의 간선
    V, E = map(int, input().split())

    # 1. 인접행렬 방식
    # 연결 체킹하는 매트릭스 생성
    # edge_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    # for _ in range(E):
    #     start_node, end_node = map(int, input().split())
    #     edge_matrix[start_node][end_node] = 1

    # 2. 인접리스트 방식
    edge_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))

    visited = [False] * (V+1)  # 방문했는지 안했는지 체크하는 리스트 ( V = [ F F F F F F] )
    stack = [S]  # 출발점을 S로 하겠다.

    while stack:  # 하나라도 stack에 있으면 계속 반복. stack 다 돌면 비어있게 됨.
        now = stack.pop()
        # 방문한 경우
        if visited[now]:
            pass
        # 방문 하지 않은 경우 방문하고 F->T로 체인지
        else:
            visited[now] = True
            # 현재 노드와 연결된 모든 노드를 반복
            for v in edge_list[now]:
                # 방문을 안했다면 if visited[v] == False:
                if not visited[v]:
                    stack.append(v)

    result = 1 if visited[G] else 0

    print("#{} {}".format(tc, result))
