import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    result = max_num - min_num
    print("#{} {}".format(tc, result))