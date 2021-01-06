# countConstruct(target, word_bank) -> number of ways that target can be constructed from wordbank

def count_construct(target: str, word_bank: [str], memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    num_ways = 0
    for word in word_bank:
        if target.startswith(word):
            num_ways += count_construct(target.removeprefix(word), word_bank, memo)
    memo[target] = num_ways
    return num_ways


assert count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
assert count_construct("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
assert  count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                     [
                         "e",
                         "ee",
                         "eee",
                         "eeee",
                         "eeeee",
                         "eeeeee"
                     ]
                     ) == 0
