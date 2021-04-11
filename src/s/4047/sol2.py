import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    card = input()
    card_set = set()

    S, D, H, C = 13, 13, 13, 13
    for i in range(len(card) // 3):
        card_set.add(card[i*3:i*3+3])
        if card[i*3] == 'S':
            S -= 1
        elif card[i*3] == 'D':
            D -= 1
        elif card[i*3] == 'H':
            H -= 1
        elif card[i*3] == 'C':
            C -= 1

    if len(card_set) != 4:
        print("#{} ERROR".format(tc))
    else:
        print("#{} {} {} {} {}".format(tc, S, D, H, C))