# insertion_sort_descending.py
# Course: MSCS-532 - Algorithms and Data Structures
# Assignment 1: Insertion Sort in Decreasing Order
# Reference: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.

"""
This program demonstrates the Insertion Sort algorithm that sorts
a given list of numbers in *monotonically decreasing* order.

Algorithm logic:
1. Start from the second element in the list (index 1).
2. Compare the current element (key) with the elements before it.
3. Shift all elements that are *smaller* than the key one position ahead.
4. Insert the key into the correct position to maintain decreasing order.
5. Repeat until the entire list is sorted.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort_desc(arr):
    """Sorts a list in decreasing order using the insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]          # Current element to be compared
        j = i - 1             # Index of the previous element

        # Shift all smaller elements to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key element in its correct position
        arr[j + 1] = key

    return arr


# Example usage
if __name__ == "__main__":
    # Example data for testing
    data = [14, 9, 27, 3, 18, 7]
    print("Original array:", data)

    sorted_data = insertion_sort_desc(data)
    print("Sorted array (decreasing order):", sorted_data)
