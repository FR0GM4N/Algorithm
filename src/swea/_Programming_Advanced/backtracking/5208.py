import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def dfs(i, max_i, cnt):  # 현재위치(인덱스), 최대로 갈 수 있는 범위, 해당타임 교환횟수
    global res
    if cnt >= res:
        return
    if max_i >= N:
        res = min(cnt, res)
        return
    for j in range(max_i, i, -1):
        dfs(j, j + M[j], cnt + 1)


for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    M = [0] + tmp[1:]  # 정류장 별 배터리 용량(1~N-1)

    res = 10000
    dfs(1, 1+M[1], 0)
    print("#{} {}".format(tc, res))

