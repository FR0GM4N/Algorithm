str1 = '1234'  # <type: str>
int1 = 1234  # <type: int>

# str -> int
def atoi(my_str):
    my_int = 0
    for i in my_str:
        my_int *= 10
        my_int += ord(i) - ord('0')
    return my_int

print(atoi(str1)) #=> 1234  <type: int>


# int -> str
def itoa(my_int):
    # ord 함수 사용하여 아스키 코드 값으로 변환
    my_str = []
    while my_int != 0:
        r = my_int % 10
        num = chr(ord('0') + r)
        my_str.append(num)
        my_int //= 10

    my_str.reverse()
    return ''.join(my_str)
    # reverse 안하고 바로 return ''.join(my_str)[::-1] 해줘도 됨
print(itoa(int1))