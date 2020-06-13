/**
 * sortColors takes in an an array with n objects colored red: 0, white: 1 or blue: 2, sorts them in-place so that
 * objects of the same color are adjacent, with the colors in the order red, white and blue.
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let sortColors = function (nums) {
    let start = 0,
        i = 0,
        j = nums.length - 1;
    while (i <= j){
        if (nums[i] === 0){
            [nums[i], nums[start]] = [nums[start], nums[i]];
            i++; start++;
        } else if (nums[i] === 1) {
            i++;
        } else {
            [nums[i], nums[j]] = [nums[j], nums[i]];
            j--;
        }
    }
};



