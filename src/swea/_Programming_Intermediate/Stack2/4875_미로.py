import sys
sys.stdin = open("sample_input.txt")

def isRange(r, c):
    # 이 범위에 들어가면 return True(즉, 이 범위이면 반환), 안들어가면 return False.
    return 0 <= r < N and 0 <= c < N and (maze[r][c] == 0 or maze[r][c] == 3)

def dfs(nr, nc):
    global res
    # 도착하면 1 리턴하고 끝냄
    if maze[nr][nc] == 3:
        res = 1
        return

    # 현재 내 위치 방문도장 찍고
    visited.append((nr, nc))
    # 상하좌우 방향 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    for d in range(4):
        r = nr + dr[d]
        c = nc + dc[d]
        # 인덱스 범위 안에 있으면서 0,3 인 애들 중 방문 아직 안했으면 dfs 체킹
        if isRange(r, c) and (r, c) not in visited:
            dfs(r, c)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # 0:통로, 1:벽, 2:출발, 3:도착

    # 먼저 출발점을 찾음
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                nr, nc = i, j

    visited = []
    res = 0
    dfs(nr, nc)
    # 도착가능-> 1, 불가능-> 0 출력
    print("#{} {}".format(tc, res))

