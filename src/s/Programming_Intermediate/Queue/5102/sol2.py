import sys
sys.stdin = open("sample_input.txt")

def bfs(S):
    global res
    queue = [S]  # 시작점 큐에 먼저 넣고, 방문체크 한 다음 함수 실행
    visited[S] = 1

    while queue:  # 큐 비어있을 때까지 반복
        t = queue.pop(0)
        for v in edge_list[t]:  # pop한 애랑 연결된 노드 중
            if not visited[v]:  # 방문 안 한 노드면
                visited[v] = 1  # 방문체크하고
                queue.append(v)  # 큐에 넣음
                distance[v] = distance[t]+1  # 전의 노드의 길이에 1 추가
                if v == G:  # 도착점이랑 같아지면 길이값 반환하고 리턴
                    res = distance[v]
                    return  # 리턴 안써도 됨. 안쓰면 완전탐색함(시간이 좀 걸리더라도 결과값은 동일). 리턴 쓰면 완탐 전에 원하는 결과값 찾으면 거기서 끝내는 것임.

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        edge_list[s].append(e)
        edge_list[e].append(s)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)  # 방문체킹 리스트
    distance = [0] * (V + 1)  # 시작점으로부터 거리 체킹 리스트
    res = 0
    bfs(S)

    print("#{} {}".format(tc, res))
