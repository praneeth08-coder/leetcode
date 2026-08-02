class Solution:
    def reverseWords(self, s: str) -> str:
        st=s[::-1]
        a=st.split()
        b=a[::-1]
        c=' '.join(b)
        return c