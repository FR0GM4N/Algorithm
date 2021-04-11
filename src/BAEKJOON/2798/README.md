# 2798번 블랙잭

[문제 보러가기](https://www.acmicpc.net/problem/2798)

🚩 `브루트포스`

<br>

## 🅰 설계

모든 경우를 다 뽑아보기에는 경우의 수가 너무 많다고 생각했는데 완전탐색 문제였음..

처음에는 M과 최대한 가깝게하려면 `abs(M-3개합)`가 젤 작으면 된다고 생각해서 이렇게 풀려고 했으나 저 3개합을 고르려면 결국 다 따져봐야되서 그렇게 풀었다..

<br>

## 🅱 최종 코드

### sol1

```python
N, M = map(int, input().split())
card = list(map(int, input().split()))

res = 0  # 결과값 초기화
# for 문 돌면서 비교검사
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] <= M:
                res = max(res, card[i] + card[j] + card[k])
print(res)
```



### sol2 - itertools_combinations 사용 ver

```python
from itertools import combinations


N, M = map(int, input().split())
card_lst = list(map(int, input().split()))

max_value = 0  # 결과값 초기화
for card in combinations(card_lst, 3):
    # card = (5, 6, 7) <class 'tuple'>
    tmp = sum(card)
    if max_value < tmp <= M:
        max_value = tmp

print(max_value)
```



<br>

## ✅ 후기

N(3 ≤ N ≤ 100) & M(10 ≤ M ≤ 300,000) 이어서 시간초과 날 줄 알았는데 안났음

시간초과 어케 계산하는지 공부하자...