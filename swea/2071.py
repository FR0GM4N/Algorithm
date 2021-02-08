# 평균값 구하기

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0
    my_len = 0
    for number in numbers:
        total += number
        my_len += 1
    result = round(total / my_len)
    print('#{} {}'.format(tc, result))