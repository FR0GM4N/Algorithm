import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    a.sort(key=lambda x: (-x[1], -x[0]))

    s, e = a.pop()
    cnt = 1
    while a:
        c_s, c_e = a.pop()
        if e <= c_s:  # 현재 시작시간이 전회차의 끝시간보다 같거나 크면
            s, e = c_s, c_e  # 갱신
            cnt += 1

    print("#{} {}".format(tc, cnt))

