import sys
sys.stdin = open("sample_input.txt")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = input().split()
    print("#{}".format(tc), end=" ")
    a = 0
    b = N // 2 + N % 2
    while b < N:
        print(card[a], end=" ")
        print(card[b], end=" ")
        a += 1
        b += 1
    if N % 2 == 1:
        print(card[a])
    print()