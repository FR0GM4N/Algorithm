# 내가 처음에 푼 풀이인데... 참 길다...
# 애초에 prime을 리스트로 만들어서 반복문으로 돌리면 될 것을...

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 변수초기화
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    # 포인트는 소수로 나누었을 때 나머지가 0이냐 아니냐?!
    # 나머지가 0 이라는건 나누어 떨어진다는거고, 더 이상 안 나누어 떨어질 때까지 그 횟수를 카운팅하면 됨
    while N % 2 == 0:
        a += 1
        N //= 2
    while N % 3 == 0:
        b += 1
        N //= 3
    while N % 5 == 0:
        c += 1
        N //= 5
    while N % 7 == 0:
        d += 1
        N //= 7
    while N % 11 == 0:
        e += 1
        N //= 11

    print("#{} {} {} {} {} {}".format(tc, a, b, c, d, e))

