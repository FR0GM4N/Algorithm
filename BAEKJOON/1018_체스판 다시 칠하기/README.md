# 1018번 체스판 다시 칠하기

[문제 보러가기](https://www.acmicpc.net/problem/1018)

🚩 `브루트포스`

<br>

## 🅰 설계

- W로 시작하는 경우

WBWBWBWB  -> W로 시작했는데 첫번째칸이 W가 아니면 다시 칠해야함

BWBWBWBW  -> W로 시작했는데 두번째칸이 B가 아니면 다시 칠해야함



- B로 시작하는 경우

BWBWBWBW  -> B로 시작했는데 첫번째칸이 B가 아니면 다시 칠해야함

WBWBWBWB  -> B로 시작했는데 두번째칸이 W가 아니면 다시 칠해야함



<br>

=> WBWB or BWBW 번갈아가면서 나오니까 **행+열 인덱스의 나머지**로 생각 ! (i.e. 0101 or 1010)

| 행/열 | 0    | 1    | 2    | 3    |
| ----- | ---- | ---- | ---- | ---- |
| **0** | 0    | 1    | 0    | 1    |
| **1** | 1    | 0    | 1    | 0    |
| **2** | 0    | 1    | 0    | 1    |
| **3** | 1    | 0    | 1    | 0    |



<br>

## 🅱 최종 코드



```python
N, M = map(int, input().split())  # N:행 M:열
a = [list(input()) for _ in range(N)]

res = []
# 8x8 체스판 탐색
for i in range(N-7):
    for j in range(M-7):
        w_cnt, b_cnt = 0, 0  # w_cnt:W로 시작할 때 다시 칠해야하는 개수, b_cnt:B로 시작할 때 다시 칠해야하는 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                # wbwb... or bwbw... 번갈아가면서 나오니까 행+열 인덱스의 나머지로 생각 (i.e. 0101... or 1010...)
                if (k+l) % 2 == 0:
                    if a[k][l] != 'W':  # W로 시작했는데 첫번째칸이 W가 아니면 다시 칠해야함
                        w_cnt += 1
                    if a[k][l] != 'B':
                        b_cnt += 1
                else:
                    if a[k][l] != 'B':  # W로 시작했는데 두번째칸이 B가 아니면 다시 칠해야함
                        w_cnt += 1
                    if a[k][l] != 'W':
                        b_cnt += 1
        res.append(w_cnt)
        res.append(b_cnt)
print(min(res))

```

<br>

## ✅ 후기

처음에 이걸 어케 풀어야하나 어려웠다.

**나머지** 접근을 기억하자

