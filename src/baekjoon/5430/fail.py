import sys
sys.stdin = open("input.txt")

def sol(p, n):
    flag = 0  # 짝
    delete = [0, 0]
    # 홀이면 뒤집(뒷 숫자 삭제), 짝이면 stay(앞 숫자 삭제)
    for s in p:
        if s == 'R' and flag == 0:
            flag = 1
        elif s == 'R' and flag == 1:
            flag = 0
        elif s == 'D' and flag == 0:
            delete[0] += 1
        elif s == 'D' and flag == 1:
            delete[1] += 1
        if sum(delete) >= n:
            return 'error'

    # 삭제하고 뒤집
    res = num_lst[delete[0]:len(num_lst) - delete[1]]
    if flag:
        res.reverse()
    return "["+",".join(res)+"]"


T = int(input())
for tc in range(1, T+1):
    p = input()  # 수행할 연산
    n = int(input())  # 배열에 들어있는 숫자 개수
    num_lst = input()[1:-1].split(',')
    print(sol(p, n))

