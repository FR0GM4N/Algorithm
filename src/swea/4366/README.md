# 4366. 정식이의 은행업무

> 2진수와 3진수가 주어졌을 때 한자리씩만 바꾸어 겹치는 숫자를 찾아내는 문제

<br>

### ⭐ tip 1  -> sol3

진수의 크기가 곧 자리수이기 때문에  각 자리를 돌며 이전 숫자에 자리수(진수크기)를 곱하며 더해주면 된다.

```python
# 2진수로 바꾸기
num = 0
bit = '1110'
for x in bit:
    num = num*2 + int(x)
print(num)  #=> 14


# 3진수로 바꾸기
num = 0
bit = '212'
for x in bit:
    num = num*3 + int(x)
print(num)  #=> 23


# 10진수로 바꾸기
num = 0
bit = '12345'
for x in bit:
    num = num*10 + int(x)
print(num)  #=> 12345
```

<br>

### ⭐ tip 2  -> sol2

파이썬의 성질을 이용한다. (자세한 내용은 밑에 작성함)

```python
# 2진수로 바꾸기
print(int('1110', 2))  #=> 14


# 3진수로 바꾸기
print(int('212', 3))   #=> 23
```

<br><br>

## 풀이 1

파이썬 진수의 성질을 몰라 무식한 방법으로 풀었다 . . ㅋ

2진수와 3진수 input data를 리스트형으로 받고, 원본리스트를 바꾸면 안되기에 카피리스트를 만들면서 하나하나 바꿀 수 있는 모든 경우를 바꾸어주었다.

그 후 진수표현된 비트를 숫자로 바꾼다음, 중복을 체크해주기 위해 set에 넣고 교집합을 결과값에 넣어주었다.

```python
def find_num2(nums):
    tmp = []
    for i in range(len(nums)):
        if nums[i]:  # 1이면 0으로 바꿔봄
            a = nums[:]
            a[i] = 0
            tmp.append(a)
        else:  # 0이면 1로 바꿔봄
            a = nums[:]
            a[i] = 1
            tmp.append(a)

    for ele in tmp:  # tmp = [[0, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 1, 1]]
        num_10 = 0
        for i in range(len(nums)):  # nums = [1, 0, 1, 0]
            num_10 += (2 ** (len(nums) - 1 - i)) * ele[i]
        set_2.add(num_10)


def find_num3(nums):
    tmp = []
    for i in range(len(nums)):
        if nums[i] == 0:  # 0 -> 1, 2
            a = nums[:]
            a[i] = 1
            tmp.append(a)
            b = nums[:]
            b[i] = 2
            tmp.append(b)
        if nums[i] == 1:  # 1 -> 0, 2
            a = nums[:]
            a[i] = 0
            tmp.append(a)
            b = nums[:]
            b[i] = 2
            tmp.append(b)
        if nums[i] == 2:  # 2 -> 0, 1
            a = nums[:]
            a[i] = 0
            tmp.append(a)
            b = nums[:]
            b[i] = 1
            tmp.append(b)

    for ele in tmp:
        num_10 = 0
        for i in range(len(nums)):
            num_10 += (3 ** (len(nums) - 1 - i)) * ele[i]
        set_3.add(num_10)


T = int(input())
for tc in range(1, T+1):
    num_2 = list(map(int, input()))  # 2진수 input_data
    num_3 = list(map(int, input()))  # 3진수 input_data
    set_2 = set()
    set_3 = set()

    find_num2(num_2)
    find_num3(num_3)

    res = set_2 & set_3
    print("#{} {}".format(tc, *res))
```



<br>

## 풀이 2

`tip 2` 를 사용하여 해결

```python
T = int(input())

for tc in range(1, T + 1):
    b = input()
    t = input()

    b_lst = []
    for i in range(len(b)):
        if b[i] == '1':
            tmp = '0'
        else:
            tmp = '1'
        b_lst.append(int(b[:i] + tmp + b[i+1:], 2))

    for i in range(len(t)):
        for k in range(3):
            if t[i] != str(k):
                ter = int(t[:i] + str(k) + t[i+1:], 3)
                if ter in b_lst:
                    res = ter

    print("#{} {}".format(tc, res))
```



