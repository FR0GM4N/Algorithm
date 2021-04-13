import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N:노드개수, M:리드노프개수, L:출력할 노드번호
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    # 방법2
    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]

    print("#{} {}".format(tc, tree[L]))