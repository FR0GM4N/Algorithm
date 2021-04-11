import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    A = int(input())  # A: 원본숫자
    # 문제점 : 이렇게 하면 012312 이런 숫자가 12312로 됨.. 맨 앞의 0이 인식이 안됨
    C = [0] * 10  # C : 카운팅 리스트

    # 1. 카운팅
    length = 0
    for i in range(6):
        C[A % 10] += 1
        A //= 10
        length += 1

    # 2. 맨 앞의 체크 안되는 0 문제 해결
    if length < 6:
        C[0] += 6 - length

    i = 0
    triplet = 0
    runn = 0
    # 2. 순회하면서 triplet, run 체크
    while i < 10:
        if C[i] >= 3:
            triplet += 1
            C[i] -= 3
            continue
        if C[i] >= 1 and C[i+1] >= 1 and C[i+2] >= 1:
            runn += 1
            C[i] -= 1
            C[i+1] -= 1
            C[i+2] -= 1
            continue
        i += 1

    if triplet + runn == 2:
        result = 1
    else:
        result = 0
    print("#{} {}".format(tc, result))