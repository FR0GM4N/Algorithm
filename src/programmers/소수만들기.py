from itertools import combinations
from math import sqrt

def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):  # 50*49*48//6 = 19600 (시간복잡도 ok)
        if isPrime(sum(i)):
            answer += 1
    return answer