/*
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
 */


/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    let l = 0,
        h = citations.length - 1,
        papers, mid;
    while (l <= h){
        mid = Math.floor((l + h)/2);
        papers = citations.length - mid;
        if (papers === citations[mid]) return papers;
        else if (papers > citations[mid]) l = mid+1;
        else h = mid -1;
    }
    return citations.length - l;
};


// This part is for testing only any not part of the leetcode solution
let c;
c = [100]
console.log(hIndex(c))
c = []
console.log(hIndex(c))
c = [0, 3, 5]
console.log(hIndex(c))
c = [0, 1, 3, 4, 5]
console.log(hIndex(c))
