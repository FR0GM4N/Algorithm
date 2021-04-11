import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def size(root):
    global cnt
    if tree[root][0]:
        cnt += 1
        size(tree[root][0])
    if tree[root][1]:
        cnt += 1
        size(tree[root][1])

for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선개수, root
    tmp = list(map(int, input().split()))  # 부모-자식
    tree = [[0] * 3 for _ in range(E+2)]  # [왼자,오자,부모]
    for i in range(E):
        # [왼쪽자식, 오른쪽자식, 부모노드]
        parent, child = tmp[i * 2], tmp[i * 2 + 1]
        tree[child][2] = parent
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    cnt = 1
    size(N)
    print("#{} {}".format(tc, cnt))

