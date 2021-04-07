# 정수 N개의 합

def solve(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

num_list = list(map(int,input().split()))
print(solve(num_list))