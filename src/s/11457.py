import sys
sys.stdin = open("input.txt")

T = int(input())

def gravity_check(numbers):
    # 최고값
    max_value = 0
    for i in range(len(numbers)):
        # 낙차를 하나씩 더해줌
        l = 0
        # 같은 라인의 블록을 만나면 카운트 x
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                l += 1

        if l >= max_value:
            max_value = l
    return max_value


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = gravity_check(numbers)
    print("#{} {}".format(tc, result))
