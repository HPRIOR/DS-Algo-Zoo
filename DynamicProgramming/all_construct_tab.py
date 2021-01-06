# all_construct(target, words) -> all the ways that target can be constructed using words or none

def all_construct(target, words):
    if not target:
        return None
    tab = [[] if i == 0 else None for i in range(len(target) + 1)]
    for index, value in enumerate(tab):
        current_slice = target[index:]
        for word in words:
            if current_slice.startswith(word):
                ending_index = len(word) + index
                if tab[ending_index] is None:
                    tab[ending_index] = [word]
                else:
                    tab[ending_index] = tab[ending_index] + [word]
    return tab
## this is wrong needs fixing

all_construct("harry", ["ha", "h", "rr", "y", "harr"])
