import sys
sys.stdin = open("input.txt")


# N과 M 중 작은 수를 s에, 큰 수를 b에 할당할건데, 이걸 if else로 쓰면 두번 써야하니까
# 아예 함수를 만듦. 근데 인자 자체를 (큰 값, 작은 값)으로 받음 !!
def check(long, short):
    max_value = -987654321
    for i in range(len(long) - len(short)+1):
        result = 0
        for j in range(len(short)):
            result += long[i+j] * short[j]
        if max_value < result:
            max_value = result
    return max_value

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = check(A, B)
    else:
        ans = check(B, A)

    print("#{} {}".format(tc, ans))