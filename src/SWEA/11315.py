import sys
sys.stdin = open("sample_input.txt")

dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

# 가로, 세로, 대각선 동시에 탐색하면서 5이상이면 끝. 5이상이면 뒤는 더이상 볼 필요가 없음
def check():
    for i in range(N):
        for j in range(N):
            for k in range(4):  # dr, dc가 4개라서 range 4
                o_cnt = 0
                nr, nc = i, j
                while 0 <= nr < N and 0 <= nc < N and a[nr][nc] == 'o':
                    o_cnt += 1
                    if o_cnt == 5:
                        return "YES"
                    nr += dr[k]
                    nc += dc[k]
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 배열의 크기
    a = [input() for _ in range(N)]

    print("#{} {}".format(tc, check()))

