# how_sum(target, nums) -> [one way in which we can sum to produce the target] or None

def how_sum(target, nums):
    tab = [None for i in range(target + 1)]
    tab[0] = []
    for num in nums:
        if num < target:
            tab[num] = []
    for i in range(target + 1):
        for num in nums:
            if num + i <= target and tab[i] is not None:
                tab[num + i] = tab[i] + [num]
    return tab[-1]


assert how_sum(7, [2, 3]) == [3, 2, 2]
assert how_sum(7, [5, 3, 4, 7]) == [4, 3]
assert how_sum(7, [2, 4]) is None
assert how_sum, (8, [2, 3, 5]) == [2, 2, 2, 2]
assert how_sum(300, [7, 14]) is None
