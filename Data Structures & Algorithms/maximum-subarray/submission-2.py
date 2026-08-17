class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m,c=nums[0],0
        for i in nums:
            if c < 0 :
               c=0
            c+=i
            if c>m:
                m = c 
        return m 