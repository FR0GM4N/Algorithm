from itertools import permutations
from math import sqrt

def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    tmp = []
    for j in range(1, len(numbers)+1):
        for i in permutations(numbers, j):
            num = int("".join(i))
            if num == 0 or num == 1: continue
            if num not in tmp:
                tmp.append(num)
                if isPrime(num):
                    answer += 1
    return answer