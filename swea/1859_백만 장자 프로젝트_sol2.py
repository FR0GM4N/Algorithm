# 더 간단하게

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    revenue = 0

    # price 리스트의 뒤에서부터 최대값 체킹할거라서 max_val 을 맨 뒤의 값으로 잡아줌
    max_val = price[-1]
    for i in range(N - 1, -1, -1):
        # max_val 보다 크거나 같으면 그 값으로 체인지
        if price[i] >= max_val:
            max_val = price[i]
        revenue += max_val - price[i]

    print("#{} {}".format(tc, revenue))