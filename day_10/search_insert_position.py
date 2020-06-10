def searchInsert(nums, target):
    """
    searchInsert takes in a sorted array and a target value, it returns the index if the target is found. If not,
    return the index where it would be if it were inserted in order.
    :param nums: Sorted []
    :param target: Integer
    :return: Integer
    """

    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    # if equal value was not found, l will point to the first element greater than target
    return l


# the below lines are for testing only and it is not part of the solution
print(searchInsert([1, 3, 5, 6], 5))  # 2
print(searchInsert([1, 3, 5, 6], 2))  # 1
print(searchInsert([1, 3, 5, 6], 7))  # 4
print(searchInsert([1, 3, 5, 6], 0))  # 0
print(searchInsert([], 5))  # 0
