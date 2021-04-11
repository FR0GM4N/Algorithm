import sys
sys.stdin = open("input.txt")

T = 10

def cal(c1, p, c2):
    if p == '+':
        return c1 + c2
    elif p == '-':
        return c1 - c2
    elif p == '*':
        return c1 * c2
    elif p == '/':
        return c1 / c2


for tc in range(1, T+1):
    N = int(input())
    tree = [[0]*4 for _ in range(N+1)]
    for i in range(1, N+1):
        tmp = input().split()
        if len(tmp) == 4:
            # [value,왼쪽자식,오른쪽자식,부모노드]
            tree[i][0], tree[i][1], tree[i][2] = tmp[1], int(tmp[2]), int(tmp[3])
            tree[tree[i][1]][3] = int(tmp[0])
            tree[tree[i][2]][3] = int(tmp[0])
        else:
            tree[i][0] = int(tmp[1])

    for i in range(N-1, 0, -2):
        parent = tree[i][3]
        tree[parent][0] = cal(tree[i][0], tree[parent][0], tree[i+1][0])  # 부모노드 값 변경

    print("#{} {}".format(tc, int(tree[1][0])))