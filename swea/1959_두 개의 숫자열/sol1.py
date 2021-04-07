import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N과 M 중 작은 수를 s에, 큰 수를 b에 할당할거임
    if N < M:
        s = N
        b = M
        s_lst = A
        b_lst = B
    else:
        s = M
        b = N
        s_lst = B
        b_lst = A

    # 변수 초기화
    max_val = 0
    for i in range(b - s + 1):
        total = 0
        for j in range(s):
            total += b_lst[i + j] * s_lst[j]
        if total > max_val:
            max_val = total

    print("#{} {}".format(tc, max_val))

