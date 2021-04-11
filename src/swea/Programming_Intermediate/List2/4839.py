import sys
sys.stdin = open("input.txt")

# 이길려면 이진탐색하는 횟수가 적어야함 (같으면 0 출력)
# 방향: 이진탐색 함수 만들고 카운팅해서 비교

T = int(input())

def bianary_search(last_num, key):
    l = 1
    r = last_num
    cnt = 0  # 탐색 횟수
    while l <= r:
        mid = int((l + r) / 2)
        if mid == key:  # key 값 찾으면 탐색 끝냄
            cnt += 1
            return cnt
        elif mid < key:  # 찾는 key 값이 중간보다 뒤에 있는 경우
            l = mid
            cnt += 1
        else:  # 찾는 key 값이 중간보다 앞에 있는 경우
            r = mid
            cnt += 1

for tc in range(1, T+1):
    last_num, a, b = map(int, input().split())
    if bianary_search(last_num, a) == bianary_search(last_num, b):
        res = 0
    elif bianary_search(last_num, a) < bianary_search(last_num, b):
        res = 'A'
    else:
        res = 'B'

    print("#{} {}".format(tc, res))