import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 돌아가야할 학생수
    room_lst = [list(map(int, input().split())) for _ in range(N)]  # [[출발방, 도착방], ...]

    cnt = [0] * 201
    for room in room_lst:
        if room[0] < room[1]:
            s = (room[0] + 1) // 2
            e = (room[1] + 1) // 2
        else:
            e = (room[0] + 1) // 2
            s = (room[1] + 1) // 2

        for j in range(s, e+1):
            cnt[j] += 1

    ans = max(cnt)

    print("#{} {}".format(tc, ans))