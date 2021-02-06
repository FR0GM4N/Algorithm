# 최소, 최대

# 1. pythonic
number = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), max(num_list))

# 2.
number = int(input())
num_list = list(map(int, input().split()))

min_num = num_list[0]
max_num = num_list[0]
for num in num_list:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(min_num, max_num)
