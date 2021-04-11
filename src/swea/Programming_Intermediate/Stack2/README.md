# 📎 Stack 2

와 백트래킹, dfs, 스택, 재귀함수 너무 어렵다 🤯 

`4871_그래프경로` 처럼 트리구조에서 인접행렬, 인접리스트로 접근하는 문제는 할만 했는데 [파이썬 SW문제해결 기본 - Stack2](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg) 의 문제는 다 너무 어려웠다....   +  **2806_N-queen** 같은 유형

머리로는 어떻게 풀어야 할지 방향이 잡히는데 이걸 코드로 구현하는게 잘 안되고, 모르겠어서 구글링해봤는데도 이해가 안갔다..

<br>

### 🤔  Why ?!  문제풀다 궁금했던 것들

- 함수에서 global 변수 참조하는 이유 ?

  -> 재귀함수처럼 함수를 계속 불러다 쓸 껀데 함수 내에서 선언하게 되면 그 값이 계속 초기화가 되서

  & 함수 밖의 변수의 값을 참조해서 변경하려고

<br>

- 왜 함수 내에서 return 뒤에 아무것도 안 씀 ?
  
   `return 1` 이나 `return res` 등 뭔가를 적어줘야 하는것 아닌가?
  
  -> 이유 :
  
  - `return + result` 의 경우, 호출자에게 result 를 반환
  
  - `no return & no result` 의 경우, 함수 안의 코드블락만 실행하고 종료할 뿐 호출자에게는 None 반환
  
  - `return (no result)` 의 경우, 함수 즉시 종료. 
  
    이 경우 return 문은 함수 호출자에게 값을 반환(return)하는 의미로 쓰인 것이 아니고 함수를 종료(close) 하는 의미로 쓰인 것이다. 
  
    => 즉, `res = 1; return` 의 경우, None이 반환되되 res 값이 1로 바뀐다. 반환은 아무것도 안해주면서 값을 바꾸고 싶을 때 사용.

<br>

- 함수로 코드를 작성하는 이유 ?

  -> 재귀함수로 계속 체킹해줘야 되서 함수로 접근. 함수로 작성 안해도 되나 복잡 & 어려움.

  & 함수로 따로 빼서 작성하면 유지보수 편리 & 함수로 따로 빼주면 시간이 덜 걸림

<br><br>

---

<br>

# 4874. Forth

처음에는 14번째 줄의 `elif s == '.':` 인 경우를 `elif` 로 따로 안 빼고 `try~except` 문에서 `except` 로 처리한 후, 31번째 줄의 조건문에서 처리를 해주려고 했는데 잘 안됐다. 

그래서 어차피 `.` 이 나오면 문장의 끝이므로  for문을 종료할 수 있도록 `elif - break` 처리를 해주었다.

<br>

### 코드

```python
T = int(input())
for tc in range(1, T+1):
    S = input().split()
    stack = []
    operator = ['*', '/', '+', '-']
    res = 1
    for s in S:
        # 숫자인 경우
        if s != '.' and s not in operator:
            stack.append(s)
        elif s == '.':
            break
        else:
            try:  # 연산자인 경우
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if s == '+':
                    stack.append(n1 + n2)
                elif s == '-':
                    stack.append(n1 - n2)
                elif s == '*':
                    stack.append(n1 * n2)
                elif s == '/':
                    stack.append(n1 // n2)
            except:  # 스택이 비었거나 <숫자 숫자 연산자> 순이 아닐때
                res = 0

    if res == 1 and len(stack) == 1:
        print("#{} {}".format(tc, stack.pop()))
    elif res == 0 or len(stack) > 1:
        print("#{} error".format(tc))
```

- 인풋문자열을 순회하면서 숫자면 스택에 넣고, 연산자면 스택의 두 숫자를 빼서 연산을 해야하기 때문에 문자열이 `.` 과 `연산자` 가 아닌 경우로 조건을 걸어 숫자만을 스택에 넣게 조건처리 해주었다.

- 그런데 만약, 문자열이  `< 숫자, 숫자, 연산자 >` 순서가 아닌 경우에는 연산이 불가하기 때문에 elif문 안에 또 조건을 줄까 했으나 스택에 숫자가 하나만 있어서 pop을 못하거나 아예 스택이 비었거나 등등 경우의 수를 따져줄게 많아 그냥 `try~except` 문을 사용하여 예외처리하기로 했다. 

