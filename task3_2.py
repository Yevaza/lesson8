def balance_array(arr):
    positive_sum, negative_sum = sum(x for x in arr if x > 0), sum(x for x in arr if x < 0)
    arr.append(abs(positive_sum) - abs(negative_sum))
    return arr

result_array = balance_array(list(map(int, input().split())))
print(result_array, sum(x for x in result_array if x > 0), abs(sum(x for x in result_array if x < 0)), "need", abs(sum(x for x in result_array if x < 0)))