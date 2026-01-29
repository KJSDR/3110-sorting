#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) - Best, worst, and average case are all O(n) because we have to check each pair of items once
    TODO: Memory usage: O(1) - We only use a loop counter, no extra arrays or lists"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) - Worst and average case because we loop through the list multiple times.
    Best case is O(n) if the list is already sorted and we detect no swaps happened
    TODO: Memory usage: O(1) - We sort in place by swapping items, no extra space needed"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    n = len(items)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) - Always O(n^2) for best, worst, and average cases because we always search through 
    remaining items to find the minimum, even if already sorted
    TODO: Memory usage: O(1) - We sort in place, just swap items around"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    n = len(items)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) - Worst and average case when items are reversed or random.
    Best case is O(n) when the list is already sorted because we just check each item once
    TODO: Memory usage: O(1) - We sort in place by shifting items, no extra arrays needed"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current