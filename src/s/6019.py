import sys
sys.stdin = open("s_input.txt")

T = int(input())
for tc in range(1, T+1):
    # D: 두 기차 전면부 사이 거리, A: 기차 A의 속력, B: 기차 B의 속력, F: 파리 속력
    D, A, B, F = map(int, input().split())
    # 그냥 이렇게 푸는 문제였음....
    ans = D / (A+B) * F
    print("#{} {}".format(tc, format(ans, ".10f")))