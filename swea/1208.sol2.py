import sys
sys.stdin = open("input.txt")

# 최저 높이의 상자 인덱스 위치 반환
def min_search():
    min_value = 101
    min_idx = -1

    # 최저 높이를 찾자 !!
    for i in range(len(box_lst)):
        if box_lst[i] < min_value:
            min_value = box_lst[i]
            min_idx = i
    return min_idx

# 최고 높이의 상자 인덱스 위치 반환
def max_search():
    max_value = 0
    max_idx = -1

    # 최저 높이를 찾자 !!
    for i in range(len(box_lst)):
        if box_lst[i] > max_value:
            max_value = box_lst[i]
            max_idx = i
    return max_idx

for tc in range(1, 10+1):
    N = int(input())  # 덤프횟수
    box_lst = list(map(int, input().split()))

    # N번 덤프하기
    for i in range(N):
        # 최고 높이 상자 한칸 내리기
        box_lst[max_search()] -= 1
        # 최저 높이 상자 한칸 올리기
        box_lst[min_search()] += 1

    print("#{} {}".format(tc, box_lst[max_search()] - box_lst[min_search()]))