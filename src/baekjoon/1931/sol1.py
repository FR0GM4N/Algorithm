# 입력이 10만줄 이상되면 stdin.readline을 사용하는 것이 빠르다.
import sys
N = int(sys.stdin.readline())  # 회의의 수
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a = sorted(a, key=lambda x: (-x[1], -x[0]))
print(a)
cnt = 1
f1, f2 = a.pop()  # 뒤에서부터 체크
while a:
    n1, n2 = a.pop()
    if n1 >= f2:  # 다음 시작이 전회차 끝보다 크거나 같으면 갱신
        f1, f2 = n1, n2
        cnt += 1

print(cnt)