import sys
sys.stdin = open("input.txt")

T = int(input())

def fill(arr):
    num = ord('A')
    for i in range(N):
        if not i % 2:
            for j in range(N):
                arr[j][i] = chr(num)
                num += 1
                if chr(num-1) == "Z":
                    num = ord('A')
        else:
            for j in range(N-1, -1, -1):
                arr[j][i] = chr(num)
                num += 1
                if chr(num-1) == "Z":
                    num = ord('A')

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

