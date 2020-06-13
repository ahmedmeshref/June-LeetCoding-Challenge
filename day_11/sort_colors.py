from collections import Counter


# def sort_colors(nums):
#     d = Counter(nums)
#     c = d[0]
#     nums[:c] = [0] * c
#     c += d[1]
#     nums[d[0]: c] = [1] * d[1]
#     nums[c:] = [2] * d[2]
#     return nums


def sort_colors(nums):

    start = 0
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == 0:
            nums[i], nums[start] = nums[start], nums[i]
            i += 1
            start += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
