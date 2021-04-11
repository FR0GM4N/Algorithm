import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    text = input()

    # 패턴의 최대 길이가 10이고, 0부터 시작하면 비교불가 이므로 range를 1~10으로 설정
    for n in range(1, 10):
        # n: 패턴마디의 길이
        if text[0:n] == text[n:2*n]:
            ans = n
            break  # break 안해주면 10 이내 길이에서 반복되는 길이를 새로 갱신함

    print("#{} {}".format(tc, ans))