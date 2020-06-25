"""
    Problem description:
    Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that          at least one duplicate number must exist. Assume that there is only one duplicate number, find the                duplicate one.
    - You must not modify the array (assume the array is read only).
    - You must use only constant, O(1) extra space.
    - Your runtime complexity should be less than O(n2).
    - There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Get the intersection point of the two runners where hare == tortoise.
        tortoise = hare = nums[0]
        while True:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
            if hare == tortoise:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise, hare = nums[tortoise], nums[hare]

        return hare