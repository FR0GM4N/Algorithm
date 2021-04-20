import sys
sys.stdin = open("sample_input.txt")


T = int(input())

def quick_sort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        if p == N // 2:
            return  # 답 찾아서 퀵정렬 중단
        elif p > N // 2:
            quick_sort(a, l, p-1)
        elif p < N // 2:
            quick_sort(a, p+1, r)

def partition(a, l, r):
    pivot = (l + r) // 2
    while l < r:
        while a[l] < a[pivot] and l < r:
            l += 1
        while a[r] >= a[pivot] and l < r:
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            a[l], a[r] = a[r], a[l]
    a[pivot], a[r] = a[r], a[pivot]
    return r


for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    quick_sort(a, 0, len(a) - 1)
    print("#{} {}".format(tc, a[N // 2]))