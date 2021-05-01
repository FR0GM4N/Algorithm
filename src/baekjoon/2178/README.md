# 2178번 미로 탐색

[문제 보러가기](https://www.acmicpc.net/problem/2178)

🚩 `BFS`

<br>

## 🅰 설계

최소 칸수를 구하는 문제이므로 bfs로 해결하자고 생각했다.

1. 시간초과 (Fail)

 bfs로 접근한다면서 DFS로 코드 짰다.. 바보 아닌지

함수 이름만 bfs .. 😅

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, cnt):
    global res
    if res < cnt:
        return
    if x == N-1 and y == M-1:
        res = cnt
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and a[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = 1
            bfs(nx, ny, cnt+1)
            visited[nx][ny] = 0



N, M = map(int, input().split())
a = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
res = 987654321
visited[0][0] = 1
bfs(0, 0, 1)

print("{}".format(res))
```

<br>

## 🅱 최종 코드

bfs로 코드를 짰다. 

### 풀이 1

visited라는 배열을 만들어 푸는 방법

```python
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global visited
    q = deque()  # 큐 만들고
    q.append((0, 0))  # 시작점 넣어주고
    visited[0][0] = 1  # 값 갱신

    while q:  # 큐에 값이 있으면
        x, y = q.popleft()  # 맨 왼쪽 값 빼서 할당하고
        for i in range(4):  # 사방 탐색하면서
            nx = x+dx[i]
            ny = y+dy[i]
            # 인덱스가 범위 이내이면서 미로의 값이 1이고 아직 방문하지 않았다면
            if 0<=nx<N and 0<=ny<M and a[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1  # 방문체크(이전 값에 1을 더하면서 값 갱신)
                q.append((nx, ny))  # 큐에 넣는다



# 최소 칸 -> bfs
N, M = map(int, input().split())
a = [list(map(int, input())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]  # 값 갱신할 2차원배열
bfs()

print("{}".format(visited[N-1][M-1]))
```

```python
# visited 출력결과 (testcase 1번)

[
 [1, 0, 9, 10, 11, 12], 
 [2, 0, 8, 0, 12, 0], 
 [3, 0, 7, 0, 13, 14], 
 [4, 5, 6, 0, 14, 15]
]
```

<br>

### 풀이 2

애초에 받은 input 2차원배열(`a`) 자체를 갱신하는 방법

이 방법으로 할때는 input 리스트를 int형으로 받으면 [0,0]의 값이 1이 안되고 갱신되기 때문에 str형으로 그냥 받아 처리한다.

(사실 최종 결과값은 동일하나 더 정확한 풀이를 위해..😊)

```python
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0, 0))
    a[0][0] = 1  # 시작점의 값을 int형으로 갱신하고 시작

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and a[nx][ny] == '1':  # 방문체크를 굳이 안하도 된다.
                a[nx][ny] = a[x][y] + 1
                q.append((nx, ny))



N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]  # str형으로 받음
bfs()

print("{}".format(a[N-1][M-1]))
```

```python
# a 출력결과 (testcase 1번)

[
 [1, '0', 9, 10, 11, 12], 
 [2, '0', 8, '0', 12, '0'], 
 [3, '0', 7, '0', 13, 14], 
 [4, 5, 6, '0', 14, 15]
]


# a를 int형으로 받았을 때 출력결과
[
 [3, 0, 9, 10, 11, 12], 
 [2, 0, 8, 0, 12, 0], 
 [3, 0, 7, 0, 13, 14], 
 [4, 5, 6, 0, 14, 15]
]
```



<br>

## ✅ 후기

BFS로 풀자면서 DFS 코드를 입력하다니... 어이없다

bfs보다 dfs를 상대적으로 많이 풀어서 그런거 같다

bfs를 좀 더 많이 풀어야겠다 !