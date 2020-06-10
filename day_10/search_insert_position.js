/**
 * searchInsert takes in a sorted array and a target value, it returns the index if the target is found. If not,
 *  return the index where it would be if it were inserted in order.
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
let searchInsert = function(nums, target) {
    let l = 0,
        r = nums.length - 1,
        mid;
    while (l <= r){
        mid = Math.floor((l+r)/2)
        if (target === nums[mid]) return mid;
        else if (target < nums[mid])  r = mid -1;
        else l = mid + 1;
    }
    return l;
};

// the below lines are for testing only and it is not part of the solution
console.log(searchInsert([1, 3, 5, 6], 5))  // 2
console.log(searchInsert([1, 3, 5, 6], 2))  // 1
console.log(searchInsert([1, 3, 5, 6], 7))  // 4
console.log(searchInsert([1, 3, 5, 6], 0))  // 0
console.log(searchInsert([], 5))  // 0
