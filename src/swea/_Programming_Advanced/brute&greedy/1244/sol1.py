import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(s):
    global res, ex_cnt
    if ex_cnt == 0:
        res = max(int(''.join(nums)), res)
        return

    for i in range(s, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                ex_cnt -= 1
                dfs(i)
                nums[i], nums[j] = nums[j], nums[i]
                ex_cnt += 1


for tc in range(1, T+1):
    nums, ex_cnt = input().split()
    nums = list(nums)
    ex_cnt = int(ex_cnt)
    copy_nums = nums[:]

    res = 0
    if len(nums) == 2 or nums == sorted(nums, reverse=True):
        if ex_cnt % 2:
            copy_nums[-1], copy_nums[-2] = copy_nums[-2], copy_nums[-1]
        res = int(''.join(copy_nums))

    dfs(0)
    print("#{} {}".format(tc, res))

