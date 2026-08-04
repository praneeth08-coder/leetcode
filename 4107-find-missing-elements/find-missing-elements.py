class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        a=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                a.append(i)
        return a
