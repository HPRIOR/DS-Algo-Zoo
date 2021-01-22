"""
return all subsets from array: [1,2] -> [], [1], [1,2], [2]
"""


def subsets(array):
    ans = []
    visited = set()

    def helper(subset, index):
        if tuple(subset) not in visited:
            visited.add(tuple(subset))
            ans.append(subset)
        if index == len(array):
            return
        helper(subset[:], index + 1)
        new_subset = subset[:]
        new_subset.append(array[index])
        helper(new_subset, index + 1)
    helper([], 0)
    print(ans)


subsets([1, 2, 3])
