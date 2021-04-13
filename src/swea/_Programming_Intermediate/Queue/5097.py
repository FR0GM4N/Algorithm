import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        t = numbers.pop(0)
        numbers.append(t)

    print("#{} {}".format(tc, numbers[0]))
