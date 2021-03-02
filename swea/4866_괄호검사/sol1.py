import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    S = input()  # 인풋 스트링
    stack = []
    for s in S:
        # 괄호인 애들만 체킹
        if s == '{' or s == '(':
            stack.append(s)
        elif s == '}' or s == ')':
            # stack이 비어있으면 추가하고 break. 어차피 뒤쪽을 봐야 이미 짝이 안맞기 때문
            if not stack:
                stack.append(s)
                break
            # s랑 stack의 마지막 요소랑 다른 괄호이면 역시 그냥 더해주고 break. 어차피 제대로 된 짝이 아니니까
            elif (s == '}' and stack[-1] != '{') or (s == ')' and stack[-1] != '('):
                stack.append(s)
                break
            # 위의 경우에 모두 해당 안되면(i.e. 제대로 짝이 맞는 경우)
            else:
                stack.pop()

    # stack의 길이가 0이 아니면(i.e. 괄호가 남아있다는 의미)
    if len(stack):
        print("#{} 0".format(tc))
    # stack의 길이가 0인 경우(i.e. 짝이 잘 맞았다는 의미)
    else:
        print("#{} 1".format(tc))