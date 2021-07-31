def solution(numbers, hand):
    phone = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    answer = ''
    lx, ly, rx, ry = 3, 0, 3, 2
    for num in numbers:
        r,c = phone[num]
        if c == 0:
            answer += 'L'
            lx, ly = r, c
        elif c == 2:
            answer += 'R'
            rx, ry = r, c
        elif c == 1:
            abs_l = abs(r-lx)+abs(c-ly)
            abs_r = abs(r-rx)+abs(c-ry)
            if abs_l == abs_r:
                if hand == "right":
                    answer += 'R'
                    rx, ry = r, c
                else:
                    answer += 'L'
                    lx, ly = r, c
            elif abs_l > abs_r:  # 오른쪽
                answer += 'R'
                rx, ry = r, c
            else:  # 왼쪽
                answer += 'L'
                lx, ly = r, c
    return answer