import sys
sys.stdin = open("input.txt")

T = 10

def in_order(node):
    # 왼쪽자식
    if len(tmp[node]) >= 3:
        in_order(int(tmp[node][2]))
    # 해당노드
    print(tmp[node][1], end="")
    # 오른쪽자식
    if len(tmp[node]) == 4:
        in_order(int(tmp[node][3]))


for tc in range(1, T+1):
    N = int(input())  # 정점의 총 수
    tmp = [[]] + [input().split() for _ in range(N)]


    print("#{}".format(tc), end=" ")
    in_order(1)
    print()
