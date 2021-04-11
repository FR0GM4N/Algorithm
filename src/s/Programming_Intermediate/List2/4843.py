import sys
sys.stdin = open("input.txt")

# 원본 리스트를 내림차순으로 정렬하고 mid~min 애들 반복문 돌리면서 맨 뒤의 값부터 앞에 사이사이 껴 넣기

# 내림차순 정렬 함수
def descending_sort(a):
    for i in range(len(a)):
        max_idx = i
        for j in range(i+1, len(a)):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수 개수
    a = list(map(int, input().split()))

    # 원본리스트 내림차순 정렬
    descending_sort(a)

    # mid~min 애들 반복문 돌리면서 맨 뒤의 값부터 사이사이 껴 넣기...를 할랬으나 insert와 pop을 안쓰고는 못하겠어서 일단 썼음...
    for i in range(1, N, 2):
        k = a.pop(-1)
        a.insert(i, k)

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(a[i], end=" ")
    print()