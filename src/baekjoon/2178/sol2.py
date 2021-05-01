# 인풋 배열 자체를 갱신하는 방법 (리스트를 int형으로 받으면 [0,0]값도 갱신되므로 str으로 받는다)
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0, 0))
    a[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and a[nx][ny] == '1':
                a[nx][ny] = a[x][y] + 1
                q.append((nx, ny))



N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
bfs()

print("{}".format(a[N-1][M-1]))

