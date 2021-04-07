import sys
sys.stdin = open("input.txt")

T = int(input())

def check_babygin(numbers):
    # counter = [0 for _ in range(10)]
    counter = [0] * 10
    is_babygin = 0
    # 카운팅
    for number in numbers:
        counter[number] += 1

    i = 0
    while i < len(counter):
        # triplet check
        if counter[i] >= 3:
            counter[i] -= 3
            is_babygin += 1
            continue

        # run check
        if i < 8:
            if counter[i] and counter[i + 1] and counter[i + 2]:
                counter[i] -= 1
                counter[i + 1] -= 1
                counter[i + 2] -= 1
                is_babygin += 1
                continue

         # 중간 계산 중에 베이비진이 등장했다면
        if is_babygin == 2:
            return 1
        i += 1
    # 전부 돌 때까지 베이비진이 없다면
    if is_babygin != 2:
        return 0

for tc in range(1, T+1):
    numbers = list(map(int, input()))  # 숫자가 붙어있어서 .split() 안해줌
    result = check_babygin(numbers)
    print("#{} {}".format(tc, result))

