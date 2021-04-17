print(int('1110', 2))  # 14
print(int('212', 3))   # 23


num = 0
bit = '1110'
for x in bit:
    num = num*2 + int(x)
print(num)  # 14

num = 0
bit = '212'
for x in bit:
    num = num*3 + int(x)
print(num)  # 23


num = 0
bit = '12345'
for x in bit:
    num = num*10 + int(x)
print(num)  # 12345