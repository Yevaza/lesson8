def InsertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key<A[j]:
            A[j+1]=A[j]
            j -= 1
        A[j+1] = key
z=list(map(int, input("Введите список целых: ").split()))
InsertionSort(z)
print(z)
