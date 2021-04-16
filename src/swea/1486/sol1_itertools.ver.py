from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())  # N:직원수, B:선반높이
    heigth = list(map(int, input().split()))

    res = []
    for i in range(1, N+1):
        ele = combinations(heigth, i)  # i개(1~N) 뽑는 경우의수
        for k in ele:
            tmp = sum(k)
            if tmp >= B:
                res.append(tmp)

    print("#{} {}".format(tc, min(res)-B))

