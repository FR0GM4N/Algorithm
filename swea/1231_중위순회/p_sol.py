import sys
sys.stdin = open("input.txt")


T = 10

def in_order(node):
    if tree[node][3] != 0:
        in_order(tree[node][0])
        print(tree[node][3], end="")
        in_order(tree[node][1])


for tc in range(1, T+1):
    N = int(input())  # 정점의 개수
    tree = [[0 for _ in range(4)]for _ in range(N+1)]  # 왼쪽자식, 오른쪽자식, 부모노드, 데이터
    for i in range(N):
        # 1 W 2 3 / 8 S
        node_info = input().split()
        node_num = int(node_info[0])
        node_data = node_info[1]

        tree[node_num][3] = node_data

        # 내가 6번이면 자식노드는 6*2, 6*2+1, 부모노드는 6//2번
        # 왼쪽자식 여부 판단
        if node_num * 2 <= N:
            tree[node_num][0] = int(node_info[2])
            # 오른쪽 자식 여부 판단
            if node_num * 2 + 1 <= N:
                tree[node_num][1] = int(node_info[3])

    print('#{}'.format(tc), end=" ")
    in_order(1)
    print()