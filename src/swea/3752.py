import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [1] + [0] * sum(score)  # 방문체크할 리스트

    tmp = [0]
    for ele in score:
        for i in range(len(tmp)):
            if not visited[ele+tmp[i]]:
                visited[ele+tmp[i]] = 1  # 방문체크
                tmp.append(ele+tmp[i])
    print('#{} {}'.format(tc, len(tmp)))

