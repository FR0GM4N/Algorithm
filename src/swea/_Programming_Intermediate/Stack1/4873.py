import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    S = input()  # 인풋스트링
    stack = []

    # stack에 인풋스트링을 담아가면서 같은 문자가 연속해서 나오면 pop해서 없애주고 아니면 걍 패쓰 -> 총 stack의 길이를 재면 끝!
    for i in range(len(S)):
        # 만약 stack이 비었거나, 스택의 마지막 값이 S와 다를 경우
        if not stack or stack[-1] != S[i]:
            stack.append(S[i])
        # stack에 값이 있고, 그 마지막 값이 인풋스트링과 일치하는 경우(i.e. 연속문자)
        elif stack and stack[-1] == S[i]:
            stack.pop()

    print("#{} {}".format(tc, len(stack)))