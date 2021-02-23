import sys
sys.stdin = open("sample_input.txt")

# 재귀함수
def paper_cut(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return paper_cut(n-1) + paper_cut(n-2) * 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = paper_cut(N//10)

    print("#{} {}".format(tc, ans))