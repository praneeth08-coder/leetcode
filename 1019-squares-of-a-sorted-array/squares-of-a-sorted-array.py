class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        b=[abs(i**2) for i in nums]
        b.sort()
        return b