from collections import Counter


def sort_colors(nums):
    d = Counter(nums)
    c = d[0]
    nums[:c] = [0] * c
    c += d[1]
    nums[d[0]: c] = [1] * d[1]
    nums[c:] = [2] * d[2]
    return nums


print(sort_colors([1, 2, 1, 2, 2, 0, 0]))
