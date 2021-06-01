from itertools import combinations

# Sij 합 구하는 함수
def subsum(tp1, tp2):
    sumA, sumB = 0, 0
    for i in tp1:
        for j in tp1:
            sumA += S[i][j]
    for i in tp2:
        for j in tp2:
            sumB += S[i][j]
    return abs(sumA-sumB)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]  # Sij: 1~100

comb_lst = list(combinations(range(N), N//2))
res = 987654321
for i in range(len(comb_lst)//2):
    tmp = subsum(comb_lst[i], comb_lst[len(comb_lst)-1-i])
    if tmp < res:
        res = tmp

print(res)

