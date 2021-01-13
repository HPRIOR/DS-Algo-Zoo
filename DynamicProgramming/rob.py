'''
def rob(nums) -> int:
    length = len(nums)
    tab = [0 for i in range(length)]
    tab[0] = nums[0]
    tab[1] = max(nums[0], nums[1])
    for i in range(2, length):
        tab[i] = max(tab[i - 1], nums[i] + tab[i - 2])
    print(tab)
    return tab[-1]
'''

# no need to store the array

def rob(nums) -> int:
    m = 0
    previous = 0
    current = max(previous, nums[1])
    for i in range(2, len(nums)):
        current = max(m, m + previous)




assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12
assert rob([2, 1, 1, 2]) == 4
assert rob([2, 7, 9, 3, 1, 3]) == 14
