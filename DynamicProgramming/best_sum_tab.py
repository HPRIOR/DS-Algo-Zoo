# best_sum(target, num) -> [shortest answer] or None

def best_sum(target, nums):
    tab = [None for i in range(target + 1)]
    tab[0] = []
    for i in range(1, target + 1):
        if i in nums:
            tab[i] = []
    for i in range(target + 1):
        for num in nums:
            if tab[i] is not None and num + i <= target:
                new = tab[i] + [num]
                current = tab[i + num]
                # if current is not None produced error
                # if not current checks for nonzero, whereas the former
                # compares with None
                if not current or len(new) <= len(current):
                    tab[i + num] = new
    return tab[-1]


assert best_sum(7, [5, 3, 4, 7]) == [7]
assert best_sum(8, [1, 4, 5]) == [4, 4]
assert best_sum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]
