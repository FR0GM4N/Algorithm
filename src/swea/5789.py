import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N: 박스 칸수, Q: 숫자 변경 횟수
    N, Q = map(int, input().split())

    # 전부 0인 박스 만들어주고
    box = [0] * (N+1)

    # 반복문 돌리면서 L, Q값에 따라 숫자 i로 바꿔주기
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i

    print("#{}".format(tc), end=" ")
    for i in range(1, N+1):
        print('{}'.format(box[i]), end=" ")
    print()
