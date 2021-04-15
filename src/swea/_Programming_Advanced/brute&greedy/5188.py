import sys
sys.stdin = open("sample_input.txt")

# 가능한 모든 경로 구해서 min 구하면 되겠네? -> 근데 그럼 최악의 경우 10,400,600 번 연산해서 시간초과 뜸

T = int(input())

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    global res, tmp
    if res < tmp:  # 현재 결과값 보다 크면 함수 끝나도록 -> 제한시간때문에 가지치기 해야함
        return
    if x == N-1 and y == N-1:
        res = tmp
        return
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if (nx, ny) not in visited:
            visited.append((nx, ny))  # 좌표 업로드
            tmp += a[nx][ny]
            dfs(nx, ny)
            tmp -= a[nx][ny]  # 원상복구
            visited.remove((nx, ny))


for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    res = 3000
    tmp = a[0][0]
    dfs(0, 0)  # 현재좌표
    print("#{} {}".format(tc, res))

