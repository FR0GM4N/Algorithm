# 트리 전위 순회하는 코드 만들기

"""
# input
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

# 전위 순회 코드
def preorder(node):
    if node != 0:  # 노드가 0이 아니라면 == 빈값이 아니라면
        print(node, end=' ')
        preorder(tree[node][0])  # 왼쪽 노드 재귀적으로 탐색
        preorder(tree[node][1])  # 오른쪽 노드 재귀적으로 탐색

V = int(input())  # 정점의 개수
E = V-1
temp = list(map(int, input().split()))  # V-1개 간선 (부모-자식)
tree = [[0]*3 for _ in range(V+1)]

for i in range(E):
    # [왼쪽자식, 오른쪽자식, 부모노드]
    parent, child = temp[i*2], temp[i*2+1]

    if not tree[parent][0]:  # 왼쪽이 비어있다면
        tree[parent][0] = child
    else:  # 오른쪽이 비어있는 경우
        tree[parent][1] = child
    tree[child][2] = parent

preorder(1)
