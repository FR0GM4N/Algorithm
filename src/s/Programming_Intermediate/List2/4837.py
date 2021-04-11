import sys
sys.stdin = open("input.txt")

'''
일단 1~12 까지 숫자있는 리스트 a 만들고, 일단 완전탐색으로 모든 부분집합 생성
 ( 원래는 처음부터 원소의 개수가 N인 집합만 뽑고 싶었는데, 그럴려면 이진수로 나타냈을 때 
   1의 개수가 N, 0의 개수가 12-N인 애들만 뽑아서 반복문 돌리면 되는데 이 부분을 못하겠어서 패쓰....)
부분집합의 원소 개수가 N인 집합만 뽑고 합 구함.
합이 K 인 애들의 개수를 카운팅해서 출력


# 부분집합 구할 때 비트연산자 사용함. 근데 비트연산자로 풀어도 되고 from itertools import combinations로 풀면 간단함.
'''

# 리스트 생성
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(a)

T = int(input())
for tc in range(1, T+1):
    # N: 부분집합의 원소 개수, K: 부분집합의 합
    N, K = map(int, input().split())
    cnt = 0

    # 모든 부분집합 생성
    for i in range(1<<n):
        # 각 부분집합들 리스트 & 합 생성
        new_a = []
        a_sum = 0
        for j in range(n+1):
            if i & (1<<j):
                new_a += [a[j]]
                a_sum += a[j]
        # 원소개수 N이면서 합이 K인 부분집합 개수 카운트
        if len(new_a) == N and a_sum == K:
            cnt += 1

    print("#{} {}".format(tc, cnt))