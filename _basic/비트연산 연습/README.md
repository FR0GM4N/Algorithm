# 1. 비트연산

![image-20210412164020378](README.assets/image-20210412164020378.png)

![image-20210413185945992](README.assets/image-20210413185945992.png)



<br>

## 1-1. 예제 1

![image-20210412164058705](README.assets/image-20210412164058705.png)

<br>

## 1-2. 연습문제 1

![image-20210412164111984](README.assets/image-20210412164111984.png)

<br>

## 1-3. 예제 2

![image-20210412164124993](README.assets/image-20210412164124993.png)



<br>

## 엔디안 (Endianness)

![image-20210412164136430](README.assets/image-20210412164136430.png)

<br>

## 1-4. 예제 3

![image-20210412164152273](README.assets/image-20210412164152273.png)

<br>

## 1-5. 예제 4

![image-20210412164159140](README.assets/image-20210412164159140.png)

<br>

## 1-6. 예제 5 

![image-20210412164211649](README.assets/image-20210412164211649.png)



<br><br>

---

# 2. 진수

![image-20210413093411523](README.assets/image-20210413093411523.png)

![image-20210412164318710](README.assets/image-20210412164318710.png)



## 음수 표현 방법

![image-20210413190355851](README.assets/image-20210413190355851.png)

<br>

if, 4비트

- 맨 앞 1비트-> 부호
- 나머지 3비트-> 이진수 숫자표현 => `2³-1 = 7` -> 범위: `-8 ~ 7`

<br>

**ex.**  00000001 <- `1`

~(1) : 11111110 <- 1의 보수

+1 => 11111111 <- `-1`  (2의 보수) : 현재 비트보다 1자리 많은(i.e. 100000000) 2의 제곱수와의 차이

<br>

**ex.** 1010 -> `-6`

1의 보수 (0,1 반대로) -> 0101

2의 보수 (1의 보수에 +1) -> 0110 => `6`

<br>

## 2-2. 연습문제 2

![image-20210412164240019](README.assets/image-20210412164240019.png)

```
10진수로 변환하려면 2진수로 먼저 변환 후, 10진수로 변환해야함.
0F를 2진수로 바꾸면 00001111 -> 그 다음에 7개씩 끊은 다음 10진수로 변환
```

<br><br>

---

# 3. 실수

![image-20210412164425118](README.assets/image-20210412164425118.png)



![image-20210412164451803](README.assets/image-20210412164451803.png)

![image-20210412164501006](README.assets/image-20210412164501006.png)

![image-20210412164508129](README.assets/image-20210412164508129.png)

![image-20210412164526528](README.assets/image-20210412164526528.png)

![image-20210412164533810](README.assets/image-20210412164533810.png)

![image-20210412164541415](README.assets/image-20210412164541415.png)

![image-20210412164550392](README.assets/image-20210412164550392.png)

<br>

## 3-1. 연습문제 3

![image-20210412164559105](README.assets/image-20210412164559105.png)

<br>

---

<br>

# cf. 복잡도 분석

![image-20210412164730857](README.assets/image-20210412164730857.png)

<br>

## 시간복잡도

![image-20210413185653667](README.assets/image-20210413185653667.png)

<br>

![image-20210413191323243](README.assets/image-20210413191323243.png)

<br>

![image-20210413191407915](README.assets/image-20210413191407915.png)

- 출처 :  https://www.bigocheatsheet.com/

<br>



