"""
return all permutations of an array. e.g.
    [1, 2, 3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import copy


def permutations(arr: []) -> [[]]:
    result = []
    '''
    Base case: if there is just one item left in the array recursion we have bottomed out of the
    tree. in this case we return a copy of it
    '''
    if len(arr) == 1:
        return [arr[:]]
    '''
    otherwise: 
    for each element in the array, we pop off the last element
    '''
    for i in range(len(arr)):
        '''
        the pop method represents the change state, the rest is essentially dfs recursion
        as we go through the recursive 
        '''
        state = arr.pop(0)          # removes and returns first element
        perms = permutations(arr)
        for perm in perms:
            perm.append(state)
        result += perms
        arr.append(state)           # in order to return to the previous state the last transition needs to be added
    return result


print(permutations([1, 2, 3]))
