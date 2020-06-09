/**
 * isSubsequence takes in a string s and a string t and returns true if s is subsequence of t, false otherwise.
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
let isSubsequence = function (s, t) {
    if (s.length > t.length) return false;
    if (s.length === 0) return true;
    let i = j = 0;
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) i++;
        j++;
    }
    return i === s.length;
};


// the below lines are for testing only and it is not part of the solution
const s = "abc",
    t = "ahbgdc";
console.log(isSubsequence(s, t))