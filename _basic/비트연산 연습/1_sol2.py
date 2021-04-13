# shift 연산할때마다 2배씩 증가함.
# 인풋이 들어오는대로 앞에서부터 계산하는 방법
# n = 2*n + arr[i]

import sys
sys.stdin = open("1_input.txt")

inp = input()
length = 7
tmp = [inp[i:i+length] for i in range(0, len(inp), length)]

for i in range(len(tmp)):
    ans = 0
    for j in range(7):
        ans = ans * 2 + int(tmp[i][j])
    print(ans)
