import sys
sys.stdin = open("input.txt")

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*(N*N+1)

    for x in range(N):
        for y in range(N):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<N and 0<=ny<N and a[x][y]+1 == a[nx][ny]:
                    check[a[x][y]] = 1

    res = [0, 0]  # 처음 출발해야 하는 방 번호, 최대 몇 개의 방을 이동할 수 있는지
    cnt = 0
    for i in range(1, len(check)):
        cnt += 1
        if not check[i]:
            if res[1] < cnt:
                res = [i-cnt+1, cnt]
            cnt = 0
    print("#{} {} {}".format(tc, res[0], res[1]))

