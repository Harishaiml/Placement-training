
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(0,len(nums)):
            v=nums[i]
            diff=target-v
            if v not in d:
                d[diff]=i
            else:
                cur=i
                pre=d[v]
                return [cur,pre]