<br>

## 풀이 3

`tip 1` 을 사용하여 해결

```python
def f(b,t):
    # 2진수로 풀어 쓸 경우(1-3줄).   ###cf. 내장함수로 하면; num = int(b,2)
    num = 0
    for x in b:
        num = num*2 + int(x)
        
    binary = []
    for i in range(len(b)):
        binary.append(num^(1<<i))  # 2진수의 1비트씩을 바꿔서 저장 (XOR 연산 이용)

    for i in range(len(t)):  # 3진수에서 다른 두 수로 바꿔볼 자리
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if i != j:
                num1 = num1*3 + int(t[j])
                num2 = num2*3 + int(t[j])
            else:
                num1 = num1*3 + (int(t[j])+1)%3  # 0->1. 1->2, 2->0
                num2 = num2*3 + (int(t[j])+2)%3  # 0->2, 1->0, 2->1
        if num1 in binary:
            return num1
        if num2 in binary:
            return num2



T = int(input())
for tc in range(1, T+1):
    b = input()
    t = input()
    res = f(b,t)
    print('#{} {}'.format(tc, res))
```

<br><br>

![193508](https://user-images.githubusercontent.com/77573938/115110475-99e94d00-9fb6-11eb-862a-e667fdd0d85f.png)

<br><br>

---

<br>

# 🔍 파이썬 진수에 관하여

<br>

## 1. 2진수, 8진수, 16진수로 나타내기

파이썬에서는 기본적으로 10진수 형태로 숫자를 표현하기 때문에 다른 진수의 형태로 숫자를 표현하려면 숫자 앞에 접두어를 붙여줘야 한다.

- 2진수: `0b` 
- 8진수: `0o` 
- 16진수: `0x`

```python
# 42를 2진수, 8진수, 16진수로 나타내기

0b101010  # 2진수
0o52      # 8진수
0x2a      # 16진수
```

<br>

## 2. `bin()`, `oct()`, `hex()` 내장함수 사용

`bin()`, `oct()`, `hex()` 내장 함수를 통해 숫자를 각 진수의 형태의 문자열로 변환할 수 있다.

```python
bin(42)  #=> '0b101010'
oct(42)  #=> '0o52'
hex(42)  #=> '0x2a'
```

함수의 인자로 숫자를 넘길 때, 10진수를 사용하든 2진수를 사용하든 결국 동일한 숫자 값을 다른 진수의 형태로 표현한 것뿐이기 때문에 결과는 동일해야 한다.

```python
bin(0b101010)  #=> '0b101010'
oct(0b101010)  #=>  '0o52'
hex(0b101010)  #=>  '0x2a'
str(0b101010)  #=>  '42'
```

<br>

## 3. 비트 연산으로 표현된 문자열을 다시 정수로 바꾸기

```python
>>> int('0b101010', 2)
42
>>> int('0o52', 8)
42
>>> int('0x2a', 16)
42
>>> int('42', 10)
42
>>> int('42')  # 2번째 인자의 디폴트값은 10 -> 10진수로 출력됨
42
```

<br>

## 4. `format()` 내장함수

`format()` 내장 함수를 이용하면 숫자를 다른 진수의 문자열로 바꿀 때 접두어를 제외할 수 있다.

```python
>>> format(42, 'b')  # 2진수
'101010'
>>> format(42, 'o')  # 8진수
'52'
>>> format(42, 'x')  # 16진수
'2a'
>>> format(42, 'X')
'2A'
>>> format(42, 'd')
'42'
```

두번째 인자 앞에 `#`를 붙이면 접두어를 포함시킬 수 있다.

```python
>>> format(42, '#b')
'0b101010'
>>> format(42, '#o')
'0o52'
>>> format(42, '#x')
'0x2a'
>>> format(42, '#X')
'0X2A'
```

```python
print("int: {0:d}, bin: {0:b}, oct: {0:o}, hex: {0:x}".format(42))
#=> int: 42, bin: 101010, oct: 52, hex: 2a
```

<br>

- 출처 : https://www.daleseo.com/python-int-bases/