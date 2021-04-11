import sys
sys.stdin = open("input.txt")

T = int(input())

number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T + 1):
    N, length = input().split()
    num_str = input().split()

    res = []
    for i in range(10):
        for num in num_str:
            if number[i] == num:
                res.append(num)

    print(N)
    print(*res)