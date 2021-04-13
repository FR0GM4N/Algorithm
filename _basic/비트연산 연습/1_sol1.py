import sys
sys.stdin = open("1_input.txt")

inp = input()
length = 7
tmp = [inp[i:i+length] for i in range(0, len(inp), length)]
# tmp = list(map(''.join, zip(*[iter(inp)]*length)))
# tmp = [''.join(x) for x in zip(*[list(inp[z::length]) for z in range(length)])]

for i in range(len(tmp)):
    ans = 0
    for j in range(6, -1, -1):
        if tmp[i][j] == '1':
            ans += 2**(6-j)
    print(ans)