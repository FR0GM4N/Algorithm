import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    S = input().split()
    stack = []
    operator = ['*', '/', '+', '-']
    res = 1
    for s in S:
        # 숫자인 경우
        if s != '.' and s not in operator:
            stack.append(s)
        elif s == '.':
            break
        else:
            try:  # 연산자인 경우
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if s == '+':
                    stack.append(n1 + n2)
                elif s == '-':
                    stack.append(n1 - n2)
                elif s == '*':
                    stack.append(n1 * n2)
                elif s == '/':
                    stack.append(n1 // n2)
            except:  # 스택이 비었거나 <숫자 숫자 연산자> 순이 아닐때
                res = 0

    if res == 1 and len(stack) == 1:
        print("#{} {}".format(tc, stack.pop()))
    elif res == 0 or len(stack) > 1:
        print("#{} error".format(tc))