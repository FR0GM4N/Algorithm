import sys
sys.stdin = open("input.txt")

# 회문 길이 리턴하는 함수. 회문이면 M을 리턴하고 아니면 0을 리턴함
def my_find(M):  # M; 회문길이
    for i in range(N):
        for j in range(N-M+1):

            # 가로 검사
            for k in range(M//2):
                # 회문이 아닌 경우 break로 반복문 빠져나오기
                if a[i][j+k] != a[i][j+M-1-k]:
                    break
                elif k == M//2 - 1:  # 즉, 회문이라는 의미
                    return M
            # 세로 검사
            for k in range(M//2):
                if a[j+k][i] != a[j+M-1-k][i]:
                    break
                elif k == M//2 - 1:
                    return M

    return 0  # 반복문 다 돌았는데도 회문이 없는 경우


T = 10
for tc in range(1, T+1):
    t = int(input())
    N = 100
    a = [input() for _ in range(N)]

    # 반복문 뒤에서 부터 돌면서 가장 긴 회문 길이 출력
    for i in range(N, 0, -1):
        ans = my_find(i)

        # 0이 아닐 경우 break해서 반복문 종료하고 ans 출력
        if ans != 0:
            break

    print("#{} {}".format(t, ans))
