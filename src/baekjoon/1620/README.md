# 1620번 나는야 포켓몬 마스터 이다솜

[문제 보러가기](https://www.acmicpc.net/problem/1620)

🚩 `자료구조`, `문자열`, `해시를 이용한 집합과 맵`

<br>

## 🅰 설계

### 1. 시간초과 (fail)

문제보자마자 존쉽이군 ㅋ 하고 바로 enumerate 으로 index랑 value 출력했는데 시간초과 났다.

```python
N, M = map(int, input().split())
lst = [input() for _ in range(N)]
quest = [input() for _ in range(M)]
for j in range(M):
    for i, v in enumerate(lst):
    # print(i, type(i), v, type(v))  # 0 <class 'int'> Bulbasaur <class 'str'>
        if quest[j] == v:
            print(i+1)
        if quest[j] == str(i+1):
            print(v)
```

혹시몰라 `sys.stdin.readline()` 도 추가해줬는데 이건 의미가 없었다.

문제를 다시보니 `1 ≤ N, M ≤ 100,000` 이어서 이중 for문을 도는 경우 

**최악의 경우, 10,000,000,000 백억번의 연산을 수행해서 시간초과가 난 것 같다.**

그럼 시간초과 안나려면 이중for문 안돌아야 하는데 for문 한번으로 인덱스랑 밸류를 어케 찾지?? 

⭐ 반복문 안돌면서 값 체킹하려면 -> ***dictionary*** !!!!!!!!!!!!!!!!

<br>

### 2. pass 😀

1. `quest = [input() for _ in range(M)]` 도 굳이 리스트로 받을 이유도 없었음.

   그냥 들어오는 족족 체킹하면 되는 것이다.

   

2. 딕셔너리 하나로 구성하고 싶었는데 `for _ in dic.keys():` 를 안돌고는 특정 key값만을 출력하기 어려워서 for문을 안돌고자 딕셔너리 2개로 구성했다.

   - `dic_n = {'25': 'Pikachu'}`  : 숫자접근으로 문자출력용
   - `dic_s = {'Pikachu': 25}`  : 문자접근으로 숫자출력용

   

3. **반복문으로 여러줄을 입력받는 문제이기 때문에 input()대신 sys.stdin.readline()을 사용했다.**

   ⭐ 이거 쓰려면 문자열 인풋받을때 `input().strip()` 이렇게 받아야한다. 

   뒤에 `\n`이 붙어 같이 저장되기 때문에 문자열 맨 앞과 맨 끝의 공백문자를 제거해야한다.

<br>

## 🅱 최종 코드

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_n = {}  # {'25': 'Pikachu'}. 숫자접근으로 문자출력용
dic_s = {}  # {'Pikachu': 25}. 문자접근으로 숫자출력용
for i in range(N):
    value = input().strip()
    dic_n[str(i+1)] = value
    dic_s[value] = i+1

for j in range(M):
    quest = input().strip()
    if quest.isdigit():  # 숫자면 문자출력
        print(dic_n[quest])
    if quest.isalpha():  # 문자면 숫자출력
        print(dic_s[quest])
```

<br>

## ✅ 후기

시간초과 환장

이제 for문 보면 무서워서 못 돌리겠음

시간초과의 저주에 걸린것 같다 😇

![image-20210409234909684](https://user-images.githubusercontent.com/77573938/114198893-cb4a9300-998e-11eb-9d14-7c556e417c5a.png)