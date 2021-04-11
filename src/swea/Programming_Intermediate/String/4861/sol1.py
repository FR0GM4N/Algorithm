# 내가 처음 푼 풀이
# 반복문이 지나치게 많고, 회문이면 회문 전체를 뒤집어도 같은데 왜 굳이 중간을 잘라서 비교한건지 모를..
# 슬라이싱 생각도 못했다. 잊지말고 써먹자

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 스트링은 2x2 좌표로 인덱스 접근 할 수 없으므로 리스트로 만들어줌 <- 접근할 수 있음.. str도 iterable이자너...
    str_lst = [list(input()) for _ in range(N)]
    palindrome = ''

    # 행 체크
    for r in range(N):
        for c in range(N-M+1):
            cnt = 0  # 문자열 돌면서 같은 문자인지 체킹하는 변수
            p = ''
            # M 길이 문자열 안에서 도는 반복문
            for i in range(M//2):
                if str_lst[r][c+i] == str_lst[r][c+M-1-i]:
                    cnt += 1
                    p += str_lst[r][c+i]
            if cnt == M // 2:  # 회문 찾은 경우
                if M % 2:  # 홀수이면 mid값도 더해주기
                    palindrome = p + str_lst[r][c+M//2] + p[::-1]
                else:
                    palindrome = p + p[::-1]

    # 열 체크
    for c in range(N):
        for r in range(N-M+1):
            cnt = 0
            p = ''
            for i in range(M//2):
                if str_lst[r+i][c] == str_lst[r+M-1-i][c]:
                    cnt += 1
                    p += str_lst[r+i][c]
            if cnt == M // 2:  # 회문 찾은 경우
                if M % 2:  # 홀수이면 mid값도 더해주기
                    palindrome = p + str_lst[r+M//2][c] + p[::-1]
                else:
                    palindrome = p + p[::-1]

    print("#{} {}".format(tc, palindrome))

