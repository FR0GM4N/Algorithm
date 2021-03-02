# 1대1 가위바위보

import sys
sys.stdin = open("input.txt")

a, b = map(int, input().split())
if a > b:
    winner = 'A'
else:
    winner = 'B'
print(winner)

