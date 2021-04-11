import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N:노드개수, M:리드노프개수, L:출력할 노드번호
    tree = [0 for _ in range(N + 1)]
    for i in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    # 방법1
    if N % 2 == 0:  # 노드개수 짝수인 경우를 위해 설정
        tree.append(0)

    for i in range((N//2)*2, 1, -2):
        tree[i // 2] = tree[i] + tree[i + 1]


    print("#{} {}".format(tc, tree[L]))
