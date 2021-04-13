# 충전기 설치 된 정류장 번호 리스트를 만들고 걔네들 사이의 간격이 k보다 크면 0 리턴하는 방법

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    # k: 한번 충전 후 최대로 이동 가능한 정류장 수, n: 종점 정류장 번호, m: 충전기 설치된 정류장 개수
    k, n, m = map(int, input().split())
    # 충전기 설치 된 정류장 번호 리스트
    charge = list(map(int, input().split()))
    cnt = 0  # 충전횟수

    # 세개 다 같은 코드임
    charge = [0] + charge + [n]
    # charge.insert(0,0)
    # charge.append(n)

    last = 0  # 마지막 위치

    # 충전소에 출발점과 도착지를 넣어놓았으므로
    for i in range(1, m+2):
        if charge[i] - charge[i-1] > k:
            cnt = 0
            break

        # 갈 수 있다면 아무작업 X
        # 갈 수 없다면 내 바로직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + k:
            last = charge[i-1]
            cnt += 1

    print("#{} {}".format(tc, cnt))

