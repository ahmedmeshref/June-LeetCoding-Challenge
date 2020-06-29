/*
    Problem description:
    Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that          at least one duplicate number must exist. Assume that there is only one duplicate number, find the                duplicate one.
    - You must not modify the array (assume the array is read only).
    - You must use only constant, O(1) extra space.
    - Your runtime complexity should be less than O(n2).
    - There is only one duplicate number in the array, but it could be repeated more than once.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
let findDuplicate = function(nums) {
    // Find the intersection point where hare == tort
    hare = tort = nums[0];
    while (true){
        [hare, tort] = [nums[nums[hare]], nums[tort]];
        if (hare === tort) break;
    }

    // Find the interance of the cycle
    tort = nums[0];
    while (hare !== tort){
        [hare, tort] = [nums[hare], nums[tort]];
    }

    return hare
};