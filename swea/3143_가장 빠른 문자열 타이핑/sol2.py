import sys
sys.stdin = open("input.txt")

# 내장함수 사용 ver

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    print("#{} {}".format(tc, len(A.replace(B, '0'))))