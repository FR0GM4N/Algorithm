import sys
sys.stdin = open("sample_input.txt")

# 같은 카드인 경우 인덱스가 작은 애가 winner
def win(first, second):
    # 1:가위, 2: 바위, 3:보 -> 1<2 / 2<3 / 3<1
    winner = first
    if a[first] == 1 and a[second] == 2:
        winner = second
    if a[first] == 2 and a[second] == 3:
        winner = second
    if a[first] == 3 and a[second] == 1:
        winner = second
    return winner


# 리스트를 두개로 분류하는 작업이 필요함. 도대체 어케 분리? -> 인덱스로 접근
def divide(s, e):  # s:처음 인덱스, e: 끝 인덱스
    if s == e:  # 요소가 하나일때
        return s
    else:
        first = divide(s, (s+e)//2)
        second = divide((s+e)//2 +1, e)
        return win(first, second)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    ans = divide(0, N-1) + 1
    print("#{} {}".format(tc, ans))

