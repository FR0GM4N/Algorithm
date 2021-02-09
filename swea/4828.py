# 4828_min max

# 풀이 1
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    result = max_num - min_num
    print("#{} {}".format(tc, result))


# 풀이 2 (버블소트 이용)
# but, 버블소트는 O(n^2)의 시간이 걸림.. 구림..
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def bubblesort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    a = bubblesort(numbers)
    result = a[N-1] - a[0]
    print("#{} {}".format(tc, result))