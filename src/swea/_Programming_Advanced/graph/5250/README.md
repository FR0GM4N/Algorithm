# 5250. 최소비용

### 문제

![image-20210422151319757](https://user-images.githubusercontent.com/77573938/115674591-c6231600-a388-11eb-8cc6-1f89fb37198a.png)

<br><br>

### Fail (제한시간 초과)

큐로 안풀고 방문체크&bfs로 풀었더니 시간초과가 났다.

이 문제는 행렬값이 가중치인 다익스트라 문제여서 큐로 풀어야 한다.

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s_x, s_y, cnt):
    global res
    if cnt >= res:
        return
    if s_x == N-1 and s_y == N-1:
        res = cnt
        return
    for d in range(4):
        nx = s_x + dx[d]
        ny = s_y + dy[d]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            visited[nx][ny] = 1
            if a[nx][ny] > a[s_x][s_y]:
                bfs(nx, ny, cnt+1+(a[nx][ny]-a[s_x][s_y]))
            else:
                bfs(nx, ny, cnt+1)
            visited[nx][ny] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    res = 987654321
    visited = [[0]*N for _ in range(N)]
    bfs(0, 0, 0)  # s_x, s_y, cnt
    
    print("#{} {}".format(tc, res))
```

<br><br>

### Pass (queue로 해결)

```python
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
```



