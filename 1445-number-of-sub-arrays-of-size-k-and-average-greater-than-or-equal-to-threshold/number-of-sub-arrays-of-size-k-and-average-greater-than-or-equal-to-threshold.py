class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        first_window = arr[:k]
        cur_sum = sum(first_window)
        c = 0
        if cur_sum / k >= threshold:
            c += 1
        for i in range(k, len(arr)):
            cur_sum = cur_sum + arr[i] - arr[i - k]
            if cur_sum / k >= threshold:
                c += 1
        return c
