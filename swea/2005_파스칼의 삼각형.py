import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 먼저 0으로 배열 초기화. 여기에 숫자 넣어주고 출력할거임
    a = [[0] * N for i in range(N)]

    for i in range(N):
        # 맨 앞 원소는 1로 설정
        a[i][0] = 1
        # 행의 인덱스 만큼 열이 출력되어야 하므로 범위 설정
        for j in range(1, i+1):
            a[i][j] = a[i-1][j-1] + a[i-1][j]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()