- `try` 안의 20~27번째 줄 역시 하나로 처리하고 싶었으나 각 연산자마다 계산 결과가 다르기 때문에 어떻게 처리할지 몰라 그냥 베이직하게 다 적었다. 

  그리고 여기서 문제 조건에서 나눗셈이 된다고해서 `/` 를 썼더니 fail이 떠서 뭐지하고 `//` 로 바꾸니 pass 됐다.. 몫이 아닌 나눗셈은 실수형이므로 조심하자 !

- 맨 마지막 조건문(31~34번째 줄)을 통해, res가 1이면서 스택의 길이가 1인 경우만 형식이 올바른 문자열이므로 pop해서 값을 출력하게 설정했다. 

  처음에는 스택의 길이가 1이라는 조건을 안쓰고 `res == 1` 조건만 써도 맞을 거 같았는데 10개의 테스트케이스 중 9개만 통과했다. 

  이유를 생각해보니  `< 숫자, 숫자, . >`  의 경우라면 res값은 그대로 1 이겠지만, 연산자가 없어 연산이 안되기 때문에 그런것 같다.

- 마찬가지로 error가 출력되는 경우는 res 값이 0이거나 위의 경우처럼 숫자만 나온다면 스택의 길이가 2 이상일것이므로 이 경우를 `or` 로 묶어주었다.

<br><br><br>

# 4875. 미로

💧 원래는 11번째 줄에서 `visited.append((nr, nc))` 를 안쓰고 `N x N` 행렬로 접근을 하려고 했는데 잘 안되서 튜플형식으로 접근했다..

아예 빈 리스트를 만들고 0 이나 3인 애들 중에 방문했으면 그 좌표를 넣어서 체킹해주는게 더 나은거 같다.

<br>

### 코드

```python
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
```

- 먼저 0과 3만 갈 수 있기 때문에 범위를 체킹하는 함수 `isRange` 를 만들어 주었고 , dfs 문제여서 `dfs()` 함수를 만들어 줬다.

- 미로에 대한 정보를 `maze` 라는 2차원 배열로 받은 후, 2가 출발점이어서 좌표를 찾은 후, 그 좌표부터 탐색을 시작했다.

- 결과값을 0으로 먼저 설정해 준 후, `dfs` 함수 내부에 전역변수(`global`) 로 가져와서 함수를 구성했다.

- 도착점(3)이 되면 함수를 종료하도록 리턴을 설정해주었고, 현 위치에 방문했다는 것을 체크하기 위해 `visited` 라는 빈 리스트에 좌표를 append  해주었다.

- delta 를 이용해서 상하좌우 탐색하며 인덱스 범위 안에 있으면서 0과 3인 애들 중 아직 방문 하지 않은 좌표들에 대해  `dfs` 함수를 적용해 체킹하도록 하는 함수를 설정했다.

<br>

### 또 다른 풀이 <- 이게 더 쉽고 이해 잘감

dfs 라는 함수를 만들어 재귀적으로 호출하며 좌표로 접근해서 풀었다.

```python
# 사방 탐색해야하니까 먼저 디렉션 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(s_x, s_y):
    global res, visited, e_x, e_y

    if s_x == e_x and s_y == e_y:
        res = 1
        return

    visited[s_x][s_y] = 1  # 방문체크
    for i in range(4):  # 4방향 체크
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위체크. 범위 벗어나면 패쓰
            continue
        if miro[nx][ny] == 1:  # 벽인지 체크. 벽이면 패쓰
            continue
        if not visited[nx][ny]:  # 방문 안 했으면 방문하고 계속 재귀
            visited[nx][ny] = 1
            dfs(nx, ny)  # 재귀호출


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]  # 0:통로, 1:벽, 2:출발, 3:도착

    # 출발점과 도착점을 먼저 구한 후, 이동하면서 도착점과 같아지면 res = 1 리턴하는 함수로 풀 예정
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                s_x, s_y = i, j
            if miro[i][j] == 3:
                e_x, e_y = i, j
    visited = [[0] * N for _ in range(N)]  # 미로의 크기만큼 방문체크 배열 만듦
    res = 0
    dfs(s_x, s_y)

    print("#{} {}".format(tc, res))
```

<br><br><br>

# 4880. 토너먼트 카드게임

~~이 문제는 문제 자체도 이해하지 못했음......ㅋ 🙄 환.장.~~

-> 0305 추가

문제에서 하라는데로 인덱스로 접근한 후, 그룹을 두개로 나누면 되는 문제였다 ! 

처음 문제를 봤을 때 그림이 거꾸로 되어있어서(작은그룹-> 큰 그룹) 이해가 안갔는데, 밑에서 부터 보면 되는 것이었다. 

