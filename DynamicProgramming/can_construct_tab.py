# can_construct(target, words) -> true if target can be made through concatonating words otherwise false
import time


def can_construct(target, words):
    if not target:
        return True
    # initialise an array with the first value True, the rest False
    tab = [False if i != 0 else True for i in range(len(target))]
    for index, boolean in enumerate(tab):
        # if we can reach the first item
        if boolean:
            # slice the word from this point
            current_slice = target[index:]
            for word in words:
                # assign true to other reachable points so that we can access them above
                if current_slice.startswith(word):
                    tab[index + len(word) - 1] = True
    return tab[-1]


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
