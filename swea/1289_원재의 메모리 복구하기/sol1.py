import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    memory = input()

    cnt = 0
    for i in range(1, len(memory)):
        if memory[i] != memory[i-1]:
            cnt += 1

    # 맨 처음 숫자가 1이면 이것도 카운팅 해야함
    if memory[0] == '1':
        cnt += 1

    print("#{} {}".format(tc, cnt))

