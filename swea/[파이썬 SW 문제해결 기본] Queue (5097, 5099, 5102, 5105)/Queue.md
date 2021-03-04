# 📎 Queue

[파이썬 SW 문제해결 기본 - Queue](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg&&)

🌟 주요 개념

- BFS
- Queue

<br><br><br>

# [swea] 5097. 회전

so easy ㅋ 큐의 개념을 알 수 있었음

이 문제를 큐로 안풀고(중간 for문- pop / append 안하고) 규칙으로 접근하면 걍 바로  `numbers[M % N]` 으로 출력하면 답이 나온다 !  대박 신기

<br>

### 코드

```python
import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        t = numbers.pop(0)
        numbers.append(t)

    print("#{} {}".format(tc, numbers[0]))
```

<br><br><br>

# [swea] 5105. 미로의 거리

지난 시간에 Stack2 문제로 미로를 한번 해서 그런지 좀 할만했다.

근데 Queue 카테고리인데 큐가 전혀 사용되지 않았다... 그냥 `4875_미로 (Stack2)` 랑 똑같이 재귀함수 이용해서 풀되, 카운트만 추가해줬다. 이건 스택을 이용한거 같은데 이게 맞는 풀이인가,, 흠 🤨 

<br>

### 코드

26번째 줄에 `visited[nx][ny] = 0` 안써도 된다. 왜냐면  `4875_미로` 처럼 정답이 아닌 길을 다시 돌아갈 필요가 없기 때문에 잘못 온 길만큼만 카운트만 취소해주면 된다.

💦 그냥 13번째 줄에서 `return cnt-1` 을 바로 해주고 싶었는데 그렇게 하면 `None` 이 리턴된다.

```python
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
            # visited[nx][ny] = 0  <- 안써도 됨
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


```

<br><br><br>

# [swea] 5099. 피자 굽기

치즈의 양이 0이 되면 pop하고 new 치즈 append 하면서 마지막 남은 치즈의 인덱스 출력하고자 했다. 그럴려면 인덱스를 찾아야 하는데, 처음에 아무생각 없이 튜플로 만들었다. 근데 답이 계속 안나와서 도대체 뭐가 잘못된거지 생각했는데 튜플은 안에 값이 변경 불가라는 특징을 갖고있는 자료형이다...... 나 진짜 멍충쓰 🙄

그래서 다시 리스트로 인덱스와 치즈 값을 같이 묶어준 후, 리스트 요소 접근을 통해 값을 직접적으로 바꿔주었다.

<br>

💥 내가 생각하지 못한 good point :

- enumerate로 접근하는 방식을 아예 몰랐다. 꼭 기억할 것!!!!!

  ```python
  pizza = [[v, i] for i, v in enumerate(cheese)]  # i:cheese 요소의 인덱스, v: cheese 요소 값
  print(pizza)
  
  # 출력
  [[7, 0], [2, 1], [6, 2], [5, 3], [3, 4]]
  ```

- 그리고 제발 슬라이싱을 잊지말자!!!! 처음 인풋받은 cheese 리스트 자체를 cheese`[:n]`,  `cheese[:n]` 로 했으면 오븐에 들어간 피자, 못 들어간 피자 한번에 나뉨........ 멍충쓰...... 

<br><br>

#### 💡 enumerate

enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.

```python
for i, name in enumerate(['body', 'foo', 'bar']):
	print(i, name)

# 출력
0 body
1 foo
2 bar
```

순서 값과 함께 body, foo, bar가 순서대로 출력된다. 그래서 for문처럼 반복문에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할때 enumerate 함수를 사용하면 매우 유용하다.

