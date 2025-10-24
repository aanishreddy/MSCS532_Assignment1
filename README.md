# MSCS532_Assignment1 – Insertion Sort (Decreasing Order)

## 📘 Course Information
**Course:** MSCS-532 – Algorithms and Data Structures  
**Assignment:** 1  
**Instructor Reference:** Cormen et al., *Introduction to Algorithms* (4th ed.), MIT Press (2022)

---

## 🧠 Description
This project implements the **Insertion Sort algorithm** in **monotonically decreasing order**.  
The program demonstrates how each element is inserted into its proper position so the array remains sorted in descending order.

---

## 💻 Code Overview
File: `insertion_sort_descending.py`

Algorithm steps:
1. Start from the second element.
2. Compare it with previous elements.
3. Shift smaller elements rightward.
4. Insert the current element (key) in the correct position.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

---

## 🚀 Example Run
```python
data = [10, 3, 5, 2, 8, 6]
print("Original array:", data)
sorted_data = insertion_sort_desc(data)
print("Sorted array (decreasing):", sorted_data)

output
Original array: [10, 3, 5, 2, 8, 6]
Sorted array (decreasing): [10, 8, 6, 5, 3, 2]
