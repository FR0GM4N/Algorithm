import sys
sys.stdin = open("input.txt")

T = int(input())

# 서브트리 크기 구하는 함수
def size(node):
    global cnt
    if tree[node][0]:
        size(tree[node][0])
        cnt += 1
    if tree[node][1]:
        size(tree[node][1])
        cnt += 1

for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    tmp = list(map(int, input().split()))  # 부모-자식
    tree = [[0]*3 for _ in range(V+1)]  # [자식1,자식2,부모]

    for i in range(E):
        parent, child = tmp[2*i], tmp[2*i+1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    # 공통조상 중 가장 가까운 정점 찾기
    n1_p, n2_p = [], []
    while True:
        p = tree[n1][2]
        if p == 0:
            break
        n1_p.append(p)
        n1 = p
    while True:
        p = tree[n2][2]
        if p == 0:
            break
        n2_p.append(p)
        n2 = p

    n1_p.reverse(), n2_p.reverse()
    ans_root = 1  # 공통조상이 1 하나인 경우를 위해 설정
    for i in range(len(n1_p)):
        if n1_p[i] != n2_p[i]:
            ans_root = n1_p[i-1]
            break
    cnt = 1
    size(ans_root)
    print("#{} {} {}".format(tc, ans_root, cnt))