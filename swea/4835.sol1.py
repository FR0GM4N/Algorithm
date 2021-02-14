import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# N: 정수의 개수
# M: 이웃한 숫자의 개수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 구간 시작점
    for i in range(N - M + 1):
        tmp = 0

        for j in range(M):
            tmp += numbers[i+j]
        # for j in numbers[i:i+M]:
        #     tmp += j

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))