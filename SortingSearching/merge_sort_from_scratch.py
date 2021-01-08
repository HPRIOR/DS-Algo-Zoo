def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # find mid point of array
        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursive calls modify the right and left halves
        # prior to computation at the end of the function
        merge_sort(left_half)
        merge_sort(right_half)

        # iterator for traversing two halves
        i = j = 0
        # iterator for main list
        k = 0

        while i < len(left_half) and j < len(right_half):
            # make the value of k the smallest of either the right half
            # and left half of the array. Will stop when either empty
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            # each step of this loop iterates through the main array with index k
            k += 1

        # these ensure that remaining values are added to the array
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [2,5,6,7,8,4,2,3,6,3,2,1]
merge_sort(arr)
print(arr)


