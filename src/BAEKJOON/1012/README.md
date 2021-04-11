# 1012번 유기농 배추

[문제 보러가기](https://www.acmicpc.net/problem/1012)

🚩 `그래프 이론`, `그래프 탐색`, `DFS`, `BFS`

<br>

## 🅰 설계

1. 틀림 (fail)

샘플output은 맞았는데 백준에 돌려보니 틀렸다.

어차피 →↓으로 진행되서 오른쪽, 아래 델타만 탐색했는데 이것 때문인것 같다. 4방향 탐색했을 땐 패쓰 뜸

```python
def dfs(r,c):
    dr = [0, 1]
    dc = [1, 0]
    a[r][c] = -1  # 방문체크
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위체크
            continue
        if a[nr][nc] == 1:
            a[nr][nc] = -1  # 방문체크
            dfs(nr,nc)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # M:가로길이(열 길이), N:세로길이(행 길이), K:배추개수
    a = [[0] * M for _ in range(N)]  # 배추밭

    for _ in range(K):  # 배추 1로 바꾸기
        c, r = map(int, input().split())
        a[r][c] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:  # 배추면 카운트+1 & 방향 탐색
                dfs(i,j)
                cnt += 1

    print(cnt)
```

2. 런타임에러 (fail)

위 코드에서 델타만 상하좌우 4방향 탐색으로 바꿨더니 **런타임에러**가 났다.

⭐ 구글링 했더니 **재귀 limit을 설정해주지 않아서 발생**한 문제라고 한다. 

K(1 ≤ K ≤ 2500)의 범위가 엄청 커서 그런듯

파이썬의 기본 재귀 한도가 (1000)이어서 재귀 깊이가 1000을 넘어갈 경우 모듈을 추가해줘야한다.

<br><br>

## 🅱 최종 코드

**`sys.setrecursionlimit(10000)` 모듈 추가**

```python
import sys
sys.setrecursionlimit(10000)

def dfs(r,c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    a[r][c] = -1  # 방문체크
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위체크
            continue
        if a[nr][nc] == 1:
            a[nr][nc] = -1  # 방문체크
            dfs(nr,nc)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # M:가로길이(열 길이), N:세로길이(행 길이), K:배추개수
    a = [[0] * M for _ in range(N)]  # 배추밭

    for _ in range(K):  # 배추 1로 바꾸기
        c, r = map(int, input().split())
        a[r][c] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:  # 배추면 카운트+1 & 방향 탐색
                dfs(i,j)
                cnt += 1

    print(cnt)
```

<br><br>

## ✅ 후기

dfs 오랜만에 풀었는데 아주 어색했다

꾸준히 풀 것

백준은 런타임에러가 뜨면 제발 뭐때문에 뜬 건지 알려줬으면 좋겠다

### 새롭게 알게된 점

 최대 재귀 깊이 늘리는 모듈

```python
import sys 
sys.setrecursionlimit(10000)
```