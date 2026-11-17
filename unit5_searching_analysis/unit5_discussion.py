# Tamfor Dulin - CMSC 315 Unit 5 Discussion
# Linear search vs. binary search on student scores


def linear_search(scores, target):
    for i in range(len(scores)):
        if scores[i] == target:
            return i
    return -1


def binary_search(scores, target):
    low = 0
    high = len(scores) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if scores[mid] == target:
            return mid
        elif scores[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


scores = [55, 67, 72, 81, 90, 95]

# 81, which is found (index 3)
print("Search for 81 (found):", linear_search(scores, 81), binary_search(scores, 81))

# 100, which is missing (-1)
print("Search for 100 (missing):", linear_search(scores, 100), binary_search(scores, 100))

# An empty list [] (-1)
print("Empty list []:", linear_search([], 81), binary_search([], 81))

# A one-item list [50] (found at 0, missing at -1)
print("One-item list [50] (found):", linear_search([50], 50), binary_search([50], 50))
print("One-item list [50] (missing):", linear_search([50], 81), binary_search([50], 81))

# 55 and 95, the first and last items (index 0 and index 5)
print("First item 55:", linear_search(scores, 55), binary_search(scores, 55))
print("Last item 95:", linear_search(scores, 95), binary_search(scores, 95))

# Large dataset: 100,000 sorted items, target is the last one (worst case for linear search)
big = list(range(100000))
print("Large list, search for 99999:", linear_search(big, 99999), binary_search(big, 99999))
