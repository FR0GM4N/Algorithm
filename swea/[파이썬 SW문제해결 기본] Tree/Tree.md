# 📎Tree

<br>

## 5174. subtree

### sol

```python
T = int(input())

def size(root):
    global cnt
    if tree[root][0]:
        cnt += 1
        size(tree[root][0])
    if tree[root][1]:
        cnt += 1
        size(tree[root][1])

for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선개수, root
    tmp = list(map(int, input().split()))  # 부모-자식
    tree = [[0] * 3 for _ in range(E+2)]  # [왼쪽자식, 오른쪽자식, 부모]
    for i in range(E):
        # [왼쪽자식, 오른쪽자식, 부모노드]
        parent, child = tmp[i * 2], tmp[i * 2 + 1]
        tree[child][2] = parent
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    cnt = 1
    size(N)
    print("#{} {}".format(tc, cnt)
```



```python
# print(tree)

[[0, 0, 0], [6, 0, 2], [1, 5, 0], [0, 0, 5], [0, 0, 6], [3, 0, 2], [4, 0, 1]]
[[0, 0, 0], [0, 0, 4], [6, 0, 0], [0, 0, 5], [1, 0, 6], [3, 0, 6], [4, 5, 2]]
[[0, 0, 0], [0, 0, 8], [0, 0, 5], [0, 0, 5], [11, 0, 7], [3, 2, 9], [9, 0, 7], [6, 4, 0], [1, 10, 11], [5, 0, 6], [0, 0, 8], [8, 0, 4]]
```

<br><br>

## 5176. 이진탐색

### sol

```python
T = int(input())

def in_order(i):
    global cnt
    if i <= N:
        in_order(2*i)
        tree[i] = cnt
        cnt += 1
        in_order(2*i+1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    cnt = 1
    in_order(1)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))
```



```python
# print(tree)

[0, 4, 2, 6, 1, 3, 5]
[0, 5, 3, 7, 2, 4, 6, 8, 1]
[0, 8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
```

<br><br>

## 5177. 이진힙

### fail (9개의 테스트케이스 중 3개가 맞았습니다.)

틀린이유 : `change` 함수에서 자식-부모 비교를 한번만 해줌.

만약 `5-3-1` 의 경우라면 함수 1번 시행시 → `3-5-1` , 함수 2번 시행시 → `3-1-5`  가 되어 전체적으로 봤을 때 `부모<자식` 이 항상 성립하지 않음.

=> 재귀로 `부모<자식` 이 될 때까지 계속해서 돌려야함 -> how? 자식노드를 기준으로 돌리기 (기존의 change함수는 부모노드 기준으로 돌렸음)

```python
T = int(input())

def change():
    for i in range(1, N + 1):
        if tree[tree[i][1]][3] != 0 and tree[i][3] > tree[tree[i][1]][3]:
            tree[i][3], tree[tree[i][1]][3] = tree[tree[i][1]][3], tree[i][3]
        if tree[tree[i][2]][3] != 0 and tree[i][3] > tree[tree[i][2]][3]:
            tree[i][3], tree[tree[i][2]][3] = tree[tree[i][2]][3], tree[i][3]

def sum_root(N):
    global ans
    if tree[N][0] == 0:
        return
    ans += tree[tree[N][0]][3]
    sum_root(tree[N][0])


for tc in range(1, T+1):
    N = int(input())
    tmp = list(map(int, input().split()))
    tree = [[0]*4 for _ in range(N+1)]  # [부모노드,왼자,오자,value]

    for i in range(1, N+1):
        tree[i][3] = tmp[i-1]
        tree[i][0] = i // 2
        if 2 * i <= N:
            tree[i][1] = 2 * i
            tree[i][2] = 2 * i + 1
    if N % 2 == 0:
        tree[N//2][2] = 0

    change()
    ans = 0
    sum_root(N)

    print("#{} {}".format(tc, ans))
```

<br>

### sol

```python
T = int(input())

# 자식노드 기준에서 체크. 부모가 작아질 때까지 계속 비교 -> 재귀
def change(node):
    parent = tree[node][0]
    if parent:
        if tree[parent][3] > tree[node][3]:
            tree[parent][3], tree[node][3] = tree[node][3], tree[parent][3]
    else:
        return
    change(parent)


def sum_root(N):
    global ans
    if tree[N][0] == 0:
        return
    ans += tree[tree[N][0]][3]
    sum_root(tree[N][0])


for tc in range(1, T+1):
    N = int(input())
    tmp = list(map(int, input().split()))
    tree = [[0]*4 for _ in range(N+1)]  # [부모노드,왼쪽자식,오른쪽자식,value]

    for i in range(1, N+1):
        tree[i][3] = tmp[i-1]
        tree[i][0] = i // 2
        if 2 * i <= N:
            tree[i][1] = 2 * i
            tree[i][2] = 2 * i + 1
            if 2*i+1 > N:
                tree[i][2] = 0

    for i in range(1, N+1):
        change(i)

    ans = 0
    sum_root(N)

    print("#{} {}".format(tc, ans))
```



```python
# print(tree)

[[0, 0, 0, 0], [0, 2, 3, 2], [1, 4, 5, 3], [1, 6, 0, 5], [2, 0, 0, 7], [2, 0, 0, 4], [3, 0, 0, 6]]
[[0, 0, 0, 0], [0, 2, 3, 1], [1, 4, 5, 3], [1, 6, 0, 4], [2, 0, 0, 16], [2, 0, 0, 23], [3, 0, 0, 12]]
[[0, 0, 0, 0], [0, 2, 3, 11], [1, 4, 5, 14], [1, 6, 7, 18], [2, 8, 0, 40], [2, 0, 0, 52], [3, 0, 0, 45], [3, 0, 0, 63], [4, 0, 0, 57]]
```

<br><br>

## 5178. 노드의 합

생각해보니 **후위순회(postorder)** 문제였음 . . . !

<br>

### fail (10개의 테스트케이스 중 9개가 맞았습니다. & 런타임에러)

틀린이유 :  중간 if문에서 `M % 2` 으로 써서 틀림. 리드노프의 개수로 따지지 말고 전체 노드의 개수로 따져야함

```python
T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N:노드개수, M:리드노프개수, L:출력할 노드번호
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v
        
    if M % 2:  # 홀수개인 경우
        tree.append(0)
        
    for i in range((N//2)*2, 1, -2):
        tree[i // 2] = tree[i] + tree[i + 1]

    print("#{} {}".format(tc, tree[L]))
```

<br>

### sol1 - 자식노드 세트로 더하기

```python
T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N:노드개수, M:리드노프개수, L:출력할 노드번호
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    # 방법1
    if N % 2 == 0:  # 노드의 개수가 짝수인경우
        tree.append(0)

    for i in range((N//2)*2, 1, -2):
        tree[i // 2] = tree[i] + tree[i + 1]

    print("#{} {}".format(tc, tree[L]))
```

<br>

### sol2 - 자식노드 하나씩 더하기

```python
T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N:노드개수, M:리드노프개수, L:출력할 노드번호
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    # 방법2
    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]

    print("#{} {}".format(tc, tree[L]))
```



```python
# print(tree)

[0, 6, 3, 3, 1, 2]
[0, 1516, 845, 671, 510, 335, 501, 170, 42, 468, 335]
[0, 5190, 2972, 2218, 1801, 1171, 428, 1790, 838, 963, 465, 706, 146, 282, 828, 962, 479, 359]
```




