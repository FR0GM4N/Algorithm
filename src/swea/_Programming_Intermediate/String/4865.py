import sys
sys.stdin = open("input.txt")

'''
1. str1 순회하면서 알파벳들 딕셔너리에 키 값으로 추가 & value는 전부 0으로 세팅
2. srt2 순회하면서 문자가 딕셔너리에 키 값에 있으면 value 값을 +1
3. 딕셔너리 순회하면서 value 가장 큰 값 출력
'''

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # 빈 딕셔너리 만들어주기
    result = {}

    # 1. str1 순회하면서 알파벳들 딕셔너리에 키 값으로 추가 & value는 전부 0으로 세팅
    for s in str1:
        result[s] = 0

    # 2. srt2 순회하면서 문자가 딕셔너리에 키 값에 있으면 value 값을 +1
    for s in str2:
        if s in result:
            result[s] += 1

    # 3. 딕셔너리 순회하면서 value 가장 큰 값 출력
    max_cnt = 0
    for k, v in result.items():
        if v > max_cnt:
            max_cnt = v

    print("#{} {}".format(tc, max_cnt))

