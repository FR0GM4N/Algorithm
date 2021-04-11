import sys
sys.stdin = open("input.txt")

T = int(input())

# row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())

    # 일단 빈 2차원 배열 만들어줌
    snail = [[0]*N for _ in range(N)]

    # row, col 처음 위치 설정 & snail 첫 시작점 1로 설정 후 반복문 스타트
    r, c = 0, 0
    snail[r][c] = 1

    i = 0  # 0:우, 1:하, 2:좌, 3:상
    # N**2 되면 배열 끝나게 조건 설정
    for n in range(2, N**2 + 1):
        r += dr[i]
        c += dc[i]
        snail[r][c] = n

        # 가로 세로 길이가 N이 되면 direction 체인지 하도록 설정
        # 1. 가로세로 범위 N 안에서, 아직 0인 애들은 값 바뀔 수 있게 건너뜀
        if 0 <= r + dr[i] < N and 0 <= c + dc[i] < N and snail[r + dr[i]][c + dc[i]] == 0:
            continue

        # 2. 인덱스가 3 이 되면 달팽이 모양으로 다시 돌아야 하니까 인덱스 0으로 바꿔줌. 3 아님 킵고잉
        if i == 3:
            i = 0
        else:
            i += 1

    print("#{}".format(tc))
    for row in snail:
        print(*row)  # 프린트할 때 앞에 * 붙이면 [] 안나옴!!
    print()
