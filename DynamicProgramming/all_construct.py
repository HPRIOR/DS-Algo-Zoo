# all construct(target, word_bank) -> all the ways that the target can be constructed by concatonating
# elements of the wordbank array (2d array)
# TODO come back to this question

def all_construct(target: str, word_bank: [str]):
    if target == "":
        return []
    nested_array = []
    for word in word_bank:
        if target.startswith(word):
            answer_array = all_construct(target.removeprefix(word), word_bank)
    return nested_array


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
assert all_construct("purple", ["purp", "p", "ur", "le", "purpl"]) == [["purp", "le"], ["p", "ur", "p", "le"]]
