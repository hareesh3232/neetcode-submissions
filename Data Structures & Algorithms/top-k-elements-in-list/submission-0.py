class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)

        sort_items=sorted(count,key=count.get,reverse=True)
        return sort_items[:k]