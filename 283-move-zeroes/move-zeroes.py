class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zco=nums.count(0)
        for i in range(zco):
            nums.remove(0)
            nums.append(0)
        return nums