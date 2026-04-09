## Optimized Bubble Sort in Python

## Overview

This program implements an optimized Bubble Sort algorithm in Python to sort a list of integers in ascending order. It also includes a custom input function that allows users to dynamically create a list through the command line.

The implementation uses a swap-detection optimization to terminate early if the list becomes sorted before completing all passes.

---

## Features

- Written in Python with a modular function-based design
- Custom input system using "get_input()" for dynamic list creation
- Interactive command-line interface for user control
- Early termination using a swap flag
- Reduced comparisons per pass (optimized loop range)
- In-place sorting (no additional memory required)
- Clean and beginner-friendly implementation focused on learning algorithms

---

## Algorithm Concept

1. Compare adjacent elements in the list.
2. Swap them if they are in the wrong order.
3. After each pass, the largest unsorted element moves to its correct position.
4. If no swaps occur in a pass, the algorithm stops early.

---

## Input Method

The program uses a custom function "get_input()" to build the list:

- Users enter elements one by one.
- Input continues until the user chooses to stop.
- Ensures controlled and flexible list creation.

---

## Example Output

Input:
3 1 4 2

Output:
Sorted: [1, 2, 3, 4]

---

## Author's Note

Built as part of my learning journey in algorithms and Python programming. This project focuses on understanding sorting logic, improving program structure, and implementing optimization techniques through hands-on problem solving.
