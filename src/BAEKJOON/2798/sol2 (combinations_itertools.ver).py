import sys
sys.stdin = open("input.txt")
from itertools import combinations


N, M = map(int, input().split())
card_lst = list(map(int, input().split()))

max_value = 0  # 결과값 초기화
for card in combinations(card_lst, 3):
    # card = (5, 6, 7) <class 'tuple'>
    tmp = sum(card)
    if max_value < tmp <= M:
        max_value = tmp

print(max_value)