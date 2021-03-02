import sys
sys.stdin = open("input.txt")

# 버블소트나 셀렉션소트 모두 시간복잡도 O(n^2)으로 큼... 만약 N의 값이 엄청 크면 어쩔꺼임...
# -> 셀렉션 알고리즘을 이용해서 반만 돌려버리는 거임!!

def selection(a, k):
    for i in range(k+1):
        min_idx = i
        for j in range(i+1, len(a)):  # 최솟값 찾기
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k]

N = int(input())
num_lst = list(map(int, input().split()))
print(selection(num_lst, N // 2))