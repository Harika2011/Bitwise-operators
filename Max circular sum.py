def max_circular_subarray_sum(arr):
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def min_kadane(nums):
        min_ending_here = min_so_far = nums[0]
        for x in nums[1:]:
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far

    total_sum = sum(arr)
    max_kadane_sum = kadane(arr)
    min_kadane_sum = min_kadane(arr)

    if max_kadane_sum < 0:
        return max_kadane_sum

    return max(max_kadane_sum, total_sum - min_kadane_sum)

arr = [8, -1, 3, 4]
print("Max circular subarray sum is:", max_circular_subarray_sum(arr))
