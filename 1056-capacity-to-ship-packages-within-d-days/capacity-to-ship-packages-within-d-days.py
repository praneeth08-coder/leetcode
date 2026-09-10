def canship(weights,days_have,capacity):
    days_needed=1
    weightsum=0
    for w in weights:
        if weightsum+w <= capacity:
            weightsum+=w
        else:
            days_needed+=1
            weightsum=w
    return days_needed<=days_have
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canship(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low
        