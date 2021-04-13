import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    # k: 한번 충전 후 최대로 이동 가능한 정류장 수, n: 종점 정류장 번호, m: 충전기 설치된 정류장 개수
    k, n, m = map(int, input().split())
    # 충전기 설치 된 정류장 번호 리스트
    charge = list(map(int, input().split()))

    # 충전기 설치된 정류장은 1, 없으면 0으로 설정
    bus_stop = [0] * (n+1)
    for i in charge:
        bus_stop[i] = 1

    bus = 0  # 버스 위치
    cnt = 0  # 충전횟수

    # 끝낼 수만 있다면 무한으로 돌려서 확인
    while True:
        # 버스가 이동할 수 있는 만큼 이동하자
        bus += k
        if bus >= n:
            break  # 종점에 도착하거나 종점지나 더 나아간 경우

        for i in range(bus, bus-k, -1):
            if bus_stop[i]:
                cnt += 1
                bus = i
                break
        # 충전기를 못 찾았을 때
        else:
            cnt = 0
            break

    print("#{} {}".format(tc, cnt))


