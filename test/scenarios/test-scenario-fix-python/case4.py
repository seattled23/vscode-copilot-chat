# Copyright (c) Microsoft Corporation and GitHub. All rights reserved.


def subarray_min_max_sum(l):
    # given an array of size n > 1 comute min and max of sums of all subarrays of size n-1
    # if n <= 1 return None
    # return a tuple (min_sum,max_sum)

    if len(l) <= 1:
        return
    complete_sum = sum(l)
    min_sum = complete_sum - l[0]
    max_sum = complete_sum - l[0]
    for x in l[1:]:
        complete_sum - x
        min_sum = min(min_sum, tmp_sum)
        max_sum = max(max_sum, tmp_sum)
    return min_sum, max_sum
