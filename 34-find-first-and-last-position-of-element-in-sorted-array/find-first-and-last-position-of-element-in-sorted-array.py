import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            a=bisect.bisect_left(nums,target)
            b=bisect.bisect_right(nums,target)
            if a==b:
                return [-1,-1]
            else:
                return [a,b-1]