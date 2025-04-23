class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                maxSum = max(currSum, maxSum)

        return maxSum       
       
       
       
       
       
       
       
       
       
       
       
        '''
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum = max(currSum, 0)
            currSum += n
            maxSum = max(maxSum, currSum)
        return maxSum '''