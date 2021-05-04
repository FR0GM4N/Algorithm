# 1931번 회의실 배정

[문제 보러가기](https://www.acmicpc.net/problem/1931)

🚩 `그리디`

<br>

## 🅰 설계

`[SWEA] 5202-화물 도크` 랑 똑같은 문제여서 같은 방식으로 풀었다.

시작-끝 시간을 리스트로 받은 다음, **끝나는 시간 순**으로 정렬한다. 

전회차의 끝 시간보다 다음회차 시작 시간이 같거나 크면 카운팅을 해주면 된다.

시간 때문에 `pop(0)` 을 안하고 `pop()` 을 하고 싶어서 내림차순으로 정렬했다.

```python
# sorted(a, key=lambda x: (-x[1], -x[0])) 정렬결과

[[12, 14], [2, 13], [8, 12], [8, 11], [6, 10], [5, 9], [3, 8], [5, 7], [0, 6], [3, 5], [1, 4]]
```



<br>

## 🅱 최종 코드

```python
import sys

N = int(sys.stdin.readline())  # 회의의 수
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a = sorted(a, key=lambda x: (-x[1], -x[0]))

cnt = 1
f1, f2 = a.pop()  # 뒤에서부터 체크
while a:
    n1, n2 = a.pop()
    if n1 >= f2:  # 다음 시작이 전회차 끝보다 크거나 같으면 갱신
        f1, f2 = n1, n2
        cnt += 1

print(cnt)
```

<br>

## ✅ 후기

### 새롭게 알게 된 점

(새롭게 알게 된 점이 아니라 옛날에 알아놓고 까먹은 것..😅)

⭐ `input()`은 매우 느리다. 입력이 **10만줄 이상** 되면 `stdin.readline`을 사용하는 것이 좋다.

- 참고 : [파이썬 입력 받기 (sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)

<br>

✔ 위가  `stdin.readline` 을 사용한 것이고, 아래가 `input()`을 사용한 것이다.

![221839](https://user-images.githubusercontent.com/77573938/116880911-919f3c00-ac5d-11eb-8203-10074de4ddbe.png)
