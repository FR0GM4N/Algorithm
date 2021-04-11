import sys
sys.stdin = open("sample_input.txt")

# 상하좌우 탐색 방향 델타
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(s_x, s_y):
    global res, cnt

    if s_x == e_x and s_y == e_y:
        res = cnt - 1  # 맨 마지막 3도 카운팅 해줘서 하나 빼줘야함
        return

    for i in range(4):
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 밖이면 패쓰
            continue
        if miro[nx][ny] == 1:  # 벽이면 패쓰
            continue
        if not visited[nx][ny]:  # 방문 안했으면 방문하고 길이 카운팅
            visited[nx][ny] = 1
            cnt += 1
            DFS(nx, ny)
            cnt -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    # 시작, 도착점 좌표 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                s_x, s_y = i, j
            if miro[i][j] == 3:
                e_x, e_y = i, j

    visited = [[0] * N for _ in range(N)]  # 방문체킹 리스트
    visited[s_x][s_y] = 1  # 방문체크
    cnt = 0  # 경로 길이 카운팅 변수
    res = 0
    DFS(s_x, s_y)
    print("#{} {}".format(tc, res))

