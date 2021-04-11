import sys
sys.stdin = open("sample_input.txt")

# 처음 풀었을 때는 함수의 인자로 시작점과 edge_list를 같이 받았는데, 생각해보니 어차피 edge_list는 변하지 않는 자료이므로 그냥 global로 전역참조 시킴
def dfs(S):
    global res  # res만 참조해서 값 변경해주려고 얘만 global 설정함

    visited[S] = True  # 리스트는 전역에 존재하지만, 리스트 안의 요소를 바꿀때는 global 참조 안해도 됨
    for v in edge_list[S]:
        if not visited[v]:
            # visited[v] = True <- 어차피 11번째 줄에서 체킹해줘서 여기에 안써도 됨.
            if v == G:  # 도착노드와 같으면 끝
                res = 1
                return
            dfs(v)

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
    dfs(S)  # 시작점을 인자로 받음

    print("#{} {}".format(tc, res))