# max_subarray(nums) -> maximum contiguous sub array

def max_subarray(nums: [int]) -> int:
    # this will store the maximum subarray for each index
    if len(nums) == 1:
        return nums[0]
    if not nums:
        return 0
    memo = {0: nums[0]}
    global_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(memo[i-1] + nums[i], nums[i])
        if current_max > global_max:
            global_max = current_max
        memo[i] = current_max
    return global_max

print(max_subarray([1, -3, 2, 1, -1]))


# As with all dp problems the solution entails keeping a cumulative record of sub problems, which we can
# use as we progress through the solution. In this case, as we move through the array, we tally the the
# the maximum value between the current index itself, and adding this index to the previously largest subarray.
# Hence at each stage we are sorting the maximum sub array up to that point, and using this as a basis for the
# next index. At the same time we are keeping a global maximum value, which to compare each index, current_max
# that is above this will be the new global_max. This is what is reterned at the end


