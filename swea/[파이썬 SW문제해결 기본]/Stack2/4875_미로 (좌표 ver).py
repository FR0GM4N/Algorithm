# 출발점과 도착점을 먼저 구한 후, 이동하면서 도착점과 같아지면 res = 1 리턴하는 함수로 풀 예정

import sys
sys.stdin = open("sample_input.txt")

# 사방 탐색해야하니까 먼저 디렉션 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(s_x, s_y):
    global res, visited, e_x, e_y

    if s_x == e_x and s_y == e_y:
        res = 1
        return

    visited[s_x][s_y] = 1  # 방문체크
    for i in range(4):  # 4방향 체크
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위체크. 범위 벗어나면 패쓰
            continue
        if miro[nx][ny] == 1:  # 벽인지 체크. 벽이면 패쓰
            continue
        if not visited[nx][ny]:  # 방문 안 했으면 방문하고 계속 재귀
            visited[nx][ny] = 1
            dfs(nx, ny)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]  # 0:통로, 1:벽, 2:출발, 3:도착

    # 출발점과 도착점을 먼저 구한 후, 이동하면서 도착점과 같아지면 res = 1 리턴하는 함수로 풀 예정
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                s_x, s_y = i, j
            if miro[i][j] == 3:
                e_x, e_y = i, j
    visited = [[0] * N for _ in range(N)]  # 미로의 크기만큼 방문체크 배열 만듦
    res = 0
    dfs(s_x, s_y)

    print("#{} {}".format(tc, res))