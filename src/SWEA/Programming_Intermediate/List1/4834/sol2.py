import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 숫자가 붙어있어서 split 처리 안하고 str 그대로 받음
    # (str은 iterable하니까 for문 돌려서 카운팅 가능)
    card = input()

    # count 배열 생성
    count = [0] * 10

    max_count = -1
    max_num = -1

    # 카드 숫자 세기
    for i in card:
        count[int(i)] += 1
        if max_count < count[int(i)]:
            max_count = count[int(i)]

    for i in range(len(count)-1, -1, -1):
        if max_count == count[i]:
            max_num = i
            break

    print("#{} {} {}".format(tc, max_num, max_count))

