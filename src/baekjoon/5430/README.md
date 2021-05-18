# 5430번 AC

[문제 보러가기](https://www.acmicpc.net/problem/5430)

🚩 `자료구조`, `문자열`, `파싱`, `덱`

<br>

## 🅰 설계

0 ≤ p ≤ 100,000 ,  0 ≤ n ≤ 100,000 이라 리터럴리 연산하면 시간초과 날거 같아서 규칙을 찾아봤다.

- R이 연속해서 홀수개면 뒤집고, 짝수개면 걍 그대로
- D는 연속한 개수만큼 삭제
- => R 홀짝 체킹할 flag변수 만들고, p연산 돌면서 앞에서부터 삭제할 개수랑 뒤에서부터 삭제할 개수 찾아서 삭제

<br>

- **input 배열 받기**

인풋배열을 받을 때 str형이어서 얘를 list형으로 바꾸기 위해 lstrip과 rstrip을 써서 `[]`를 없애고 `,` 를 기준으로 쪼개서 리스트로 만들었다. <- strip 안쓰고 `[1:-1]` 슬라이싱으로도 가능

처음부터 아래처럼 int형으로 바꾼 다음 리스트 형변환을 해주면, input이 `[]`인 경우 value에러가 난다. 

```python
num_lst = list(map(int, input().lstrip('[').rstrip(']').split(',')))
# ValueError: invalid literal for int() with base 10: ''
```

---

### 1. 실패

아니 왜 틀??????????????????? 시간초과도 아니고 런타임에러도 아니고 그냥 틀?????????????????????????

왜?????????

```python
def sol(p, n):
    flag = 0  # 짝
    delete = [0, 0]
    # 홀이면 뒤집(뒷 숫자 삭제), 짝이면 stay(앞 숫자 삭제)
    for s in p:
        if s == 'R' and flag == 0:
            flag = 1
        elif s == 'R' and flag == 1:
            flag = 0
        elif s == 'D' and flag == 0:
            delete[0] += 1
        elif s == 'D' and flag == 1:
            delete[1] += 1
        if sum(delete) >= n:
            return 'error'

    # 삭제하고 뒤집
    res = num_lst[delete[0]:len(num_lst) - delete[1]]
    if flag:
        res.reverse()
    return "["+",".join(res)+"]"


T = int(input())
for tc in range(1, T+1):
    p = input()  # 수행할 연산
    n = int(input())  # 배열에 들어있는 숫자 개수
    num_lst = input().lstrip('[').rstrip(']').split(',')

    print(sol(p, n))
```

---

### 2. PASS

아 진짜 나 바보 아닌가 😑 제발 문제 좀 똑바로 읽자 ~~~

빈 배열이 아니라 빈 배열일 때 D를 수행하면 error가 발생하는 것이다..

그래서 sol 함수 안에서 이때 등호를 넣으면 안된다 . . .

```python
        if sum(delete) > n:
            return 'error'
```

<br>

## ✅ 후기

- 문제를 꼼꼼히 읽자 제발제발. 맨날 문제 후루룩 읽고 틀린적이 많다

- 왜 문제 이름이 AC일까 RD로 하지

- 덱이 뭔가 했더니 deque라니;;; 여태 디큐라고 하고 살았네;;^^;;

### deque란 ? 양방향으로 넣고 뺄 수 있는 큐

![deque](https://user-images.githubusercontent.com/77573938/118680492-be487b80-b839-11eb-85a1-75b8cec2b2fa.png)

(그림 출처: https://ehclub.co.kr/1222)

나는 덱으로 안풀었는데 덱으로 풀 수도 있다. 알아둘것
