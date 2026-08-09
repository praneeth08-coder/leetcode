class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st=s.split(' ')
        ar=st[:k]
        return ' '.join(ar)