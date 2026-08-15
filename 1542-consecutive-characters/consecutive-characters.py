class Solution:
    def maxPower(self, s: str) -> int:
        mxlen=1
        crlen=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                crlen+=1
                mxlen=max(mxlen,crlen)
            else:
                crlen=1
        return mxlen