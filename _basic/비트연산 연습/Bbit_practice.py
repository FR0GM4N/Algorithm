def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        # i & (1 << j) : i의 j번째 비트가 1인지 검사 [b7, b6, ..., b0]
        output += "1" if i & (1 << j) else "0"
    print(output)


for i in range(-5, 6):
    print("%2d = " % i, end="")
    Bbit_print(i)