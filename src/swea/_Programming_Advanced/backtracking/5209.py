import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def dfs(i, tmp):  # 행, 현재 타임 합
    global res
    if tmp >= res:
        return
    if i == N:
        res = min(tmp, res)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(i+1, tmp+a[i][j])
            visited[j] = 0


for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    res = 987654321
    visited = [0]*N  # 열체크
    dfs(0, 0)
    print("#{} {}".format(tc, res))

