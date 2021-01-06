# how_sum(target, numbers)
# return anarray containing any combination of elements that add up to exactly the target sum
# null returned if not combination that addes up to the target some

# base case == null or []

def how_sum(target, numbers: [int], memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        difference = target - num
        possible_array = how_sum(difference, numbers)
        if possible_array is not None:
            # value of the number which the difference is derived from is appended to the cumulative
            # array such that only those values which contributed to the base case of 0 are returned.
            # either None will propagate upwards, or an array which will be populated
            ans = possible_array + [num]
            memo[target] = ans
            return ans


print(how_sum(7, [2, 3]))
assert how_sum(7, [2, 3]) == [3, 2, 2]
assert how_sum(7, [5, 3, 4, 7]) == [4, 3]
assert how_sum(7, [2, 4]) is None
assert how_sum, (8, [2, 3, 5]) == [2, 2, 2, 2]
assert how_sum(300, [7, 14]) is None
