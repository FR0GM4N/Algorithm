def dfs(idx, tmp):
    global res

    if tmp >= B:
        res = min(tmp, res)
        return
    if idx == N:
        return

    dfs(idx+1, tmp+heigth[idx])  # 뽑은 경우
    dfs(idx+1, tmp)  # 안뽑은 경우


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())  # N:직원수, B:선반높이
    heigth = list(map(int, input().split()))
    res = 200001
    dfs(0, 0)  # 인덱스, 부분집합합
    print("#{} {}".format(tc, res-B))