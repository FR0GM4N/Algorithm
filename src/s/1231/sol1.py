import sys
sys.stdin = open("input.txt")

T = 10

def in_order(node):
    if node != 0:
        in_order(tree[node][1])
        print(tree[node][0], end="")
        in_order(tree[node][2])

for tc in range(1, T+1):
    N = int(input())  # 정점의 총 수
    tree = [[0]*3 for _ in range(N+1)]  # [me, ch1, ch2]
    for _ in range(N):
        tmp = input().split()
        num, me = int(tmp[0]), tmp[1]
        tree[num][0] = me
        if len(tmp) == 4:
            ch1, ch2 = int(tmp[2]), int(tmp[3])
            tree[num][1] = ch1
            tree[num][2] = ch2
        elif len(tmp) == 3:
            ch1 = int(tmp[2])
            tree[num][1] = ch1


    print("#{}".format(tc), end=" ")
    in_order(1)
    print()

