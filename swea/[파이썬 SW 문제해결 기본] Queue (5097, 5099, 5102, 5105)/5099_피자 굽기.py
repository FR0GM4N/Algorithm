import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N:화덕의 크기, M: 피자 개수
    cheese = list(map(int, input().split()))  # M개의 피자에 뿌려진 각 치즈 양

    # 치즈의 양이 0이 되면 pop하고 new 치즈 append 하면서 마지막 남은 치즈의 인덱스 출력하면 되는데 인덱스를 찾기 위해서 리스트로 묶어줌
    cheese_check = []  # 치즈랑 인덱스랑 같이 묶어줄 리스트
    for i in range(M):
        cheese_check.append([cheese[i], i])

    oven = []  # 오븐 안에 들어간 치즈들
    for i in range(N):
        oven.append(cheese_check.pop(0))

    while True:
        if len(oven) == 1:
            break
        oven[0][0] = oven[0][0] // 2
        f_c = oven[0][0]
        t = oven.pop(0)
        if f_c != 0:
            oven.append(t)
        elif cheese_check and f_c == 0:  # 치즈가 남은 상태라면
            oven.append(cheese_check.pop(0))
        elif not cheese_check and f_c == 0:  # 치즈 안남은 상태라면
            continue

    print("#{} {}".format(tc, oven[0][1] + 1))


