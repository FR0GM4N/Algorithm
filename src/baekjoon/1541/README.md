# 1541번 잃어버린 괄호

[문제 보러가기](https://www.acmicpc.net/problem/1541)

🚩 `수학`, `그리디 알고리즘`, `문자열`, `파싱`

<br>

## 🅰 설계

`-` 기준으로 쪼개고 리스트의 첫번째 요소만 더하고 그 이후 요소는 다 빼면 된다.

ex. `50+32-48+72-145+32-5-3` => `50+32-(48+72)-(145+32)-5-3`

1. `-` 기준으로 쪼갠다 -> `['50+32', '48+72', '145+32', '5', '3']`
2. 첫번째 요소는 `+` 기준으로 쪼갠 후 더한다 -> `50+32`
3. 나머지 요소는 `+` 기준으로 쪼갠 후 다 뺀다 -> `-48-72-145-32-5-3`

<br>

## 🅱 최종 코드

```python
input_lst = input().split('-')

tmp = input_lst[0].split('+')
res = 0
for ele in tmp:
    res += int(ele)

for i in range(1, len(input_lst)):
    tmp = input_lst[i].split('+')
    for ele in tmp:
        res -= int(ele)

print(res)
```

<br>

## ✅ 후기

한번에 맞다니 예 ~✌

근데 왜 그리디인지 몰겠음