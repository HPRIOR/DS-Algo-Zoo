"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

"""
def rotate_array(nums: [int], k: int):
    if not nums:
        return
    new_start_index = len(nums) - k
    new_arr = nums[new_start_index:] + nums[:new_start_index]
    for i in range(len(new_arr)):
        nums[i] = new_arr[i]

"""
def rotate_array(nums: [int], k : int):
    """
    this doens't work with all test cases
    :param nums:
    :param k:
    :return:
    """
    if not nums:
        return
    new_start_index = len(nums) - k
    temp_array = []
    i = 0
    while i < k + 1:
        temp_array.append(nums[i])
        i += 1
    i = 0
    j = 0
    n = new_start_index
    while i < len(nums):
        if n < len(nums):
            nums[i] = nums[n]
            n += 1
        if i >= new_start_index - 1:
            nums[i] = temp_array[j]
            j += 1
        i += 1
    return nums



assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]



assert rotate_array([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