문제에서 친절히 인덱스도 다 명시해줘서 인덱스로 접근하여 그룹을 두개로 나눈 후, 가위바위보 서열에 맞게끔 winner를 리턴하는 함수를 만들었다.

<br>

### 코드

```python
# 같은 카드인 경우 인덱스가 작은 애가 winner
def win(first, second):
    # 1:가위, 2: 바위, 3:보 -> 1<2 / 2<3 / 3<1
    winner = first
    if a[first] == 1 and a[second] == 2:
        winner = second
    if a[first] == 2 and a[second] == 3:
        winner = second
    if a[first] == 3 and a[second] == 1:
        winner = second
    return winner


# 리스트를 두개로 분류하는 작업이 필요함. 도대체 어케 분리? -> 인덱스로 접근
def divide(s, e):  # s:처음 인덱스, e: 끝 인덱스
    if s == e:  # 요소가 하나일때
        return s
    else:
        first = divide(s, (s+e)//2)
        second = divide((s+e)//2 +1, e)
        return win(first, second)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    ans = divide(0, N-1) + 1
    print("#{} {}".format(tc, ans))
```

<br><br><br>

# 4881. 배열 최소 합

와.. 이 문제 진짜진짜 어려웠다

💧  21~29번째 줄이 아주아주 난관이었다. **False를 다시 써주고 sub_sum 값을 빼주고 하는게 어려웠음.** 스택의 구조가 아주 명확히 나타나는 문제였다.

💧 처음에 13번째 줄에서 `r == N-1` 로 썼는데 결과값이 다르게 나와 N으로 수정하니 맞게 나왔다.  N x N 배열일 때 인덱스가 `0, 1, 2, .. N-1` 어서 N-1로 체크했더니 틀렸다. 왜그런가 생각해보니  함수 내에서 다음 행까지 호출하기 때문에  인덱스가 하나 증가한다. 따라서 행 인덱스가 N이 될때까지 체크한 후 리턴시켜주어야 한다.

<br>

### 코드

```python
# row 마다 돌면서 col의 경우를 따지는 함수
def check_sum(r):
    global sub_sum, res  # 계속해서 재귀처럼 함수 써야 되서 전역변수 갖고와서 쓰는 거임

    # 기존 결과값이 더 작으면 그냥 리턴
    if res < sub_sum:
        return

    # 배열의 크기랑 똑같아지면 함수 끝내기
    if r == N:
        # 기존 결과 보다 작다면 res 갱신
        if sub_sum < res:
            res = sub_sum
        # 아니면 그냥 리턴
        return

    # 열을 순회하며 방문 안했으면 방문하고, 값 더해줌
    for c in range(N):
        if not visited[c]:
            visited[c] = True
            sub_sum += a[r][c]
            # 다음 row 에 대해서 계속 체크, 재귀적으로 마지막 row 까지 호출
            check_sum(r+1)
            # 마지막까지 호출 다 끝나면 visited 랑 sub_sum 다시 초기화 시켜줘야 함. 그래야 모든 경우 다 따져보면서 체킹할 수 있음
            visited[c] = False
            sub_sum -= a[r][c]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N  # 몇번째 열을 방문한건지 체킹할 리스트
    sub_sum = 0  # 경우의 수 마다 합 비교해줄 변수
    res = 100  # :: N <= 10
    check_sum(0)  # 0번째 row 부터 찾기 시작

    print("#{} {}".format(tc, res))
```

- `N <= 10`이어서 배열의 합이 최대 100 미만이기 때문에 res 값을 100으로 설정해주었다.

- 행을 순회하면서 체킹을 해줄건데, 이미 방문한 열은 또 방문하면  안되기 때문에 몇번째 열을 방문했는지 체킹할 visited 라는 리스트를 만들었다. 

  처음에는 전부 False로 할당할 후, `check_sum()` 이라는 함수를 돌며, 방문했으면 True로 값을 바꾸면서 열 인덱스가 중복되지 않도록 sub_sum을 구하는 코드를 작성했다.

- 26번째 줄에서 다음 row에 대해 재귀적으로 계속 호출한 후, res 값을 갱신하고, 모든 과정이 끝나면 밑에 남은 28, 29번째줄 코드를 실행하며 다시 visited와 sub_sum을 초기화시켜 모든 경우의 수를 따져주었다.

  이 과정이 가장 어렵고 까다롭고 엄청 헷갈렸다. 디버깅을 해도 혼란스러워서 그림을 하나하나 그려가며 경우를 따져주었다 ㅠㅠ

<br><br><br>

## 두줄평

stack 어떡하지 큰일났다 😱

머리 터져 ~~~~ 😲

