# 0 5 6 0 5 6
arr = list(map(int, input().split()))
print(arr)  #=> [0, 5, 6, 0, 5, 6]

# 056056
# 이 경우는 두자리 숫자는 안됨. 붙어있는 숫자는 그냥 .split()을 안써주면 됨!
arr2 = list(map(int, input()))
print(arr2)  #=> [0, 5, 6, 0, 5, 6]

# kim
arr3 = list(input())
print(arr3)  #=> ['k', 'i', 'm']
