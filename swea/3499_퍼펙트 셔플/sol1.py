import sys
sys.stdin = open("sample_input.txt")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = input().split()

    ans = []
    for i in range(N // 2):
        ans.append(card[i])
        ans.append(card[- (N // 2) + i])
    if N % 2:  # 길이가 홀수이면 가운데 문자 추가
        ans.append(card[N//2])

    print("#{} {}".format(tc, " ".join(ans)))

