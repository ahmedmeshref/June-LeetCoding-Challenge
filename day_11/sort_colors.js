/**
 * sortColors takes in an an array with n objects colored red: 0, white: 1 or blue: 2, sorts them in-place so that
 * objects of the same color are adjacent, with the colors in the order red, white and blue.
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let sortColors = function (nums) {
    let Obj = {};
    // count the occurrence of each color
    for (const ele of nums) {
        if (ele in Obj) Obj[ele]++;
        else Obj[ele] = 1;
    }
    let c_ind = 0;
    // overwrite the array's indices
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < Obj[i]; j++) {
            nums[c_ind + j] = i;
        }
        c_ind += Obj[i];
    }
    // The return statement is for local testing only and it is not part of the LeetCode challenge solution
    return nums;
};

// the below lines are for testing only and it is not part of the solution
console.log(sortColors([2, 2, 2, 1, 0, 2, 2, 0]))
console.log(sortColors([2, 2, 2, 0, 2, 2, 0]))
console.log(sortColors([2, 2, 2, 1]))
console.log(sortColors([]))