# can_sum(target, nums) -> whether the target can be reached by sunmming some numbers

def can_sum(target, nums):
    tab = [False for i in range(target + 1)]
    tab[0] = True
    for num in nums:
        tab[num] = True
    for i in range(1, target + 1):
        if tab[i] is True:
            for num in nums:
                if num + i <= target:
                    tab[num + i] = True
    return tab[-1]


assert can_sum(7, [2, 3]) is True
assert can_sum(7, [5, 3, 4, 7]) is True
assert can_sum(7, [2, 4]) is False
assert can_sum(8, [2, 3, 5]) is True
assert can_sum(300, [7, 14]) is False
