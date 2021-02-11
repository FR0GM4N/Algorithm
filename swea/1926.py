# swea_1926_간단한 369게임

import sys
sys.stdin = open("input.txt")

# 정수 자리수 만큼 잘라서 3, 6, 9 확인하기
def check(n):
    cnt = 0
    while n:  # n != 0
        # n을 한자리씩 쪼개서 각각을 체크해줄거임. ex) 137 -> 1, 3, 7 따로따로 체크!!!
        res = n % 10  # 포인트는 나머지를 구하는 것!
        n //= 10
        if res != 0 and res % 3 == 0:  # 0 % 3 = 0 이기 때문에 !=0 조건 넣어줘야함
            cnt += 1
    return cnt

N = int(input())

for i in range(1, N+1):
    cnt = check(i)

    if cnt:  # cnt != 0
        for j in range(cnt):
            print("-", end="")
        print(end=" ")
    else:
        print("{}".format(i), end=" ")