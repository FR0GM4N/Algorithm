answer = 0

def dfs(value, idx, numbers, target):  # 현재값, 인덱스
    global answer
    if idx == len(numbers):
        if value == target:
            answer += 1
        return
    dfs(value+numbers[idx], idx+1, numbers, target)
    dfs(value-numbers[idx], idx+1, numbers, target)

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer