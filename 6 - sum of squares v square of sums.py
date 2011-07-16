MAX_VAL = 100

nums = range(1, MAX_VAL + 1)
sum_of_squares = sum(x*x for x in nums)
square_of_sum = sum(nums)**2

print(square_of_sum - sum_of_squares)