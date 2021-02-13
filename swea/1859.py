# swea_1859_백만 장자 프로젝트

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    revenue = 0

    # price 리스트의 뒤에서부터 최대값 체킹할거라서 max_val 을 맨 뒤의 값으로 잡아줌
    max_val = price[-1]
    max_idx = N - 1
    for i in range(max_idx - 1, -1, -1):
        count = 0
        cost = 0
        # max_val 보다 크거나 같으면 그 값으로 체인지
        if price[i] >= max_val:
            max_val = price[i]
            max_idx = i

        # max_val 보다 작으면 개수 카운팅
        else:
            count += 1
            cost += price[i]

        # 수익 = 판매가 - 원가
        #  = (max_val 보다 작은 값 개수 * max_val) - (max_val 보다 작은 값들의 원래 가격 합)
        revenue += count * max_val - cost
    print("#{} {}".format(tc, revenue))
