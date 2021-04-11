# 1976_시각 덧셈

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    times = list(map(int, input().split()))
    hour = times[0] + times[2]  # 시
    minute = times[1] + times[3]  # 분
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12

    print("#{} {} {}".format(tc, hour, minute))


# 다른 방법
T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    carry = m // 60  # 올림수
    m = m % 60  # 분에 대한 나머지
    if h % 12 == 0 and h > 0:
        h = 12
    else:
        h %= 12
    print("#{} {} {}".format(tc, h, m))