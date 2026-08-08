class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        nstr=str(n)
        xstr=str(x)
        if xstr in nstr and nstr[0]!=xstr:
            return True
        else:
            return False