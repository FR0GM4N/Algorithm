import itertools

# 순열
arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# 조합
arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))