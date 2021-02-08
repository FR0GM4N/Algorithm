# arr = [] 리스트 입력

def BubbleSort(a) :
    for i in range(len(a)-1, 0, -1) :
        for j in range(0, i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
BubbleSort(arr)
print(arr)