def binary_search(val, array: []) -> bool:
    sorted_array = sorted(array)

    def search(s_array):
        print(s_array)
        mid = len(s_array) // 2
        if s_array[mid] == val:
            return True
        if mid == 0:
            return False
        if s_array[mid] > val:
            if search(s_array[:mid]):  # repeat call on greater side of list exclusive
                return True
        else:
            if search(s_array[mid:]):  # repeat call on smaller side of list inclusive
                return True
        return False

    return search(sorted_array)


print(binary_search(1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(4, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(6, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(7, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(8, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
