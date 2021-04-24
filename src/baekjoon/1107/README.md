# 1107번 리모컨

[문제 보러가기](https://www.acmicpc.net/problem/1107)

🚩 `브루트포스`

<br>

## 🅰 설계

- 모든 버튼이 고장난 경우 -> 100과의 차이만큼 이동

- 만약 99나 101처럼 100과 인접한 경우는 직접 버튼 누르는 것보다 `++` `--`로 이동하는게 유리

- 100이랑 차이가 버튼 눌렀을 때 보다 작은 경우 고려

1. **런타임에러(EOFError)** (fail)

답은 맞게 나오는데 시간이 진짜진짜진짜진짜 오래걸렸다.. 시간초과는 아닌데 뭐지

EOFError

```python
N = int(input())
M = int(input())
notworking = set(input().split())

remote = {str(x) for x in range(10)}
remote -= notworking  # 사용가능한 버튼 뽑아냄

min_cnt = abs(100-N)
for i in range(1000001):  # iterable 순회하기 위해 str형으로 체킹
    num = str(i)
    for j in range(len(num)):
        if num[j] not in remote:  # 버튼에 없으면 건너뜀
            break
        if j == len(num)-1:  # 마지막 자리수에서 체킹
            min_cnt = min(min_cnt, abs(N-i)+len(num))

print(min_cnt)
```



2. **런타임에러(NameError)** (fail)

 문제를 다시 보니 `고장난 버튼이 있는 경우에 셋째 줄에 고장난 버튼이 주어진다` 고 되어있어 `M != 0` 조건을 안 넣어줘서 에러가 난건가 싶어 넣어줬더니 이번에는 네임에러가 났다... ㅎr.......

```python
N = int(input())
M = int(input())

if M != 0:
    remote = {str(x) for x in range(10)}
    remote -= set(input().split())

min_cnt = abs(100-N)
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if num[j] not in remote:
            break
        if j == len(num)-1:
            min_cnt = min(min_cnt, abs(N-i)+len(num))

print(min_cnt)
```

<br>

## ✅ 후기

### 새롭게 알게 된 점

list보다 set이 조회가 빠르다.

### 어려웠던 점

- `+` `-` 다 가능하므로 범위가 1000000까지 인 것

-> 채널이 500,000 까지이기 때문에 최악의 경우는 100번에서 모든 번호를 누를 수 없고 `+` 버튼으로 500,000까지 가는 499,900번임.

-> 버튼을 약 1,000,000 번까지 누를수 있게 검사를 한다면 최악의 경우까지 전부 검사가 가능함.

- `abs(100-N)` 까지는 생각했는데 그 뒤에 어떻게 해야할지 어려웠다.
- **EOFError, NameError 나는 이유**

