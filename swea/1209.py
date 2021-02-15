import sys
sys.stdin = open("input.txt")

def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

for _ in range(1, 11):
    tc = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(100)]

    # 각 행, 열, 대각선의 합을 비교할 빈 리스트 만들어줌.
    sum_lst = []

    # 리스트 순회하면서 값 저장
    # 1. 각 행의 합
    for i in range(100):
        total = 0
        for j in range(100):
            total += num_lst[i][j]
        sum_lst.append(total)

    # 2. 각 열의 합
    for j in range(100):
        total = 0
        for i in range(100):
            total += num_lst[i][j]
        sum_lst.append(total)

    # 3. 대각선의 합
    for i in range(100):
        total_1, total_2 = 0, 0
        total_1 += num_lst[i][i]
        total_2 += num_lst[99-i][99-i]
        sum_lst.append(total_1)
        sum_lst.append(total_2)

    # 버블정렬 한 후 리스트의 맨 뒤 값이 max 값이므로 출력
    print("#{} {}".format(tc, bubble_sort(sum_lst)[-1]))
