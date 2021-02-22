import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    card = input()

    S = [0] * 14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14

    res = True
    for i in range(4):  # 알파벳 인덱스: 0,3,6,9
        if card[i * 3] == 'S':
            if S[int(card[i * 3 + 1:i * 3 + 3])] == 1:
                res = False
                break
            S[int(card[i * 3 + 1:i * 3 + 3])] += 1
        elif card[i * 3] == 'D':
            if D[int(card[i * 3 + 1:i * 3 + 3])] == 1:
                res = False
                break
            D[int(card[i * 3 + 1:i * 3 + 3])] += 1
        elif card[i * 3] == 'H':
            if H[int(card[i * 3 + 1:i * 3 + 3])] == 1:
                res = False
                break
            H[int(card[i * 3 + 1:i * 3 + 3])] += 1
        elif card[i * 3] == 'C':
            if C[int(card[i * 3 + 1:i * 3 + 3])] == 1:
                res = False
                break
            C[int(card[i * 3 + 1:i * 3 + 3])] += 1

    if res is True:
        print("#{} {} {} {} {}".format(tc, 13 - S.count(1), 13 - D.count(1), 13 - H.count(1), 13 - C.count(1)))
    else:
        print("#{} ERROR".format(tc))