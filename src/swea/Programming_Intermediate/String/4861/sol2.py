# 문자열을 뒤집는 4가지 방법; 거꾸로 읽어오는 법, swop, reverse 함수, 슬라이싱 연산[::-1]

import sys
sys.stdin = open("input.txt")


# 뒤에서 부터 읽어오면서 뒤집은 리스트 만드는 함수
def my_reverse(line):
    r_line = []
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])
    return r_line

def my_find():
    for i in range(N):
        # 가로검사
        for j in range(N-M+1):
            # tmp = []
            # for k in range(M):
            #     tmp.append(words[i][j+k])
            tmp = words[i][j:j+M]  # 슬라이싱도 되지만, 세로에서는 tmp = words[j:j+M][i] 안됨
            # 회문 검사
            if tmp == my_reverse(tmp):
                return tmp

        # 세로 검사
        for j in range(N-M+1):
            # 부분 문자열을 위한 빈 리스트
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == my_reverse(tmp):
                return tmp
    return []



T = int(input())
for tc in range(1, T+1):
    # N: 2차원 리스트의 크기, M: 회문 길이
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    ans = my_find()
    print("#{} {}".format(tc, ''.join(ans)))