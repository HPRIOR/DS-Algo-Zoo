"""
given an array of numbers from 0-2, sort an array such that it is in the order
0,1,2
The solution is to have 3 pointers
p1: right-most boundary of 0's
p2: left-most boundary of 2's
current: pointer under evaluation for swapping
"""


def dutch_flag(nums):
    p1 = current = 0
    p2 = len(nums) - 1

    while current <= p2:
        if nums[current] == 0:
            nums[current], nums[p1] = nums[p1], nums[current]
            p1 += 1
            current += 1
        if nums[current] == 2:
            nums[current], nums[p2] = nums[p2], nums[current]
            p2 -= 1
        if nums[current] == 1:
            current += 1
    return nums


assert dutch_flag([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
