# 1764번 듣보잡

[문제 보러가기](https://www.acmicpc.net/problem/1764)

🚩 `자료구조`, `문자열`, `정렬`

<br>

## 🅰 설계

중복없이 처리하기 위해 듣도 못한 사람과 보도 못한 사람을 각각 set에 넣은 후, 교집합을 구해 정렬했다.

<br>

## 🅱 최종 코드

```python
N, M = map(int, input().split())

set_N = set()  # 듣도 못한 사람의 명단을 담을 set
set_M = set()  # 보도 못한 사람의 명단을 담을 set
for _ in range(N):
    set_N.add(input())
for _ in range(M):
    set_M.add(input())

res = sorted(list(set_N & set_M))  # 교집합을 구한다음 정렬

print(len(res))
for ele in res:
    print(ele)
```

<br>

## ✅ 후기

채점하는데 체감상 293872387274시간이 걸렸다... 파이썬.. 너무 느리다...