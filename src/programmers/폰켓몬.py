# 중복제거 -> set 이용
def solution(nums):
    length = len(nums) // 2  # N//2
    if len(set(nums)) <= length:  # 중복제거한 개수가 N//2보다 작으면 set개수 리턴
        answer = len(set(nums))
    else:  # 중복제거한게 N//2보다 크면 N//2 리턴
        answer = length
    return answer
