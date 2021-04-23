import sys
sys.stdin = open("s_input.txt")

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    relations = []
    for _ in range(M):
        relations.append(list(map(int, input().split())))

    parent = [i for i in range(N+1)]
    for i in range(M):
        x, y = relations[i][0], relations[i][1]
        union(x, y)

    res = set()
    for i in range(1, N+1):
        res.add(find_set(i))
    
    print("#{} {}".format(tc, len(res)))

