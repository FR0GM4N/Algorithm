# 2814. 최장경로

N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로를 구하는 문제

(경로의 길이는 경로 상에 등장하는 정점의 개수임)

<br>

### 0️⃣ 현재 노드 상태

![image-20210421173955841](https://user-images.githubusercontent.com/77573938/115530238-8e579800-a2ce-11eb-835d-bc4baea810c9.png)

<br>

### 1️⃣ 인접리스트로 연결 노드 정보 받아오기

```python
N, M = map(int, input().split())  # N:정점, M:간선개수
edge_list = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    edge_list[x].append(y)
    edge_list[y].append(x)
```

```python
# edge_list
[[], [2], [1, 3], [2]]
```

<br>

### 2️⃣ DFS 재귀 풀이 1

```python
def dfs(s, cnt):  # 시작노드, 카운트
    global res
    if res < cnt:
        res = cnt
        # return  <- 리턴하나 안하나 pass는 되는데, 리턴하면 동일한 경로길이를 한번만 체킹함
    for v in edge_list[s]:
        if not visited[v]:
            visited[v] = 1
            dfs(v, cnt+1)
            visited[v] = 0


# 본문 코드            
    res = 0
    visited = [0] * (N + 1)
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
```

<br>

### 2️⃣ DFS 재귀 풀이 2

```python
def dfs(s, cnt):  # 시작노드, 카운트
    global res
    if res < cnt:
        res = cnt
    visited[s] = 1
    for v in edge_list[s]:
        if not visited[v]:
            dfs(v, cnt+1)
    visited[s] = 0


# 본문 코드    
	res = 0
    visited = [0] * (N + 1)
    for i in range(1, N+1):
        dfs(i, 1)
```

<br>

`cnt` 를 함수의 인자로 안하고 함수 내에서 계산한 후, `res` 와 크기 비교를 하고 싶었는데 fail이 떴다..

디버깅을 해보니 cnt횟수가 누적되어서 그런것 같다. 

`cnt -= 1` 을 하면 계속 초기화가 되어 이 방법도 안되는 것 같다.. 흠 😐

함수의 인자로 넘겨주면 자동으로 재귀가 끝나면서 원상복구되서 이 방법이 best인것인가..?!

그냥 방문체킹만 하는 것보다 경로 길이 구하는게 더 어렵다 ~

<br><br><br>

---

### 🆖 실패코드

```python
T = int(input())

def dfs(s):  # 시작노드
    global res, cnt
    cnt += 1
    visited[s] = 1
    for v in edge_list[s]:
        if not visited[v]:
            dfs(v)
    visited[s] = 0


for tc in range(1, T+1):
    N, M = map(int, input().split())  # N:정점, M:간선개수
    edge_list = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        edge_list[x].append(y)
        edge_list[y].append(x)

    res, cnt = 0, 0
    visited = [0] * (N + 1)
    for i in range(1, N+1):
        dfs(i)
        res = max(res, cnt)
        cnt = 0  # 초기화

    print("#{} {}".format(tc, res))
```





