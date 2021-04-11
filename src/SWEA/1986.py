import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    total = 0
    for i in range(1, N+1):
        if i % 2:  # 홀수인 경우
            total += i
        else:  # 짝수인 경우
            total -= i

    print("#{} {}".format(tc, total))

