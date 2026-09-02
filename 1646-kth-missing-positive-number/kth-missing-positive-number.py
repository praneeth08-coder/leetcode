class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ar=set(arr)
        for i in range(1,k+len(arr)+1):
            if i not in ar:
                k-=1
                if k==0:
                    return i