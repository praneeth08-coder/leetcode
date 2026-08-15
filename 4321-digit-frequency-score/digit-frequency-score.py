class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = str(n)
        score = sum(int(d) * s.count(d) for d in set(s))
        return score
