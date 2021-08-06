def solution(answers):
    answer = []
    dic = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    length = len(answers)
    max_cnt = 0
    for i in range(1, 4):
        cnt = 0
        q = length // len(dic[i])
        r = length % len(dic[i])
        tmp = (dic[i] * q) + (dic[i][:r])
        for j in range(len(answers)):
            if answers[j] == tmp[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            answer = []
            answer.append(i)
        elif cnt == max_cnt:
            answer.append(i)

    return answer