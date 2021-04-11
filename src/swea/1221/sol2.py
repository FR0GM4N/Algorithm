import sys
sys.stdin = open("input.txt")

T = int(input())

number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T + 1):
    N, length = input().split()
    num_lst = list(input().split())

    idx_lst = [0] * 10

    for num in num_lst:
        for i in range(len(number)):
            if num == number[i]:
                idx_lst[i] += 1

    ans = ''
    for i in range(len(idx_lst)):
        ans += (number[i] + ' ') * idx_lst[i]

    print("#{} {}".format(tc, ans))