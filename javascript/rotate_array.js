//Given an array, rotate the array to the right by k steps, where k is non-negative.

//Example 1:

//Input: [1,2,3,4,5,6,7] and k = 3
//Output: [5,6,7,1,2,3,4]
//Explanation:
//rotate 1 steps to the right: [7,1,2,3,4,5,6]
//rotate 2 steps to the right: [6,7,1,2,3,4,5]
//rotate 3 steps to the right: [5,6,7,1,2,3,4]
//Example 2:

//Input: [-1,-100,3,99] and k = 2
//Output: [3,99,-1,-100]
//Explanation: 
//rotate 1 steps to the right: [99,-1,-100,3]
//rotate 2 steps to the right: [3,99,-1,-100]
//Note:

//Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
//Could you do it in-place with O(1) extra space?

const rotate = function(nums, k) {
    if(nums.length === 1 || k === 0) return nums
    let temp = nums[0]
    let start = 0
    for(let i=0; i<nums.length; i++) {
        const idx = (((i+1)*k + start) % nums.length)
        let tmp = nums[idx]
        nums[idx] = temp
        temp = tmp
        if(idx === start) {
            start = ++start%nums.length
            temp = nums[start]
        }
    }
    print(nums)
}

const ex1 = [[1,2,3,4,5,6,7], 3] //[5,6,7,1,2,3,4]
const ex2 = [[-1,-100,3,99], 2] //[3,99,-1,-100]
const ex3 = [[1,2], 3] //[2,1]

rotate(ex1[0], ex1[1])
rotate(ex2[0], ex2[1])
rotate(ex3[0], ex3[1])