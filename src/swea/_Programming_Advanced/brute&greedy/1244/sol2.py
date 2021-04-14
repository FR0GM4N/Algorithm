import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(ex_cnt):
    global res
    if ex_cnt == 0:
        res = max(int(''.join(nums)), res)
        return

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            if not visited.get((''.join(nums), exchange - ex_cnt + 1), 0):
                visited[(''.join(nums), exchange - ex_cnt + 1)] = 1
                dfs(ex_cnt-1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, T+1):
    nums, ex_cnt = input().split()
    nums = list(nums)
    exchange = int(ex_cnt)

    res = 0
    visited = {}
    dfs(exchange)
    print("#{} {}".format(tc, res))