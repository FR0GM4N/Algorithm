# 내가 처음 푼 풀이. 슬라이싱을 생각하지 못해 괜히 복잡하게 풀었다..

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    input_str = input()
    # 패턴의 최대길이가 10이므로 일단 10만큼 자르고 얘를 input_str과 비교할거임
    p = input_str[:10]

    # i: 인풋문자열 인덱스, j: 패턴 인덱스
    # 패턴의 길이가 10인 경우 idx 10까지는 가야 체킹됨
    for i in range(11):
        i += 1
        check = 0  # 같은지 체크하는 변수. 누적합이 10이면 패턴10글자가 전부 일치한다는 소리
        for j in range(10):
            if input_str[i + j] == p[j]:
                check += 1
            else:
                break
        # 누적합이 10이면 반복문 종료하고 output 출력
        if check == 10:
            ans = i
            break

    print("#{} {}".format(tc, ans))

