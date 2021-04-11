# 2630번 색종이 만들기

[문제 보러가기](https://www.acmicpc.net/problem/2630)

🚩 `분할정복`

<br>

## 🅰 설계

### 첫 코드 (Fail)

N이 1이 될때까지 쪼개면서 체킹하자고 생각.

그럼 어케 쪼갤 것이냐? -> 시작점의 좌표를 구해서 종이크기만큼 range 설정한 후, 범위 체킹하자.

반복문 돌리면서 체킹하다 색깔 전부 같으면  거기는 stop하고 white or blue 개수에 카운팅. _(경우의 수 줄이기)_

계속 체킹하기 위해 재귀함수로 구성함.

**문제점** : 

- 아웃풋이 다르게 나옴. (15 13 나옴)

- 이유 : 10번째 줄에서 **`while N > 1:` 을 해줬기  때문**

  이미 재귀로 함수를 계속해서 호출하는데, 그 안에서 N == 1이 될때까지 반복문을 돌려서 틀린것이다.

```python
# 종이 쪼개는 함수
def divide(s_x,s_y,N):  # s_x:시작행좌표, s_y:시작열좌표, N:
    global cnt_w, cnt_b  # 전역변수 참조해서 값 변경할거라 global로 참조
    if N == 1 and a[s_x][s_y] == 0:  # 더이상 종이 안쪼개지면서 색종이 색이 0이면(white) 하얀색 개수에 카운팅하고 리턴. 전역변수 참조해서 값을 변경해줄 목적이라 따로 어떤 값을 리턴시키지 않음.
        cnt_w += 1
        return
    if N == 1 and a[s_x][s_y] == 1:  # 마찬가지로 blue의 경우
        cnt_b += 1
        return

    while N > 1:  # 📍 문제점. 이 부분만 삭제하면 코드가 정상적으로 작동된다.
        flag_w = 0  # 화이트가 나왔는지 체킹할 변수. 구역안에 화이트가 나왔으면 flag를 1로 체인지한다.
        flag_b = 0  # 블루가 나왔는지 체킹할 변수
        for i in range(s_x, s_x+N):  # 행 범위설정: s_x(시작점 행) ~ s_x+N(N크기의 구역의 마지막 점)
            for j in range(s_y, s_y+N):  # 열 범위설정
                if flag_w == 0 and a[i][j] == 0:  # 화이트가 아직 안나온 상태에서 화이트가 나왔으면 flag_w를 1로 변경(white 구역에 있다는 의미)
                    flag_w = 1
                elif flag_b == 0 and a[i][j] == 1:  # 블루가 안나온 상태에서 나오면 역시 상태 체인지
                    flag_b = 1
                    
        N //= 2  # N의 크기를 반씩 나눠줘야 다음 사이클이 진행됨
        if flag_w == 1 and flag_b == 0:  # 전부 하얀색인 경우 -> 하얀색 카운트하고 끝
            cnt_w += 1
        if flag_w == 0 and flag_b == 1:  # 전부 파랑색인 경우 -> 파랑색 카운트하고 끝
            cnt_b += 1
        if flag_w == 1 and flag_b == 1:  # 둘다 나오면 재귀함수 호출하여 쪼개기
            divide(s_x, s_y, N)
            divide(s_x + N, s_y, N)
            divide(s_x, s_y + N, N)
            divide(s_x + N, s_y + N, N)

            

# 본 프로그램 시작
N = int(input())  # N:종이크기
a = [list(map(int, input().split())) for _ in range(N)]  # 색종이 2차원 배열로 받음. (0:white, 1:blue)
cnt_w, cnt_b = 0, 0  # 하얀색 개수, 파랭이 개수
divide(0, 0, N)  # 함수 호출
print(cnt_w, cnt_b)  # 답을 출력형식과 다르게 했는데 패쓰 됐음.. 신기.. 답만 맞게나옴 패쓰되나봄
```

<br><br>

## 🅱 최종 코드

첫 코드와 전부 동일하되, 10번째 줄의 ` while N > 1:` 을 삭제함

```python
def divide(s_x,s_y,N):
    global cnt_w, cnt_b
    if N == 1 and a[s_x][s_y] == 0:
        cnt_w += 1
        return
    if N == 1 and a[s_x][s_y] == 1:
        cnt_b += 1
        return

    flag_w = 0
    flag_b = 0
    for i in range(s_x, s_x+N):
        for j in range(s_y, s_y+N):
            if flag_w == 0 and a[i][j] == 0:
                flag_w = 1
            elif flag_b == 0 and a[i][j] == 1:
                flag_b = 1
    N //= 2
    if flag_w == 1 and flag_b == 0:  # 전부 하얀색인 경우 -> 하얀색 카운트하고 끝
        cnt_w += 1
    if flag_w == 0 and flag_b == 1:  # 전부 파랑색인 경우 -> 파랑색 카운트하고 끝
        cnt_b += 1
    if flag_w == 1 and flag_b == 1:  # 둘다 나오면 쪼개기
        divide(s_x, s_y, N)
        divide(s_x + N, s_y, N)
        divide(s_x, s_y + N, N)
        divide(s_x + N, s_y + N, N)



N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
cnt_w, cnt_b = 0, 0
divide(0, 0, N)
print(cnt_w, cnt_b)
```

<br><br>

## ✅ 후기

### 어려웠던 점

while... 맨날 얘때문에 틀린다.... 😲