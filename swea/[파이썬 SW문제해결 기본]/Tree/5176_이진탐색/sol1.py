import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def in_order(i):
    global cnt
    if i <= N:
        in_order(2*i)
        tree[i] = cnt
        cnt += 1
        in_order(2*i+1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    cnt = 1
    in_order(1)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))

