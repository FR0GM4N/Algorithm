# 런타임에러 (10개의 테스트케이스 중 9개가 맞았습니다.)
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 런타임에러 -> 메모리를 많이 차지해서 그런듯?
def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, more, equal = [], [], []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)
        else:
            equal.append(num)
    return quick_sort1(less) + equal + quick_sort1(more)


# 더 느려지겠지만 메모리를 절약하는 코드 -> 근데 얘도 런타임에러
# 배열을 리턴하면 안되는 듯? 리턴 안하고 바로 참조해서 값 바꾸도록 해야할듯
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, more, equal = [], [], []
    for _ in range(len(arr)):
        num = arr.pop()
        if num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)
        else:
            equal.append(num)
    return quick_sort2(less) + equal + quick_sort2(more)


for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    print("#{} {}".format(tc, quick_sort1(a)[N // 2]))
    print("#{} {}".format(tc, quick_sort2(a)[N // 2]))