class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0 
        maxi=nums[0]
        for num in nums:
            curr=max(num,num+curr)
            maxi=max(curr,maxi)
        return maxi
        