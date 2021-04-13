import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        res = 1
    else:
        res = 0
    print("#{} {}".format(tc, res))

