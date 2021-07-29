# 스택이용
def solution(board, moves):
    stack = []  # 스택
    cnt = 0  # answer
    for i in moves:  # moves를 순회하면서
        for row in range(len(board)):
            if board[row][i - 1]:  # 0이 아니면, stack에 넣고 0으로 바꾸기
                stack.append(board[row][i - 1])
                board[row][i - 1] = 0
                break

        # 만약 stack에 같은 숫자가 있으면 삭제 후 카운트
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                cnt += 2
                stack.pop()
                stack.pop()
    return cnt