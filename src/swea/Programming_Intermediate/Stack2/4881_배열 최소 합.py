import sys
sys.stdin = open("sample_input.txt")

# row 마다 돌면서 col의 경우를 따지는 함수
def check_sum(r):
    global sub_sum, res  # 계속해서 재귀처럼 함수 써야 되서 전역변수 갖고와서 쓰는 거임

    # 기존 결과값이 더 작으면 그냥 리턴
    if res < sub_sum:
        return res

    # 배열의 크기랑 똑같아지면 함수 끝내기
    if r == N:
        # 기존 결과 보다 작다면 res 갱신
        if sub_sum < res:
            res = sub_sum
        # 아니면 그냥 리턴
        return res

    # 열을 순회하며 방문 안했으면 방문하고, 값 더해줌
    for c in range(N):
        if not visited[c]:
            visited[c] = True
            sub_sum += a[r][c]
            # 다음 row 에 대해서 계속 체크, 재귀적으로 마지막 row 까지 호출
            check_sum(r+1)
            # 마지막까지 호출 다 끝나면 visited 랑 sub_sum 다시 초기화 시켜줘야 함. 그래야 모든 경우 다 따져보면서 체킹할 수 있음
            visited[c] = False
            sub_sum -= a[r][c]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N  # 몇번째 열을 방문한건지 체킹할 리스트
    sub_sum = 0  # 경우의 수 마다 합 비교해줄 변수
    res = 100  # :: N <= 10
    check_sum(0)  # 0번째 row 부터 찾기 시작

    print("#{} {}".format(tc, res))

