def solution(s):
    answer = ''
    dict = {'ze':['0',4], 'on':['1',3], 'tw':['2',3], 'th':['3',5], 'fo':['4',4], 'fi':['5',4], 'si':['6',3], 'se':['7',5], 'ei':['8',5], 'ni':['9',4],} # [value, len]
    i = 0
    nums = ['0','1','2','3','4','5','6','7','8','9']
    while i < len(s):
        if s[i] in nums:
            answer += s[i]
            i += 1
        else:
            answer += dict[s[i:i+2]][0]
            i += dict[s[i:i+2]][1]
    return int(answer)