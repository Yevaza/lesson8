def nearest_numbers(nums):
    sorted_nums=sorted(nums)
    result_pair=min(zip(sorted_nums, sorted_nums[1:]), key=lambda pair: pair[1] - pair[0])
    return result_pair
numbers=list(map(int,input("Список чисел: ").split()))

result=nearest_numbers(numbers)
print("Ближайшие числа друк к другу: ",result)