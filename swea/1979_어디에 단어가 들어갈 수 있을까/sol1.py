import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 배열 크기, K: 단어 길이
    N, K = map(int, input().split())

    # 양 옆 블랙박스인지 체크하기 위해 맨 앞뒤 row, col에 0 넣어줌
    a = [[0] * (N + 2)]
    a += [[0]+list(map(int, input().split()))+[0] for _ in range(N)]
    a += [[0] * (N + 2)]

    # 1 에만 단어가 들어갈 수 있음. 근데 자리 남으면 안되고 꽉 채워서 들어가야 됨. -> 양옆이 0인지 체크하면 됨
    # 그러고 행/열 각각 for문 돌려서 1이 연속으로 K냐 보면 됨.
    cnt = 0

    # 행 탐색
    for i in range(1, N + 1):  # 맨 앞에 0 추가 해줘서 범위 주의
        for j in range(1, N - K + 2):
            sum_of_1 = 0
            for k in range(K):
                if a[i][j+k]:
                    sum_of_1 += 1
            if sum_of_1 == K and a[i][j-1] == 0 and a[i][j+K] == 0:
                cnt += 1

    # 열 탐색
    for j in range(1, N + 1):
        for i in range(1, N - K + 2):
            sum_of_1 = 0
            for k in range(K):
                if a[i+k][j]:
                    sum_of_1 += 1
            if sum_of_1 == K and a[i-1][j] == 0 and a[i+K][j] == 0:
                cnt += 1

    print("#{} {}".format(tc, cnt))