# can_sum(target, numbers) -> bool: true when it is possible to generate the target sum using the numbers from the array
# elements can be used as many times as needed, elements are non-negative

# Python does not allow mutable values as arguments apparently. The same dictionary will be used each time
# the function is called. Declaring a defualt value of none makes the function behave.

def can_sum(target: int, numbers: [int], memo=None) -> bool:

    if memo is None:
        memo = {}
    # checks if current value has True or False associated with it
    if target in memo:
        return memo[target]
    # True is returned given a 0 is found e.g. a sequence from the list can add to the target
    if target == 0:
        return True
    # otherwise a minus value indicates that the sequence does not add to target
    if target < 0:
        return False
    # if the current value is not negative and is not 0, we will repeat a call to this function
    # for each of the remainders of this value and the numbers from the list
    for num in numbers:
        remainder = target - num
        # a returned 0 from the bottom of the call stack will propagate upwards
        if can_sum(remainder, numbers, memo):
            memo[target] = True
            # returning the value here will cause the recursion to end before reaching the next section
            return True

    memo[target] = False
    return False


assert can_sum(7, [2, 3]) is True
assert can_sum(7, [5, 3, 4, 7]) is True
assert can_sum(7, [2, 4]) is False
assert can_sum(8, [2, 3, 5]) is True
assert can_sum(300, [7, 14]) is False
