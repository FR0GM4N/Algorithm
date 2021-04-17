import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def find_num2(nums):
    tmp = []
    for i in range(len(nums)):
        if nums[i]:  # 1 -> 0으로 바꿈
            a = nums[:]
            a[i] = 0
            tmp.append(a)
        else:  # 0 -> 1로 바꿈
            a = nums[:]
            a[i] = 1
            tmp.append(a)

    for ele in tmp:  # tmp = [[0, 0, 1, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 1, 1]]
        num_10 = 0
        for i in range(len(nums)):  # nums = [1, 0, 1, 0]
            num_10 += (2 ** (len(nums) - 1 - i)) * ele[i]
        set_2.add(num_10)


def find_num3(nums):
    tmp = []
    for i in range(len(nums)):
        if nums[i] == 0:  # 0 -> 1, 2
            a = nums[:]
            a[i] = 1
            tmp.append(a)
            b = nums[:]
            b[i] = 2
            tmp.append(b)
        if nums[i] == 1:  # 1 -> 0, 2
            a = nums[:]
            a[i] = 0
            tmp.append(a)
            b = nums[:]
            b[i] = 2
            tmp.append(b)
        if nums[i] == 2:  # 2 -> 0, 1
            a = nums[:]
            a[i] = 0
            tmp.append(a)
            b = nums[:]
            b[i] = 1
            tmp.append(b)

    for ele in tmp:
        num_10 = 0
        for i in range(len(nums)):
            num_10 += (3 ** (len(nums) - 1 - i)) * ele[i]
        set_3.add(num_10)


for tc in range(1, T+1):
    num_2 = list(map(int, input()))
    num_3 = list(map(int, input()))
    set_2 = set()
    set_3 = set()

    find_num2(num_2)
    find_num3(num_3)

    res = set_2 & set_3
    print("#{} {}".format(tc, *res))


