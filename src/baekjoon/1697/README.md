# 1697번 숨바꼭질

[문제 보러가기](https://www.acmicpc.net/problem/1697)

🚩 `그래프 이론`, `그래프 탐색`, `BFS`

<br>

## 🅰 설계

1. fail (메모리초과)

 N(0 ≤ N ≤ 100,000), K(0 ≤ K ≤ 100,000) 범위가 커서 방문체킹을 인덱스로 접근하는 리스트로 안만들고 딕셔너리로 만들었는데 메모리 초과났다.

구글링해보니, 이렇게 하면 방문했던 노드도 큐에 다시 넣어져서 그렇다고 한다.

```python
from collections import deque

def bfs(x):
    global res
    q = deque()
    q.append(x)
    visited = {x:1,}

    while q:
        x = q.popleft()
        if x == K:
            res = visited[x]-1
            return
        tmp = []  # 연결노드 담을 임시 리스트
        tmp.extend([x - 1, x + 1, 2 * x])
        for v in tmp:
            if not visited.get(v, 0):  # 방문 안했으면 방문체크
                visited[v] = visited[x]+1
                q.append(v)
        tmp = []  # 초기화


N, K = map(int, input().split())  # N:수빈, K:동생
res = 0
bfs(N)
print(res)
```

2. success 😀

방문체킹 리스트를 100,001 개 칸으로 만들어줬더니 패쓰했다.

칸이 10만개 있어도 상관없군 🤔

**이때 주의할건 19번째 줄에 `if 0<=v <=100000:` 조건을 설정해야한다 !!!**

처음 이 조건 안 썼을 때 런타임에러가 나서 찾아보니 x가 가질 수 있는 값이 x-1, x+1, x² 인데 

동생 위치의 범위가 0 ≤ K ≤ 100,000 이므로 x-1, x+1, x² 값들은 0~100,000 사이에 있어야 한다.

<br>

## 🅱 최종 코드

```python
from collections import deque


def bfs(x):
    global res
    q = deque()
    q.append(x)
    visited = [0]*100001
    visited[x] = 1

    while q:
        x = q.popleft()
        if x == K:
            res = visited[x]-1
            return
        tmp = []  # 연결노드 담을 임시 리스트
        tmp.extend([x - 1, x + 1, 2 * x])
        for v in tmp:
            if 0<=v <=100000:  # ⭐ 런타임에러(out of range) 방지용 범위설정
                if not visited[v]:  # 방문 안했으면 방문체크
                    visited[v] = visited[x]+1
                    q.append(v)
        tmp = []  # 초기화


N, K = map(int, input().split())  # N:수빈, K:동생
res = 0
bfs(N)
print(res)
```

<br>

## ✅ 후기

실버 1을 보고 실패각이라고 생각했는데 패쓰해서 행복하다 엉엉

 

### 새롭게 알게 된 점

⭐ 메모리 초과 발생 이유:

과거에 했던 값을 계속 처리하기 위해 큐에 값을 넣는 것 때문에 발생함.

ex. 10에서 갈 수 있는 노드: 9, 11, 20. but, 10까지 갈 수 있는 방법 엄청 많음. (9->10, 11->10, 5->10 ... )

10으로 일단 도착하면 위의 3가지 길은 한번만 계산하면 되므로 방문여부를 확인하는 배열을 하나 추가해서 방문할때마다 true로 설정해두고 체크하면서 이 문제를 해결할 수 있다.

- 출처: https://1sook.tistory.com/20

