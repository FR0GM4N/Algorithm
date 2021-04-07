# 내가 푼 풀이인데 실행시간이 801 ms이다.... 즉, 망했다는 소리....
# 다른 사람들은 230 ms 정도로 나옴........

import sys
sys.stdin = open("input.txt")


T = int(input())

num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
reverse_num_dict = dict(map(reversed, num_dict.items()))

for tc in range(1, T+1):
    t = input().split()  # ['#1', '7041'] <class 'str'>
    str_lst = input().split()  # ['SVN', 'FOR', 'ZRO', ...]

    num_lst = []
    for s in str_lst:
        n = num_dict[s]
        num_lst.append(n)
        num_lst.sort()

    result = []
    for n in num_lst:
        s = reverse_num_dict[n]
        result.append(s)

    print("{}".format(t[0]))
    print(" ".join(result))