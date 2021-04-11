import sys
sys.stdin = open("input.txt")

'''
10x10 리스트를 전부 0으로 만들어주고, 빨이면 +1, 파이면 +2 그래서 총합이 3인 애들 개수만 출력
근데 중복된 컬러가 칠해져있다면 안칠하고 패쓰
근데 코드를 완성하고 나니 이중 for문이 너무 많은거 같은디.... 어케 방법이 없나....
'''

T = int(input())
for tc in range(1, T+1):
    # 빈 리스트 만들어주기
    a = [[0] * 10 for _ in range(10)]
    # 총합이 3인 애들만 카운팅할 output 변수
    res = 0

    N = int(input())
    for _ in range(N):
        # 빨: color = 1, 파: color = 2
        r1, c1, r2, c2, color = map(int, input().split())

        # 빨간색
        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if a[i][j] != 1 and a[i][j] != 3:
                        a[i][j] += 1

        # 파란색
        elif color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if a[i][j] != 2 and a[i][j] != 3:
                        a[i][j] += 2

    for i in range(10):
        for j in range(10):
            if a[i][j] == 3:
                res += 1

    print("#{} {}".format(tc, res))