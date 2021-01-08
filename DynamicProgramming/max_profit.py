def max_profit( prices: 'List[int]') -> 'int':
    min_val = float('inf')
    ans = 0
    for i in range(len(prices)):
        current_price = prices[i]
        # get minimum value
        if current_price < min_val:
            min_val = current_price
        # maximum of the difference between any item in the array and the minimum found value
        ans = max(ans, current_price - min_val)
    return ans


print(max_profit([1, 2, 4]))
assert max_profit([7, 1, 5, 3, 6, 4]) == 5

assert max_profit([7, 6, 5, 4, 3, 1]) == 0
