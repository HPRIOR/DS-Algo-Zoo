def count_construct(target, words):
    if not target:
        return 0
    tab = [0 if i != 0 else 1 for i in range(len(target) + 1)]
    for index, value in enumerate(tab):
        current_slice = target[index:]
        print("current slice: " + current_slice)
        for word in words:
            if current_slice.startswith(word):
                # add the value of this index to the last character's index
                ending_index = len(word) + index
                print("----", word, ending_index)
                tab[ending_index] += tab[index]
                print(tab)

    return tab[-1]


assert count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
# assert count_construct("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
# assert count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#                       [
#                           "e",
#                           "ee",
#                           "eee",
#                           "eeee",
#                           "eeeee",
#                           "eeeeee"
#                       ]
#                       ) == 0
