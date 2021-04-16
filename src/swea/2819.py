import sys
sys.stdin = open("sample_input.txt")

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def f(n, x, y):  # n:이동한횟수, x,y:행열 좌표
    global res

    if n == 7:
        res.add(''.join(s))
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<4 and 0<=ny<4:
            s[n] = a[nx][ny]
            f(n+1, nx, ny)


for tc in range(1, T+1):
    a = [input().split() for _ in range(4)]
    s = [''] * 7  # 7개 숫자 채울 리스트
    res = set()
    for i in range(4):
        for j in range(4):
            f(0, i, j)

    print("#{} {}".format(tc, len(res)))

