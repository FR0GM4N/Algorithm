def cal(i, tmp):
    global ans
    if i == N:  # tmp 계산
        for idx, val in enumerate(tmp):
            if len(val) == 3:  # 괄호 계산 ('3+8')
                tmp[idx] = str(eval(val))
        res = tmp[0]
        for op in range(1, len(tmp), 2):
            res = eval(str(res)+tmp[op]+tmp[op+1])

        if ans < res:  # 최대값 갱신
            ans = res
        return

    tmp.append(s[i])
    cal(i+1, tmp)
    del tmp[-1]

    if tmp[-1] in operator and i+3 <= N:  # 맨 마지막이 연산자이면서 자릿수 부족하면
        tmp.append(s[i:i+3])  # 괄호 넣기 ('9*2')
        cal(i+3, tmp)
        del tmp[-1]


N = int(input())
s = input()
ans = -2**31
operator = ['+', '-', '*']

if N == 1:
    print(max(ans, int(s)))
    quit()

cal(1, [s[0]])  # idx, tmp
print(ans)