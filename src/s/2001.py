import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 배열 크기, M: 파리채
    N, M = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]

    # 배열 전부 탐색하면서 합 구하고 max 최신화
    m_max = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            m_sum = 0
            for r in range(M):
                for c in range(M):
                    m_sum += a[i+r][j+c]

            if m_sum > m_max:
                m_max = m_sum

    print("#{} {}".format(tc, m_max))