class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                c+=1
        return c

