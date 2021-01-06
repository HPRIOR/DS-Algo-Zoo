# canConstruct(target, wordBank) that accepts a target string and an array of strings
# return a boolean indicating whether or not the target can be constructed by concatenating elements
# in the word bank array

import time
def can_construct(target: str, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    # base case
    if target == '':
        return True
    for word in word_bank:
        if target.startswith(word):
            result = can_construct(target.removeprefix(word), word_bank, memo)
            memo[target] = result
            if result:
                return True
    memo[target] = False
    return False

start_time = time.time()
assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
assert can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == False
assert can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                     [
                         "e",
                         "ee",
                         "eee",
                         "eeee",
                         "eeeee",
                         "eeeeee"
                     ]
                     ) == False
assert can_construct("", ["asda", "sadsd", "asdasd"]) == True
print(time.time() - start_time)