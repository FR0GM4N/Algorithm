import sys
sys.stdin = open("sample_input.txt")

def Find_set(x):
    if x == parent[x]:
        return x
    else:
        return Find_set(parent[x])


def Union(x, y):
    parent[Find_set(y)] = Find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))  # M쌍의 숫자들

    parent = [i for i in range(N+1)]  # 부모노드번호 기억할 리스트
    for i in range(M):
        x, y = nums[2*i], nums[2*i+1]
        Union(x, y)

    res = set()
    for i in range(1, N+1):
        res.add(Find_set(i))
    print("#{} {}".format(tc, len(res)))

