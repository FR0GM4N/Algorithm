import itertools

# 순열
arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))  #=> [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 조합
arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))  #=> [('A', 'B'), ('A', 'C'), ('B', 'C')]