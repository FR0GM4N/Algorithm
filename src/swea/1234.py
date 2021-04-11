import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N, S = input().split()
    stack = []

    for i in range(int(N)):
        if not stack or stack[-1] != S[i]:
            stack.append(S[i])
        elif stack[-1] == S[i]:
            stack.pop()

    print("#{} {}".format(tc, "".join(stack)))

