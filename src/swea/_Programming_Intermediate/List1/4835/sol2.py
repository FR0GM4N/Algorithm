import sys

sys.stdin = open("sample_input.txt")

T = int(input())

# 간격이 5칸이면 4칸 씩 중복 되고 있음!! 중복된 연산을 줄이면 good!!

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 중복된 연산을 피하자!!!
    # 첫 구간 먼저 구해놓고 맨 앞 값 빼고, 맨 뒤값 더해주는 방법으로 go

    # 첫 구간 총합
    tmp = 0
    for i in range(M):
        tmp += numbers[i]

        max_value = tmp
        min_value = tmp

        for i in range(M, N):
            # 새로운 구간의 합을 아주 간단하게 구할 수 있음!
            tmp = tmp + numbers[i] - numbers[i - M]

            if tmp > max_value:
                max_value = tmp
            if tmp < min_value:
                min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))
