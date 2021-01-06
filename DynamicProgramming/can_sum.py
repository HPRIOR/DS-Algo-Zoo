# can_sum(target, numbers) -> bool: true when it is possible to generate the target sum using the numbers from the array
# elements can be used as many times as needed, elements are non-negative

# Python does not allow mutable values as arguments apparently. 
def can_sum(target: int, numbers: [int], memo=None) -> bool:
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


assert can_sum(7, [2, 3]) is True
assert can_sum(7, [5, 3, 4, 7]) is True
assert can_sum(7, [2, 4]) is False
assert can_sum(8, [2, 3, 5]) is True
assert can_sum(300, [7, 14]) is False
