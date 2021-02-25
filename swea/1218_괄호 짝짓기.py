import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    S = input()
    stack = []
    stack.append(S[0])

    for i in range(1, N):
        if S[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif S[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif S[i] == '}' and stack[-1] == '{':
            stack.pop()
        elif S[i] == '>' and stack[-1] == '<':
            stack.pop()
        else:
            stack.append(S[i])

    if len(stack):  # stack이 남아있는 경우
        print("#{} 0".format(tc))
    else:
        print("#{} 1".format(tc))