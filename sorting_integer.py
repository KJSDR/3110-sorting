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
    TODO: Running time: O(n+k) average case when items are distributed are evenely across the buckets. 
    Wosrt case is O(n^2) if all items are in one bucket
    TODO: Memory usage: O(n+k) where n is for storing the items in buckets and k is the number of buckets"""
    
    #check if list is empty or has element
    if len(numbers) <= 1:
        return

    #find range of given number min max values
    min_val = min(numbers)
    max_val = max(numbers)

    #handle adge case where all numbers are same
    if min_val == max_val:
        return

    #create list of buckets to store numbers in subranges on input range
    buckets = [[] for _ in range(num_buckets)]

    #calc range of each bucket
    range_size = (max_val - min_val) / num_buckets

    #loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        #dtermine which bucksts number belongs to
        bucket_index = int((num - min_val) / range_size)
        #handle edge case where num == max_val
        if bucket_index == num_buckets:
            bucket_index = num_buckets - 1
        buckets[bucket_index].append(num)

    #sort each bucket using ANY sortign algo
    for bucket in buckets:
        insertion_sort(bucket)
    
    #loop over buckets and appench each buckets numbers into ouput list
    index = 0
    for bucket in buckets:
        for num in buckets:
            numbers[index] = num
            index += 1