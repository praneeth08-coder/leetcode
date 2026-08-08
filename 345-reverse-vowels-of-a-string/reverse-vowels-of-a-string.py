class Solution:
    def reverseVowels(self, s: str) -> str:
    
        vow='aeiouAEIOU'
        sl=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left < right and sl[left]  not in vow:
                left+=1
            while left < right and sl[right] not in vow:
                right-=1
            if left<right:
                sl[left],sl[right]=sl[right],sl[left]
                left+=1
                right-=1
        return ''.join(sl)