# best_sum(target, numbers) -> [shortest array that sums to target]


def best_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    # this will store the shortest combination
    # importantly it's outside of the recursive loop
    shortest_combination = None

    for num in numbers:
        difference = target - num
        cumulative_array = best_sum(difference, numbers, memo)
        if cumulative_array is not None:
            # bubble up the array if a 0 has been found, and store the way to get there as you
            # come up the tree
            combined_array = cumulative_array + [num]
            if shortest_combination is None or len(combined_array) < len(shortest_combination):
                shortest_combination = combined_array
    # no early return after a conditional as in other similar problem, entire tree checked
    # nodes higher up the tree will compete for the shortest combination until the highest node
    memo[target] = shortest_combination
    return shortest_combination


assert best_sum(7, [5, 3, 4, 7]) == [7]
assert best_sum(8, [1, 4, 5]) == [4, 4]
assert best_sum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]
