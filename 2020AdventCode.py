def find_product_of_sum(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]


# Example usage
input_nums = [1721, 979, 366, 299, 675, 1456]
result = find_product_of_sum(input_nums)
print(result)  # prints 514579
