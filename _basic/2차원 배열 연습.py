a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 2차원 리스트 출력 1
for i in range(len(a)):  # 가로행 길이 (3)
    for j in range(len(a[0])):  # 세로열 길이 (4)
        print(a[i][j], end=' ')
    print()
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12


# 2차원 리스트 출력 2
for i in range(len(a)):
    for j in range(len(a[0])):
        print('%3d ' % a[i][j], end='')  # 3칸 떨어져서 출력됨
    print()
#   1   2   3   4
#   5   6   7   8
#   9  10  11  12