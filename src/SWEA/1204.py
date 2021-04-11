import sys
sys.stdin = open("input.txt")

# 포인트는 카운팅 소트!!!!! 빈 배열 만들고 카운트 누적한다음 최댓값 구하면 됨.

T = int(input())
for _ in range(1, T+1):
    tc = int(input())
    scores = list(map(int, input().split()))
    count = [0] * 101

    # 1. 점수 카운팅
    for i in range(1000):
        count[scores[i]] += 1

    # 최대 인덱스
    max_idx = 0
    for i in range(len(count)):
        if count[i] >= count[max_idx]:
            max_idx = i

    print("#{} {}".format(tc, max_idx))