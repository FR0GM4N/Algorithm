import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 카드 장수
    numbers = list(map(int, input()))
    # 0~9 개수 카운트 할 리스트 만들기
    cnt = [0] * 10

    # 받은 리스트 돌면서 카운팅
    for i in numbers:
        cnt[i] += 1

    # 변수 초기화
    max_cnt = 0
    max_num = 0
    for i in range(len(cnt) - 1, -1, -1):
        if cnt[i] > max_cnt:
            max_cnt = cnt[i]
            max_num = i

    print("#{} {} {}".format(tc, max_num, max_cnt))