* 출처: [점프 투 파이썬](https://wikidocs.net/32#enumerate)

<br><br>

### 코드

```python
import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N:화덕의 크기, M: 피자 개수
    cheese = list(map(int, input().split()))  # M개의 피자에 뿌려진 각 치즈 양

    cheese_check = []  # 치즈랑 인덱스랑 같이 묶어줄 리스트
    for i in range(M):
        cheese_check.append([cheese[i], i])

    oven = []  # 오븐 안에 들어간 치즈들
    for i in range(N):
        oven.append(cheese_check.pop(0))

    while True:
        if len(oven) == 1:
            break
        oven[0][0] = oven[0][0] // 2
        f_c = oven[0][0]
        t = oven.pop(0)
        if f_c != 0:
            oven.append(t)
        elif cheese_check and f_c == 0:  # 치즈가 남은 상태라면
            oven.append(cheese_check.pop(0))
        elif not cheese_check and f_c == 0:  # 치즈 안남은 상태라면
            continue

    print("#{} {}".format(tc, oven[0][1] + 1))
```

<br><br><br>

# [swea] 5102. 노드의 거리

so difficult ........... ㅋ

내가 처음 푼 풀이는 틀렸다. . . ㅋ

어디가 틀린건지, 다른 사람들은 어떻게 풀었는지 궁금해서 구글링한 후 다시 풀었을 때는 맞았다...

내 첫 풀이는 어디가 틀린걸까 ??! 😭

<br>

### 첫 풀이 (fail)

```
* 문제 조건: 10개 테스트케이스를 합쳐서 Python의 경우 2초

채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 10개의 테스트케이스 중 3개가 맞았습니다.)

제한시간 초과가 발생하였습니다. 제한시간 초과로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
```

> 샘플 테스트케이스는 맞았으나 swea 상에서 제한시간 초과와 테케 10개중 3개만 맞았다고 떴다.
>
> time 함수와 swea 상에서 run 했을 시 시간이 나오는데 분명 2초 이내(0.12984s)였다. 그런데 왜 제한시간 초과가 떴는지 모르겠어서 교수님께 물어보니 저 시간은 주어진 샘플 케이스 3개에 대한 시간이어서 숨겨진 테스트 케이스 중 시간이 오래 걸리는 케이스가 있을 수 있다는 것이었다.

<br>

어제 수업에서 배운 `size` 를 이용해서 시작점 노드와 떨어진 거리만큼 `k` 값을 증가시키는 방향으로 코드를 짰다.

도대체 어디가 잘못된걸까 🤮 어제 푼 `2814_최장경로` 도 틀렸음 ㅋ 샘플 테케는 맞는데 돌려보면 fail ㅋ

```python
import sys
sys.stdin = open("sample_input.txt")


def bfs(S):
    global res
    visited = [0] * (V + 1)
    queue = [S]  # 시작점부터 시작. 큐에 넣다 빼면서 체킹할거임
    visited[S] = True
    k = 0
    while True:
        size = len(queue)
        for i in range(size):
            t = queue.pop(0)  # 큐 첫번째 원소 pop
            if t == G:
                res = visited[t]
                return
            for v in edge_list[t]:
                if not visited[v]:
                    visited[v] = k+1  # 큐의 사이즈 만큼 반복문 돌면서 해당하는 노드들만 길이 증가
                    queue.append(v)
        k += 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        edge_list[s].append(e)
        edge_list[e].append(s)

    S, G = map(int, input().split())
    res = 0
    bfs(S)

    print("#{} {}".format(tc, res))
```

<br><br>

### 두번째 풀이 (pass)

✅  일반적으로 노드 경로의 길이를 찾을 때 방문체크 리스트처럼 거리를 체킹하는 `distance` 리스트를 만들어서 푼다고 한다.

✅  그리고 또 아주 신기한걸 배웠다.

**21번째 줄에 return 안써도 답 나온다.** 어떤 차이냐면, **return을 안쓰면 완전탐색을 하고, return을 쓰면 완탐 전에 원하는 결과값 찾으면 거기서 끝내는 것이다.** 그래서 시간이 좀 걸리더라도 결과값은 동일하게 나온다. 그런데 이 문제에서는 굳이 완탐을 할 이유가 없어서 return을 써서 더 빨리 프로그램을 끝나도록 하는 것이다 !!

```python
import sys
sys.stdin = open("sample_input.txt")

def bfs(S):
    global res
    queue = [S]  # 시작점 큐에 먼저 넣고, 방문체크 한 다음 함수 실행
    visited[S] = 1

    while queue:  # 큐 비어있을 때까지 반복
        t = queue.pop(0)
        for v in edge_list[t]:  # pop한 애랑 연결된 노드 중
            if not visited[v]:  # 방문 안 한 노드면
                visited[v] = 1  # 방문체크하고
                queue.append(v)  # 큐에 넣음
                distance[v] = distance[t]+1  # 전의 노드의 길이에 1 추가
                if v == G:  # 도착점이랑 같아지면 길이값 반환하고 리턴
                    res = distance[v]
                    return

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        edge_list[s].append(e)
        edge_list[e].append(s)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)  # 방문체킹 리스트
    distance = [0] * (V + 1)  # 시작점으로부터 거리 체킹 리스트
    res = 0
    bfs(S)

    print("#{} {}".format(tc, res))
```

<br><br><br><br><br><br>

stack2 보다는 할만하고 재밌었다 ㅎ

앞으로의 알고리즘도 파이티이이잉 👊

