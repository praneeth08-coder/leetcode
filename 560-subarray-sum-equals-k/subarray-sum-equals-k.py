class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum=0    #this is
        c=0
        seen={0:1}
        for i in nums:
            #compute prefix sum
            csum+=i
            req=csum-k
            if req in seen:
                c+=seen[req]  #add number of times we seen that prefix
            #push the current prefix in hashmap
            seen[csum]=seen.get(csum,0)+1
        return c

        