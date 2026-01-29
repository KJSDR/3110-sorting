#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n + m) where n = len(items1) and m = len(items2)
    TODO: Memory usage: O(n + m) we create a new list to store all merged items"""
    
    merged = []
    i, j = 0, 0

    #repeat until one list is empty
    while i < len(items1) and j < len(items2):
        #find minimum item in both lists and append it to new list
        if items1[i] <= items2[j]:
            merged.append(items1[i])
            i += 1
        else:
            merged.append(items2[j])
            j += 1

    #append remaining items in nonempty list to a new list
    merged.extend(items1[i:])
    merged.extend(items2[j:])

    return merged
            

    
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
     sorting each with an iterative sorting algorithm, and merging results into
     a list in sorted order.
    TODO: Running time: its dominated by the iterative sorting algo used on each of the halves.
    Even if we split list, bubble and insertion sort on two half is still O(n^2) overall.
    TODO: Memory usage: O(n) we create new lists for plsittign and merging"""
     
     #check if list is too small and its already sorted
    if len(items) <= 1:
        return items

    #split items list into approximately equal halves
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    #sort each half using any other sorting algo with bubble sort
    bubble_sort(left)
    bubble_sort(right)

    #merge sorted halves into one list in sorted order
    return merge(left, right)



    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(nlogn) in all cases, we divided the list log n times and 
    each level we do O(n) work to merge all sublists. So O(n) x O(logn) = O(n log n)
    TODO: Memory usage: O(n) we create temporary lists during splitting and merging.
    Recursion gets to O(log n) but each step or level is O(n) space in total"""
    
    #check if list is already sorted
    if len(items) <= 1:
        return items

    #split items list into approximeately equal halves
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    #sort each half recursively called merge sort
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    #merged sorted halves into one list in sorted order
    merged = merge(left_sorted, right_sorted)

    #copy merged items back into roginal list
    for i in range(len(items)):
        items[i] = merged[i]

    return items



def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot from that range and we move the pivot into the index "p" and items
    less than pivot into range low - p1 and items greater than pivot into range p+1 - high
    
    TODO: Running time: O(n) where n is high - low + 1. We have to iterate through the range once.
    TODO: Memory usage: O(1) we only use a constant amount of extra space for indices"""
    
    #choose the last element as pivot
    pivot = items[high]

    #index for smaller element
    i = low - 1

    #loop through all items in range low....high-1
    for j in range (low, high):
        #move items less than or equal to the pivot into front of range
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]

    #move pivot items into pivot position
    i += 1
    items[i], items[high] = items[high], items[i]

    #return index of p
    return i


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log n) when we pivot consistnet it divides the
    list into two rough equal halves. and the tree depth is the same with O(n) of work per level
    TODO: Worst case running time: O(n^2) when the pivot is always the smallest or largest elemtent
    it creates an unbalanced partitions with three depth of O(n)
    TODO: Memory usage: O(log n) best case and O(n) worst case becaue of recursion stack depth"""
    
    #check if high and low range bounds have default values
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    
    #check if list or range is small it is already sorted
    if low < high:
        #partician items in place around a pivot and get indox of pivot
        p = partition(items, low, high)

        #sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p - 1)
        quick_sort(items, p + 1, high)

    return items