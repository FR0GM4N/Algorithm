import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 자식노드 기준에서 체크. 부모가 작아질 때까지 계속 비교 -> 재귀
def change(node):
    parent = tree[node][0]
    if parent:
        if tree[parent][3] > tree[node][3]:
            tree[parent][3], tree[node][3] = tree[node][3], tree[parent][3]
    else:
        return
    change(parent)


def sum_root(N):
    global ans
    if tree[N][0] == 0:
        return
    ans += tree[tree[N][0]][3]
    sum_root(tree[N][0])


for tc in range(1, T+1):
    N = int(input())
    tmp = list(map(int, input().split()))
    tree = [[0]*4 for _ in range(N+1)]  # [부모노드,왼자,오자,value]

    for i in range(1, N+1):
        tree[i][3] = tmp[i-1]
        tree[i][0] = i // 2
        if 2 * i <= N:
            tree[i][1] = 2 * i
            tree[i][2] = 2 * i + 1
            if 2*i+1 > N:
                tree[i][2] = 0

    for i in range(1, N+1):
        change(i)

    ans = 0
    sum_root(N)

    print("#{} {}".format(tc, ans))


