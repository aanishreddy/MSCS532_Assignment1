# insertion_sort_descending.py
# Course: MSCS-532 - Algorithms and Data Structures
# Assignment 1: Insertion Sort in Decreasing Order

def insertion_sort_desc(arr):
    """Perform insertion sort on a list in decreasing order."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Test code
if __name__ == "__main__":
    data = [8, 3, 5, 1, 9, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_desc(data)
    print("Sorted array (decreasing):", sorted_data)
