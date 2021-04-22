import sys
sys.stdin = open("sample_input.txt")

# 큐로 안풀고 방문체크&bfs로 풀었더니 시간초과 남
# :: 다익스트라 문제여서 큐로 풀어야한다.
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N:
                n_add = 1  # next_add (다음칸으로 더해줄 숫자)
                if a[nx][ny] > a[x][y]:
                    n_add += a[nx][ny]-a[x][y]
                if cnt[nx][ny] > cnt[x][y]+n_add:
                    cnt[nx][ny] = cnt[x][y]+n_add  # 갱신
                    q.append((nx,ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[float('inf') for _ in range(N)] for _ in range(N)]
    cnt[0][0] = 0
    bfs(0, 0)  # start x,y
    
    print("#{} {}".format(tc, cnt[N-1][N-1]))

