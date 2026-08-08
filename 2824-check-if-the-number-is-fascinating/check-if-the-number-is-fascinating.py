class Solution:
    def isFascinating(self, n: int) -> bool:
        n_2=2*n
        n_3=3*n
        a= str(n_2)+str(n_3)+str(n)
        if len(a)!=9:
                return False
        for i in range(1,10):
            if str(i) not in a:
                return False
        return True