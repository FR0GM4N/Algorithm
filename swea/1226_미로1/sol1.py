import sys
sys.stdin = open("input.txt")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(s_x, s_y):
    global res

    if s_x == e_x and s_y == e_y:
        res = 1
        return
    for i in range(4):
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if nx < 0 or nx >= 16 or ny < 0 or ny >= 16:
            continue
        if miro[nx][ny] == 1:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            DFS(nx, ny)

T = 10
for tc in range(1, T+1):
    t = int(input())
    miro = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                s_x, s_y = i, j
            if miro[i][j] == 3:
                e_x, e_y = i, j

    visited = [[0] * 16 for _ in range(16)]
    res = 0
    DFS(s_x, s_y)

    print("#{} {}".format(t, res))