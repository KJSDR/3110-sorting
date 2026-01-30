#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n+k) where n is number of items and k is the range so max - min. All cases are same here we only count and reconctrusct
    TODO: Memory usage: O(k) for every count in array where k is the range of the values"""
    
    #check if list is empty or has one element
    if len(numbers) <= 1:
        return

    #find range of given numbers min and max values
    min_val = min(numbers)
    max_val = max(numbers)
    range_size = max_val - min_val + 1

    #create list of counts with a slot for each number in input range
    counts = [0] * range_size

    #loop over given numbers and incremement each number count
    for num in numbers:
        counts[num - min_val] += 1

    #loop over counts and append that many numbers into output list
    index = 0
    for values in range(range):
        count = counts[value]
        for _ in range(count):
            numbers[index] = value + min_val
            index += 1

    


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list