def Selection_sort(A):
    result=[]
    while A:
        result.append(A.pop(A.index(max(A))))
    return result
    
a=list(map(int, input("Введите список целых: ").split()))
print(Selection_sort(a))
