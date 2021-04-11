# 1003번 피보나치 함수

[문제 보러가기](https://www.acmicpc.net/problem/1003)

🚩 `다이나믹 프로그래밍`, `DP`

<br>

## 🅰 설계

1. TypeError (fail)

피보나치 수열 코드와 동일하게 짜되, n == 0 or 1 인 경우 0과 1의 호출횟수를 카운트하도록 함수를 구성했다.

```python
# 피보나치 함수
def f(n):
    global cnt_0, cnt_1
    if n == 0:  # n이 0이면 0호출횟수 1 증가
        cnt_0 += 1
        return
    elif n == 1:  # n이 1이면 1호출횟수 1 증가
        cnt_1 += 1
        return
    else:  # 0,1이 아니라면 재귀 호출
        return f(n-1) + f(n-2)


T = int(input())
for tc in range(T):
    N = int(input())
    cnt_0, cnt_1 = 0, 0  # cnt_0: 0호출횟수, cnt_1: 1호출횟수
    f(N)
    print("{} {}".format(cnt_0, cnt_1))
```

그런데,  input 값이 0,1 외의 다른 정수이면 **NoneType 끼리의 `+` 연산을 support 하지 않는다는 에러가 났다.**

```
  File "1003_피보나치 함수/sol1.py", line 21, in <module>
    f(N)
  File "1003_피보나치 함수/sol1.py", line 14, in f
    return f(n-1) + f(n-2)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
```

cnt_0, cnt_1을 global로 참조해서 그 값만 변경시키려고 했는데 `n == 0 or 1` 인 경우에는 리턴값을 명시하지 않고, else 문에서는 return 값을 명시해서 에러가 난 것 같다.

<br>

2. 시간초과 (fail)

`n == 0 or 1` 인 경우에도 리턴을 시키니 output은 맞게 나왔지만 **시간초과**가 떴다..

```python
# 피보나치 함수
def f(n):
    global cnt_0, cnt_1
    if n == 0:  # n이 0이면 0호출횟수 1 증가
        cnt_0 += 1
        return cnt_0, cnt_1
    elif n == 1:  # n이 1이면 1호출횟수 1 증가
        cnt_1 += 1
        return cnt_0, cnt_1
    else:
        return f(n-1) + f(n-2)


T = int(input())
for tc in range(T):
    N = int(input())
    cnt_0, cnt_1 = 0, 0
    f(N)
    print("{} {}".format(cnt_0, cnt_1))
```

<br>

3. success 😀

0호출횟수와 1호출횟수를 리스트로 만들어 피보나치 수열처럼 `n-1`, `n-2`의 호출횟수를 더하는 방식으로 코드를 짰다.

`n = 8`인 경우, `cnt_0 = [1, 0, 1, 1, 2, 3, 5, 8]`, `cnt_1 = [0, 1, 1, 2, 3, 5, 8, 13]` 가 되어 n번째 원소를 출력하면 된다.

<br>

## 🅱 최종 코드

```python
T = int(input())
for tc in range(T):
    N = int(input())
    cnt_0 = [1, 0]  # 0 호출횟수 기록하는 리스트
    cnt_1 = [0, 1]  # 1 호출횟수 기록하는 리스트

    for i in range(2, N + 1):
        cnt_0.append(cnt_0[i - 1] + cnt_0[i - 2])  # 이전 두 단계의 0 호출횟수를 더함
        cnt_1.append(cnt_1[i - 1] + cnt_1[i - 2])

    print("{} {}".format(cnt_0[N], cnt_1[N]))
```

<br>

## ✅ 후기

### 새롭게 알게 된 점

- 재귀함수의 return 호출
- TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

### 어려웠던 점

- 시 ! 간 ! 초 ! 과 !
- 시간초과 도대체 어케 예상하고 푸는거지.... 맨날 시간초과 뜨고 나서야 코드 다시 짠다 ^^