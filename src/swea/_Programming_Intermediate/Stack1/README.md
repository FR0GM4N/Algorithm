# 📎 Stack1

[파이썬 SW 문제해결 기본 - Stack1](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg#)

🌟 주요 개념

- DFS
- Stack

<br>

---

<br>

# 4866. 괄호검사



### 첫 코드 (fail)

> 샘플 케이스는 맞았는데, 채점용 input 파일로 채점한 결과 fail 이었고 (10개의 테스트케이스 중 3개만 맞음)   **런타임에러** 가 발생했다.

찾아보니 런타임에러는 배열인덱스를 잘못 참조했을 때 등등의 이유로 발생한다고 한다.

🤔 ***아마 stack에서 pop해줄게 없는데 해줘서 인듯하다***

  - 런타임 에러가 발생하는 이유 ?

    1. 배열에 할당된 크기를 넘어서 접근했을 때
    2. 전역 배열의 크기가 메모리 제한을 초과할 때
    3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
    4. 0으로 나눌 때
    5. 라이브러리에서 예외를 발생시켰을 때
    6. 재귀 호출이 너무 깊어질 때
    7. 이미 해제된 메모리를 또 참조할 때
    8. 프로그램(main 함수)이 0이 아닌 수를 반환했을 때

```python
T = int(input())
for tc in range(1, T+1):
    S = input()  # 인풋 스트링
    stack = []
    for s in S:
        # 괄호인 애들만 체킹
        if s == '{' or s == '(':
            stack.append(s)
        elif s == '}':
            if stack[-1] == '{':
                stack.pop()
        elif s == ')':
            if stack[-1] == '(':
                stack.pop()

    # stack의 길이가 0이 아니면(i.e. 괄호가 남아있다는 의미)
    if len(stack):
        print("#{} 0".format(tc))
    # stack의 길이가 0인 경우(i.e. 짝이 잘 맞았다는 의미)
    else:
        print("#{} 1".format(tc))
```

<br>

<br>

### 두번째 코드 (pass)

> `stack.pop()` 을 해줄 때, 만약 stack이 비어있으면 pop을 해줄 수 없어서 런타임에러가 일어났던 것 같다. 아래처럼 코드를 수정해주니 pass 했다 ! 

```python
T = int(input())
for tc in range(1, T+1):
    S = input()  # 인풋 스트링
    stack = []
    for s in S:
        # 괄호인 애들만 체킹
        if s == '{' or s == '(':
            stack.append(s)
        elif s == '}' or s == ')':
            # stack이 비어있으면 추가하고 break. 어차피 뒤쪽을 봐야 이미 짝이 안맞기 때문
            if not stack:
                stack.append(s)
                break
            # s랑 stack의 마지막 요소랑 다른 괄호이면 역시 그냥 더해주고 break. 어차피 제대로 된 짝이 아니니까
            elif (s == '}' and stack[-1] != '{') or (s == ')' and stack[-1] != '('):
                stack.append(s)
                break
            # 위의 경우에 모두 해당 안되면(i.e. 제대로 짝이 맞는 경우)
            else:
                stack.pop()

    # stack의 길이가 0이 아니면(i.e. 괄호가 남아있다는 의미)
    if len(stack):
        print("#{} 0".format(tc))
    # stack의 길이가 0인 경우(i.e. 짝이 잘 맞았다는 의미)
    else:
        print("#{} 1".format(tc))
```

<br><br>

# 4869. 종이붙이기

point는 재귀함수로 접근하는 것이다

처음에 1번 사각형(10x20)이 3개인 경우는 어떻게 해석해야 고민했는데 가로의 길이만을 기준으로 나눠서 생각하면 재귀로 함수를 구성할 수 있었다.

![KakaoTalk_20210223_150323636](https://user-images.githubusercontent.com/77573938/113927804-e9967e80-9828-11eb-8184-6296a64dfdaf.jpg)

<br>

### 코드

```python
def paper_cut(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return paper_cut(n-1) + paper_cut(n-2) * 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = paper_cut(N//10)

    print("#{} {}".format(tc, ans))
```

<br><br>

# 4871. 그래프 경로

풀이가 4가지나 되므로 다시 한번 볼 것

1️⃣ DFS (stack) 풀이,  2️⃣ DFS-재귀 풀이 1,  3️⃣ DFS-재귀 풀이 2,  4️⃣ BFS (queue) 풀이

<br>

⭐ 노드-간선 input data 받는법

1. 인접행렬 방식

```python
edge_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    start_node, end_node = map(int, input().split())
    edge_matrix[start_node][end_node] = 1
```



2. 인접리스트 방식

```python
edge_list = [[] for _ in range(V+1)]
for _ in range(E):
    start_node, end_node = list(map(int, input().split()))
    edge_list[start_node].append(end_node)
```


<br><br>

# 4873. 반복문자 지우기

stack에 인풋스트링을 담아가면서 같은 문자가 연속해서 나오면 pop해서 없애주고 아니면 걍 패쓰한 후,

총 stack의 길이를 재면 끝!

```python
T = int(input())
for tc in range(1, T+1):
    S = input()  # 인풋스트링
    stack = []

    for i in range(len(S)):
        # 만약 stack이 비었거나, 스택의 마지막 값이 S와 다를 경우
        if not stack or stack[-1] != S[i]:
            stack.append(S[i])
        # stack에 값이 있고, 그 마지막 값이 인풋스트링과 일치하는 경우(i.e. 연속문자)
        elif stack and stack[-1] == S[i]:
            stack.pop()

    print("#{} {}".format(tc, len(stack)))
```

