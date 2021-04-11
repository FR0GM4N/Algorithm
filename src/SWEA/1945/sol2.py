import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    prime = [2, 3, 5, 7, 11]  # 리스트를 만들어서 반복문 돌리는게 더 효율적..!!

    # 각 소수당 지수 카운팅할 리스트 만들어줌
    cnt = [0] * len(prime)

    for i in range(len(prime)):
        while N % prime[i] == 0:
            cnt[i] += 1
            N //= prime[i]

    print("#{} {}".format(tc, " ".join(map(str, cnt))))