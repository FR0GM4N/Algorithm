#  string 정렬 : ['100000000000000000', '119', '1195524421', '2', '97674223']
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            answer = False
            break
    return answer
