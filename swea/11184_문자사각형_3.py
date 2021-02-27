import sys
sys.stdin = open("input.txt")

T = int(input())

def fill(arr):
    num = ord('A')
    mid = N // 2
    s = e = mid
    for i in range(mid, -1, -1):
        for j in range(s, e+1):
            arr[j][i] = chr(num)
            num += 1
            if chr(num-1) == "Z":
                num = ord('A')
        s -= 1
        e += 1

def print_all(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()

for tc in range(1, T+1):
    N = int(input())

    arr = [['' for _ in range(N)] for _ in range(N)]

    fill(arr)

    print("#{}".format(tc))
    print_all(arr)

