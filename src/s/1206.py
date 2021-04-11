# SWEA_1206_View

import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    b_lst = list(map(int, input().split()))  # 빌딩리스트

    # 변수초기화
    cnt = 0
    # 앞 뒤 0 두개 뺀 상태에서 for 문 돌면서
    for i in range(2, N-2):
        # 왼쪽 2개보다 크고 & 오른쪽 두개보다 크면
        if b_lst[i] > b_lst[i-1] and b_lst[i] > b_lst[i-2] and b_lst[i] > b_lst[i+1] and b_lst[i] > b_lst[i+2]:
            # 양 옆 애들 중 높이 가장 높은 애 만큼 빼주고 카운팅 해줌
            # 값 차이가 가장 적은 애가 높이가 가장 높기 때문에 반복문 돌려서 두번째로 높은애 찾음
            a1 = b_lst[i] - b_lst[i - 2]
            a2 = b_lst[i] - b_lst[i - 1]
            a3 = b_lst[i] - b_lst[i + 1]
            a4 = b_lst[i] - b_lst[i + 2]
            min_gap = a1
            for a in [a1, a2, a3, a4]:
                if a < min_gap:
                    min_gap = a
            cnt += min_gap
    
    print("#{} {}".format(tc, cnt))
