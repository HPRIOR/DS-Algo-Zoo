# start at the top left of a 2d grid.
# How many ways can  you get to the bottom right square?
# You can only move down and right
# Create function grid_traveler(m, n)

def grid_traveler(m: int, n: int, memo={}) -> int:
    # whether or not m,n produce 1 or 0 will be stored here and accessed prior to any computation
    if (m, n) in memo:
        return memo[(m, n)]
    # if we have reached the destination of the grid then this is 1 way to solve the grid
    if m == 1 and n == 1:
        return 1
    # otherwise this is not a route to the end
    if m == 0 or n == 0:
        return 0
    # traverse the grid right and down - as we bubble up the recursive stack, each successful route will be added
    ans = grid_traveler(m, n - 1, memo) + grid_traveler(m - 1, n, memo)
    memo[(m, n)] = ans
    return ans


assert grid_traveler(1, 1) == 1
assert grid_traveler(2, 3) == 3
assert grid_traveler(3, 2) == 3
assert grid_traveler(3, 3) == 6
assert grid_traveler(18, 18) == 2333606220
