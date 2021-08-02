def solution(lottos, win_nums):
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    score = [0, 0]
    for i in lottos:
        if i in win_nums:
            score[0] += 1
            score[1] += 1
        if i == 0:
            score[0] += 1
    answer = [dic[score[0]], dic[score[1]]]  # 최고 순위, 최저 순위
    return answer