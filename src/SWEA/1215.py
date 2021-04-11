import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    n = int(input())  # 회문길이
    a = [input() for _ in range(8)]

    # 회문개수 구하는 output 변수
    ans = 0
    for i in range(8):

        # 가로 탐색 (슬라이싱 ver.)
        for j in range(8-n+1):
            if a[i][j:j+n] == a[i][j:j+n][::-1]:
                ans += 1

        # 세로 탐색 (빈 리스크 만들어서 문자열 넣어서 비교하는 ver.  ::세로는 슬라이싱 못함)
        for j in range(8-n+1):
            tmp = []
            for k in range(n):
                tmp.append(a[j+k][i])
            if tmp == tmp[::-1]:
                ans += 1

    print("#{} {}".format(tc, ans))

