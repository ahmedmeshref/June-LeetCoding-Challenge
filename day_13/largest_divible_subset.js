/**
 * @param {number[]} nums
 * @return {number[]}
 */
let largestDivisibleSubset = function (nums) {
    if (nums.length < 2) return nums;
    nums.sort((a, b) => a - b);
    let res = [];
    for (const num of nums) res.push([num]);
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0 && res[i].length < res[j].length + 1) {
                res[i] = res[j].concat([nums[i]]);
            }
        }
    }
    return max_ele(res);
};

let max_ele = (arr) => {
    let max_len = 0,
        max_so_far;
    for (const lst of arr){
        if (lst.length > max_len){
            max_so_far = lst;
            max_len = lst.length;
        }
    }
    return max_so_far;
}


